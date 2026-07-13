from fastapi import FastAPI
from app.database import engine, Base
from app.routers import student

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API")

app.include_router(student.router)