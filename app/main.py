from fastapi import FastAPI
from app.controllers import controller_router, health_router

app = FastAPI()
app.include_router(controller_router)
app.include_router(health_router)
