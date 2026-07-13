from fastapi import FastAPI 
from app.database import engine, Base
from app.routers.product_router import router

Base.metadata.create_all(bind=engine)

product_api = FastAPI(title='Product Management API')

product_api.include_router(router)