from fastapi import APIRouter, HTTPException, Depends, status
from pydantic import BaseModel

from app.models.database import Session, get_db_session


# Define the request and response models for the API
class WeatherRequest(BaseModel):
    date: str
    time: str
    state: str


class WeatherResponse(BaseModel):
    date: str
    time: str
    state: str
    precipitation: float
    temperature: float


class NotImplementedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                         detail="Not implemented")


router = APIRouter()


# Define the route for the login endpoint
# only allow authenticated users to access this endpoint
@router.post("/weather", response_model=WeatherResponse)
async def get_weather(request: WeatherRequest,
                      session: Session = Depends(get_db_session)):
    raise NotImplementedException()
