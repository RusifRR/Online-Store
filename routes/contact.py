from fastapi import APIRouter, Request

from templates import templates

router = APIRouter()


@router.get('/contact', include_in_schema=False)
def contact(request: Request):
    """Return contact page"""
    return templates.TemplateResponse(request, 'contact.html')