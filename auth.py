import hashlib
from datetime import UTC, datetime, timedelta, timezone

import bcrypt
from authx import AuthX, AuthXConfig

SECRET_KEY = "vrtvttgtt76hv"
ALGORITHM = "HS256"

config = AuthXConfig(
    JWT_SECRET_KEY=SECRET_KEY,
    JWT_TOKEN_LOCATION=["cookies"],
    JWT_ALGORITHM=ALGORITHM,
    JWT_ACCESS_COOKIE_NAME="access_token",
    JWT_REFRESH_COOKIE_NAME="refresh_token",
    JWT_ACCESS_TOKEN_EXPIRES=15,
    JWT_REFRESH_TOKEN_EXPIRES=60*24*7,
    JWT_COOKIE_CSRF_PROTECT=True,
    JWT_COOKIE_HTTP_ONLY=True,
    JWT_COOKIE_SECURE=False,
    JWT_COOKIE_SAMESITE="lax",
)

auth = AuthX(config=config)


def verify_password(password: str, hashed_password: str) -> bool:
    """Verifying password"""
    password_bytes = password.encode("utf-8")
    hashed_password_bytes = hashed_password.encode("utf-8")
    
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)
    

def get_hashed_password(password: str) -> str:
    """Hashing password"""
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    
    return hashed_bytes.decode("utf-8")


def get_hashed_token(token: str) -> str:
    """Hashing token"""
    return hashlib.sha256(token.encode("utf-8")).hexdigest()

def verify_token(token: str, hashed_token: str) -> bool:
    return hashlib.sha256(token.encode("utf-8")).hexdigest() == hashed_token


