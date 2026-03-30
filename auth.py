# auth.py

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"])

SECRET_KEY = "your_secret"
ALGORITHM = "HS256"

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

# Create JWT token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)