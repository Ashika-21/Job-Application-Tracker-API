from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import JobApplication, User
from app.schemas import ApplicationCreate
from app.auth import get_current_user

router = APIRouter(prefix="/applications")


@router.post("/")
def create_application(
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == username).first()

    new_app = JobApplication(
        **application.model_dump(),
        owner_id=user.id
    )

    db.add(new_app)
    db.commit()
    db.refresh(new_app)

    return new_app


@router.get("/")
def get_applications(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == username).first()

    return db.query(JobApplication).filter(
        JobApplication.owner_id == user.id
    ).offset(skip).limit(limit).all()


@router.get("/{application_id}")
def get_application(
    application_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == username).first()

    app = db.query(JobApplication).filter(
        JobApplication.id == application_id,
        JobApplication.owner_id == user.id
    ).first()

    if not app:
        raise HTTPException(404, "Application not found")

    return app


@router.put("/{application_id}")
def update_application(
    application_id: int,
    application: ApplicationCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == username).first()

    app = db.query(JobApplication).filter(
        JobApplication.id == application_id,
        JobApplication.owner_id == user.id
    ).first()

    if not app:
        raise HTTPException(404, "Application not found")

    for key, value in application.model_dump().items():
        setattr(app, key, value)

    db.commit()
    db.refresh(app)

    return app


@router.delete("/{application_id}")
def delete_application(
    application_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_user)
):
    user = db.query(User).filter(User.username == username).first()

    app = db.query(JobApplication).filter(
        JobApplication.id == application_id,
        JobApplication.owner_id == user.id
    ).first()

    if not app:
        raise HTTPException(404, "Application not found")

    db.delete(app)
    db.commit()

    return {"message": "Application deleted successfully"}