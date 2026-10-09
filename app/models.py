from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)


class JobApplication(Base):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    job_role = Column(String)
    location = Column(String)
    application_status = Column(String)
    applied_date = Column(Date)
    salary = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))