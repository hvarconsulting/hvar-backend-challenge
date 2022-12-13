import json
from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.middleware.auth import authenticate_user
from app.models import Weather
from app.models.database import get_db_session
from app.views.weather import router

# define the test client
app = FastAPI()
app.include_router(router)
client = TestClient(app)


async def mock_get_db_session():
    session = MagicMock()
    session.query.return_value.filter.return_value.first.return_value = \
        Weather(
            date="2022-01-01",
            time="00:00",
            state="SP",
            precipitation=0.0,
            temperature=0.0
        )
    return session


async def mock_authenticate_user():
    return True


# override the dependencies
app.dependency_overrides[get_db_session] = mock_get_db_session
app.dependency_overrides[authenticate_user] = mock_authenticate_user


def test_get_weather():
    data = {"date": "2022-01-01", "time": "00:00", "state": "SP"}
    response = client.post("/weather",
                           content=json.dumps(data),
                           headers={
                               "Content-Type": "application/json",
                               "Authorization": "Bearer token"
                           })

    assert response.status_code == 200
    assert response.json() == {
        "date": "2022-01-01",
        "time": "00:00",
        "state": "SP",
        "precipitation": 0.0,
        "temperature": 0.0
    }
