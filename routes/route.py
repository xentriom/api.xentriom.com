from flask import Blueprint, jsonify

bp = Blueprint("home", __name__)

@bp.route("/", methods=["GET"])
def do_GET():
  """GET function for the home route."""

  return jsonify({ "message": "Welcome to xentriom's API" }), 200