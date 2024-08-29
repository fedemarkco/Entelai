from http import HTTPStatus

from flask import Blueprint, jsonify, request

from ..views.node_view import first_option, search_option

bp = Blueprint("api", __name__)


@bp.route("/start", methods=["POST"])
def start():
    first_node = first_option()

    return jsonify(first_node), HTTPStatus.OK


@bp.route("/choose", methods=["POST"])
def choose():
    data = request.json
    options = search_option(data)

    return jsonify(options), HTTPStatus.OK
