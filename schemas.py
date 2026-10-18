from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    surname: str = Field(min_length=1, max_length=100)
    email: EmailStr = Field(mmax_length=120)
    password: str = Field(min_length=8)
    confirming_password: str = Field(min_length=8)
    
    
class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=120)
    password: str = Field(min_length=8)
    

class UserResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    
    class Config:
        from_attributes = True