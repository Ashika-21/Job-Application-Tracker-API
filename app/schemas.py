from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class ApplicationCreate(BaseModel):
    company_name: str
    job_role: str
    location: str
    application_status: str
    applied_date: date
    salary: float


class ApplicationResponse(ApplicationCreate):
    id: int
    owner_id: int

    class Config:
        from_attributes = True