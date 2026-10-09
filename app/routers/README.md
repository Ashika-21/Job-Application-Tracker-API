# Job Application Tracker API

## Project Description

The Job Application Tracker API is a backend application developed using FastAPI and SQLite. It helps users manage and track their job applications.

Users can register, log in, and perform CRUD operations on their job applications securely using JWT authentication.

## Technologies Used

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- JWT Authentication
- Bcrypt Password Hashing
- Uvicorn

## Features

- User registration and login
- Secure password hashing
- JWT token authentication
- Create a job application
- View all job applications
- View a single job application
- Update job application details
- Delete a job application
- Pagination using skip and limit
- User-specific application access
- Request and response validation

## Job Application Fields

Each job application contains:

- Company Name
- Job Role
- Location
- Application Status
- Applied Date
- Salary

## Project Structure

```text
Job_Application_Tracker/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── applications.py
├── requirements.txt
├── README.md
└── .env.example