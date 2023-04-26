from flask import Blueprint, jsonify, request

from api.main.adapter import flask_adapter
from api.main.composer import scraper_composer

api_routes_bp = Blueprint("api_routes", __name__)


@api_routes_bp.route("/api/scraper", methods=["GET"])
async def search():
    """google scraper route"""
    response = flask_adapter(request=request, api_route=scraper_composer())
    if response.status_code < 300:
        return jsonify({"data": response.body}), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
