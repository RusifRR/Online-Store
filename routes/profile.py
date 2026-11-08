from fastapi import APIRouter, Request

from auth_settings import auth
from templates import templates

router = APIRouter()

@router.get('/profile')
def get_profile(request: Request):
    """Return profile page"""
    payload = auth.access_token_required(request)
    return payload
    