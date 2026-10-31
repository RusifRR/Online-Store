from typing import Annotated

from fastapi import APIRouter, Depends, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from models import Product
from templates import templates

router = APIRouter()

@router.get("/", include_in_schema=False)
def home(request: Request, db: Annotated[Session, Depends(get_db)]):
    """Return home page"""
    products = db.execute(select(Product)).scalars().all()
    return templates.TemplateResponse(request, "index.html", context={"products": products})
    





