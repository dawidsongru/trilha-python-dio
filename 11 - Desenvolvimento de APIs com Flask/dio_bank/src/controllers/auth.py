from http import HTTPStatus

from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from sqlalchemy import inspect
from app import User, db

# localhost:5000/users
app = Blueprint("auth", __name__, url_prefix="/auth")


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORRIZED

    access_token = create_access_token(identity=username)
    return {"access_token": access_token}
