from fastapi import APIRouter
from endpoints import users

API_router = APIRouter()

API_router.include_router(users.router, prefix="/users")