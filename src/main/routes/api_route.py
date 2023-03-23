from flask import Blueprint, jsonify

api_routes_bp = Blueprint("api_routes_bp", __name__)


@api_routes_bp.route("/api", methods=["GET"])
def something():
    """Test"""

    return jsonify(
        {
            "Programador": "WrathCodes",
        }
    )
