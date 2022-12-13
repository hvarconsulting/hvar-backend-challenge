from fastapi import FastAPI

# Import the views from their respective modules
# from app.views import weather, users
from app.views import users, weather

# Create an instance of the FastAPI app
app = FastAPI()

# Register the views with the app
# app.include_router(weather.router)
app.include_router(users.router)
app.include_router(weather.router)
