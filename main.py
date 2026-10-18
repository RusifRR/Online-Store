from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from auth import (
    auth,
    get_hashed_password,
    get_hashed_token,
    verify_password,
    verify_token,
)
from database import Base, engine, get_db
from models import User
from schemas import UserLogin, UserRegister, UserResponse

app = FastAPI()

auth.handle_errors(app=app)

Base.metadata.create_all(engine)


@app.post('/register', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserRegister, db: Annotated[Session, Depends(get_db)]) -> UserResponse:
    """Register a new user"""
    result = db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists"
        )
    
    new_user = User(
        name=user.name,
        surname=user.surname,
        email=user.email,
        hashed_password=get_hashed_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
    


@app.post('/login', status_code=status.HTTP_200_OK)
def login(user: UserLogin, db: Annotated[Session, Depends(get_db)], response: Response) -> dict:
    """Login a user"""
    result = db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if not existing_user or not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    access_token = auth.create_access_token(uid=str(existing_user.id))
    refresh_token = auth.create_refresh_token(uid=str(existing_user.id))
    existing_user.refresh_token = get_hashed_token(refresh_token)
    existing_user.expires_at = datetime.now(tz=UTC) + timedelta(days=7)
    db.commit()
    db.refresh(existing_user)
    auth.set_access_cookies(access_token, response)
    auth.set_refresh_cookies(refresh_token, response)
    
    return {"message": "Вы успешно вошли в систему"}
    
    

    
    
        