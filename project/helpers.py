import calendar
import datetime
import jwt
from project.constants import (
    JWT_ALGORITHM,
    JWT_SECRET,
    TOKEN_EXPIRE_DAYS,
    TOKEN_EXPIRE_MINUTES,
)

from flask import abort, session


def generate_tokens(data: dict) -> dict:
    minutes = datetime.datetime.utcnow() + datetime.timedelta(
        minutes=TOKEN_EXPIRE_MINUTES
    )
    data["exp"] = calendar.timegm(minutes.timetuple())
    access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    days = datetime.datetime.utcnow() + datetime.timedelta(days=TOKEN_EXPIRE_DAYS)
    data["exp"] = calendar.timegm(days.timetuple())
    refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


def encode_token(token: str) -> dict:
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except Exception:
        return False
    return data


def auth_required(func):
    def wrapper(*args, **kwargs):
        if not (token := session.get("token")):
            abort(401)
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception:
            abort(401)
        return func(*args, *kwargs)

    return wrapper
