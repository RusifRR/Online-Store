
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from auth_settings import auth
from database import Base, engine
from routes.auth import router as auth_router
from routes.contact import router as contact_router
from routes.index import router as index_router

app = FastAPI()

app.mount("/statics", StaticFiles(directory="statics"), "statics")

auth.handle_errors(app=app)

Base.metadata.create_all(engine)

app.include_router(auth_router)
app.include_router(index_router)
app.include_router(contact_router)
