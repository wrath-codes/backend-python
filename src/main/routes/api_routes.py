from flask import Blueprint, jsonify, request

from src.main.adapter import flask_adapter
from src.main.composer import register_user_composer

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
