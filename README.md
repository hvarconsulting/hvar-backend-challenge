# Weather API

## Introduction

This is a challenge for a weather API that will read data from a JSON file and provide users with the ability to request weather information for a specific date, time, and state in Brazil. The API will have a database of users, and will use middleware to control authentication.

## Requirements

- The API must be written in Python using FastAPI.
- All weather data must be read from a JSON file containing information for each day and city in Brazil.
- The API must have a database of users, as well as middleware to control authentication.
- Users must be limited to 30 requests per day. If a user exceeds this limit, the API must return a 403 status code and inform the user that their quota has been reached.
- The code must be written using clean architecture, with clear separation of models, views, and controllers.
- Users must be able to parametrize their requests with date, time, and state.

## Usage

To use the API, users must first authenticate using their username and password. Once authenticated, they can make requests to the API using the following parameters:

- `date`: The date for which to retrieve weather information, in the format `YYYY-MM-DD`.
- `time`: The time for which to retrieve weather information, in the format `hh:mm`.
- `state`: The state for which to retrieve weather information, as a string.

An example request might look like this:

```bash
# get auth token
curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "test", "password": "test"}' \
    http://localhost:8000/login

# request
curl -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization Bearer <token>" \
    --data-raw '{"date": "2022-12-06", "time": "12:00:00", "state": "SP"}' \
    http://localhost:8000/weather
```

> ⚠ **Note**: The API will only accept requests for dates in the year 2022.

If the user has not exceeded their daily request quota, the API will return the weather information for the specified date, time, and state in the following JSON format:

```json
{
    "date": "2022-12-06",
    "time": "12:00:00",
    "state": "SP",
    "temperature": 25.5,
    "precipitation": 0.0
}
```

If the user has exceeded their daily request quota, the API will return a 402 status code and the following JSON response:

```json
{
    "message": "Daily request quota exceeded. Please try again tomorrow."
}
```


## Challenge

The base implementation of the API is provided in the `app` directory. Models, views, and controllers are already defined, as well as the database of users and the sqlite file containing weather data. The challenge is to complete the implementation of the API by writing the following:

- The `get_weather` function in `app/controllers/weather.py`, which will retrieve weather information from the database and return it to the user.
- The `generate_jwt` function in `app/controllers/auth.py`, which will generate a JWT token for the user.
- The `validate_jwt` function in `app/controllers/auth.py`, which will validate the user's JWT token.
- The `get_weather` authentication middleware in `app/controllers/weather.py`, which will validate the user's JWT token.

Follow the API's documentation to understand how the API is expected to behave.

# Extra Challenge

The extra challenge is to implement a rate limiter that will limit the number of requests a user can make per day. The rate limiter should be implemented following the architecture of the API, and should be able to be used in other parts of the API.

# Testing

To test the API, run the following command:

```bash
python -m pytest
```

Use the requests in the Usage section to test the API manually. You can run the API using the following command:

```bash
uvicorn main:app --reload
```

## Conclusion

This challenge is designed to evaluate a developer's ability to write a weather API using Python and FastAPI, as well as their understanding of clean architecture and the principles of authentication and rate limiting. Successfully completing this challenge will demonstrate a candidate's proficiency in these areas.

