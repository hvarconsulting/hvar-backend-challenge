from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.models.database import Session, get_db_session

# Import the models from their respective modules
from app.models import User
from app.middleware import auth


def generate_jwt(user: User) -> str:
    return auth.generate_jwt(user.username)


# Define the request and response models for the API
class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str


router = APIRouter()


# Define the route for the login endpoint
@router.post("/login")
async def login(request: LoginRequest,
                session: Session = Depends(get_db_session)):
    # Look up the user in the database
    user = session.query(User).filter_by(username=request.username).first()

    # Check if the user exists and their password is correct
    if user is None or user.password != request.password:
        raise HTTPException(status_code=401,
                            detail="Invalid username or password.")

    # Generate a JSON web token (JWT)
    token = generate_jwt(user)

    # Return the JWT in the response
    return LoginResponse(token=token)
