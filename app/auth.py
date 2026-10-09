import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
print("ALGORITHM =", ALGORITHM)
EXPIRE = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

pwd = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def hash_password(password):
    return pwd.hash(password)


def check_password(password, hashed):
    return pwd.verify(password, hashed)


def create_token(username):
    exp = datetime.utcnow() + timedelta(minutes=EXPIRE)
    return jwt.encode(
        {"sub": username, "exp": exp},
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def verify_token(token):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        return verify_token(token)["sub"]
    except:
        raise HTTPException(401, "Invalid or expired token")