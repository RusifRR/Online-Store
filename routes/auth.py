from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, Form, HTTPException, Request, Response, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from auth_settings import (
    auth,
    get_hashed_password,
    get_hashed_token,
    verify_password,
    verify_token,
)
from database import get_db
from models import User
from schemas import UserLogin, UserRegister, UserResponse

router = APIRouter()

template = Jinja2Templates(directory="templates")


@router.get('/register', include_in_schema=False)
def get_register(request: Request):
    """Return register page"""
    return template.TemplateResponse(request, 'register.html')

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(
    request: Request,
    user: Annotated[UserRegister, Form()], 
    db: Annotated[Session, Depends(get_db)],
):
    """Register a new user"""
    if user.password != user.confirming_password:
        return template.TemplateResponse(request, 'register.html', {'error': 'Пароли не совпадают'})
    result = db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        return template.TemplateResponse(request, 'register.html', {'error': 'Пользователь с таким email уже существует'})
    
    new_user = User(
        name=user.name,
        surname=user.surname,
        email=user.email,
        hashed_password=get_hashed_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = auth.create_access_token(uid=str(new_user.id))
    refresh_token = auth.create_refresh_token(uid=str(new_user.id))
    new_user.refresh_token = get_hashed_token(refresh_token)
    new_user.expires_at = datetime.now(tz=UTC) + timedelta(days=7)
    db.commit()
    db.refresh(existing_user)
    response = RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)
    auth.set_access_cookies(access_token, response)
    auth.set_refresh_cookies(refresh_token, response)
    
    return response
    

@router.get('/login', include_in_schema=False)
def get_login(request: Request):
    """Return login page"""
    return template.TemplateResponse(request, 'login.html')


@router.post('/login', status_code=status.HTTP_200_OK)
def login(
    request: Request,
    user: Annotated[UserLogin, Form()], 
    db: Annotated[Session, Depends(get_db)], 
) -> dict:
    """Login a user"""
    result = db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if not existing_user or not verify_password(user.password, existing_user.hashed_password):
        return template.TemplateResponse(request, 'login.html', {'error': 'Неверный email или пароль'})
    access_token = auth.create_access_token(uid=str(existing_user.id))
    refresh_token = auth.create_refresh_token(uid=str(existing_user.id))
    existing_user.refresh_token = get_hashed_token(refresh_token)
    existing_user.expires_at = datetime.now(tz=UTC) + timedelta(days=7)
    db.commit()
    db.refresh(existing_user)
    response = RedirectResponse(url='/', status_code=status.HTTP_303_SEE_OTHER)
    auth.set_access_cookies(access_token, response)
    auth.set_refresh_cookies(refresh_token, response)
        
    return response
    
    

    
    
        