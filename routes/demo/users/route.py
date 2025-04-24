from flask import Blueprint, jsonify
from pathlib import Path
import json

bp = Blueprint("demo_users", __name__, url_prefix="/demo/users")

@bp.route("/", methods=["GET"])
def do_GET():
  """GET function for the demo users route."""

  # Navigate up 3 levels from routes/demo/users/route.py → project root
  data_path = Path(__file__).resolve().parents[3] / "data" / "users.json"

  try:
    with open(data_path) as f:
      data = json.load(f)
    return jsonify(data), 200
  except FileNotFoundError:
    return jsonify({"error": "File not found"}), 404
  except json.JSONDecodeError:
    return jsonify({"error": "Invalid JSON format"}), 500