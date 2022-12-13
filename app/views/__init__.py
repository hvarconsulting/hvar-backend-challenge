from fastapi import APIRouter

# Import the users module from the users package
from . import users, weather

# Define a router object for the users package
router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(weather.router, prefix="/weather", tags=["weather"])
