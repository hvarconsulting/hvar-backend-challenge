from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.models.database import Session, get_db_session
from app.models.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ACCESS_TOKEN_EXPIRE_MINUTES = 60
ALGORITHM = "HS256"
JWT_SECRET_KEY = "super-secret-key"


class CredentialsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


class NotImplementedException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_501_NOT_IMPLEMENTED,
                         detail="Not implemented")


def validate_jwt(token: str) -> str:
    raise NotImplementedException()


async def authenticate_user(token: str = Depends(oauth2_scheme),
                            session: Session = Depends(get_db_session)):
    # Validate the JWT
    username = validate_jwt(token)

    # Look up the user in the database
    user = session.query(User).filter_by(username=username).first()
    if user is None:
        raise CredentialsException()
    return user


def generate_jwt(subject) -> str:
    raise NotImplementedException()
