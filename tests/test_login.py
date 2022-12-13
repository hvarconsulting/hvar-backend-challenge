import json
from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.models.database import get_db_session
from app.models import User
from app.views import users
from app.middleware.auth import validate_jwt

# define the test client
app = FastAPI()
app.include_router(users.router)
client = TestClient(app)


async def mock_get_db_session():
    session = MagicMock()
    session.query.return_value.filter_by.return_value.first.return_value = \
        User(
            username="test",
            password="test"
        )
    return session


# override the dependencies
app.dependency_overrides[get_db_session] = mock_get_db_session


# test the login endpoint
def test_login():
    data = {"username": "test", "password": "test"}
    response = client.post("/login",
                           content=json.dumps(data),
                           headers={
                               "Content-Type": "application/json",
                           })

    # check the response
    assert response.status_code == 200

    # check the token
    token = response.json()["token"]
    assert validate_jwt(token) == "test"
