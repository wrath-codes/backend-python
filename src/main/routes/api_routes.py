from flask import Blueprint, jsonify, request

from src.main.adapter import flask_adapter
from src.main.composer import (
    find_pet_composer,
    find_user_composer,
    register_pet_composer,
    register_user_composer,
)

api_routes_bp = Blueprint("api_routes_bp", __name__, url_prefix="/api")


@api_routes_bp.route("/users", methods=["POST"])
def register_user():
    """register user route"""

    message = {}
    response = flask_adapter(
        request=request,
        api_route=register_user_composer(),
    )

    if response.status_code < 300:
        message = {
            "Type": "users",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
            },
        }

        return jsonify(
            {
                "data": message,
            },
            response.status_code,
        )

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/pets", methods=["POST"])
def register_pet():
    """register pet route"""

    message = {}
    response = flask_adapter(
        request=request,
        api_route=register_pet_composer(),
    )

    if response.status_code < 300:
        message = {
            "type": "pets",
            "id": response.body.id,
            "attributes": {
                "name": response.body.name,
                "species": response.body.specie,
                "age": response.body.age,
            },
            "relationships": {
                "owner": {
                    "type": "users",
                    "id": response.body.id_user,
                }
            },
        }

        return jsonify(
            {
                "data": message,
            },
            response.status_code,
        )

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/pets", methods=["GET"])
def find_pets():
    """register pet route"""

    response = flask_adapter(request=request, api_route=find_pet_composer())

    message = []

    if response.status_code < 300:
        # if not error, format the message and return it

        for pet in response.body:
            message.append(
                {
                    "type": "pets",
                    "id": pet.id,
                    "attributes": {
                        "name": pet.name,
                        "specie": pet.specie.value,
                        "age": pet.age,
                    },
                    "relationships": {
                        "owner": {
                            "type": "users",
                            "id": pet.id_user,
                        }
                    },
                }
            )

        return jsonify(
            {
                "data": message,
            },
            response.status_code,
        )

    # Handling Errors
    return (
        jsonify(
            {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"],
                }
            }
        ),
        response.status_code,
    )


@api_routes_bp.route("/users", methods=["GET"])
def find_users():
    """find users route"""

    message = {}
    response = flask_adapter(request=request, api_route=find_user_composer())

    if response.status_code < 300:
        message = []

        for element in response.body:
            message.append(
                {
                    "type": "users",
                    "id": element.id,
                    "attributes": {"name": element.name},
                }
            )

        return jsonify({"data": message}), response.status_code

    # Handling Errors
    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
