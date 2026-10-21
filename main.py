
from fastapi import FastAPI

from auth_settings import auth
from database import Base, engine
from routes.auth import router as auth_router

app = FastAPI()

auth.handle_errors(app=app)

Base.metadata.create_all(engine)

app.include_router(auth_router)


