from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth, applications

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job Application Tracker API")

app.include_router(auth.router)
app.include_router(applications.router)