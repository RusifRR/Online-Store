from datetime import UTC, datetime
from enum import Enum as PyEnum

from sqlalchemy import Boolean, DateTime, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class UserRole(PyEnum):
    """"User roles"""
    user = "user"
    worker = "worker"
    admin = "admin"


class ProductCategory(PyEnum):
    """Category parameters"""
    earbuds = "earbuds"
    headband = "headband"
    accessory = "accessory"
    


class User(Base):
    """User table"""
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.user, server_default="user", nullable=False)
    refresh_token: Mapped[str] = mapped_column(String(64), nullable=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    

class Product(Base):
    """Product table"""
    __tablename__= "products"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[ProductCategory] = mapped_column(Enum(ProductCategory), nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=False)




# class Order(Base):
#     """Order table"""
#     __tablename__ = "orders"
    
#     pass
    



    
    
    