from flask import Blueprint, jsonify, request

bp = Blueprint("groups", __name__)

@bp.route("/", methods=["GET"])
def get_groups():
    response_data = {
        "items": [
            {
                "id": 1,
                "name": "Basic Greetings",
                "word_count": 20
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 1,
            "total_items": 10,
            "items_per_page": 100
        }
    }
    return jsonify(response_data)

@bp.route("/<int:id>", methods=["GET"])
def get_group(id):
    response_data = {
        "id": 1,
        "name": "Basic Greetings",
        "stats": {
            "total_word_count": 20
        }
    }
    return jsonify(response_data)

@bp.route("/<int:id>/words", methods=["GET"])
def get_group_words(id):
    response_data = {
        "items": [
            {
                "german": "hallo",
                "english": "hello",
                "correct_count": 5,
                "wrong_count": 2
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 1,
            "total_items": 20,
            "items_per_page": 100
        }
    }
    return jsonify(response_data)

@bp.route("/<int:id>/study_sessions", methods=["GET"])
def get_group_study_sessions(id):
    response_data = {
        "items": [
            {
                "id": 123,
                "activity_name": "Vocabulary Quiz",
                "group_name": "Basic Greetings",
                "start_time": "2025-02-08T17:20:23-05:00",
                "end_time": "2025-02-08T17:30:23-05:00",
                "review_items_count": 20
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 1,
            "total_items": 5,
            "items_per_page": 100
        }
    }
    return jsonify(response_data)