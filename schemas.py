from fastapi import Form
from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    name: str = Form(min_length=1, max_length=100)
    surname: str = Form(min_length=1, max_length=100)
    email: EmailStr = Form(max_length=120)
    password: str = Form(min_length=8)
    confirming_password: str = Form(min_length=8)
    
    
class UserLogin(BaseModel):
    email: EmailStr = Form(max_length=120)
    password: str = Form(min_length=8)
    

class UserResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    
    class Config:
        from_attributes = True