from flask import Blueprint, jsonify, request

bp = Blueprint("reset", __name__)

@bp.route("/full_reset", methods=["POST"])
def full_reset():
    # Implement logic to perform a full system reset here.
    response_data = {
        "success": True,
        "message": "System has been fully reset"
    }
    return jsonify(response_data)

@bp.route("/reset_history", methods=["POST"])
def reset_history():
    # Here you could add logic to reset study history.
    response_data = {
        "success": True,
        "message": "Study history has been reset"
    }
    return jsonify(response_data)