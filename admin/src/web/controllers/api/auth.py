from src.web.helpers.build_response import response
from src.core.auth import get_by_usr_and_pwd, get_user_by
from flask import Blueprint, request, jsonify
from src.web.config import Config
from functools import wraps
import jwt

from flask_jwt_extended import (
    create_access_token,
    set_access_cookies,
    jwt_required,
    unset_jwt_cookies,
    get_jwt_identity,
)

auth_api_blueprint = Blueprint("auth_api", __name__, url_prefix="/auth")


@auth_api_blueprint.post("/login")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    user = get_by_usr_and_pwd(username, password)
    if user:
        token = create_access_token(identity=user.id)
        res = jsonify()
        set_access_cookies(res, token)
        return res
    else:
        return "Invalid credentials", 401


@auth_api_blueprint.get("/logout")
@jwt_required()
def logout():
    res = jsonify()
    unset_jwt_cookies(res)
    return res


@auth_api_blueprint.get("/user_jwt")
@jwt_required()
def user_jwt():
    current_user = get_jwt_identity()
    user = get_user_by(current_user)
    response = jsonify(user.to_dict())
    return response
