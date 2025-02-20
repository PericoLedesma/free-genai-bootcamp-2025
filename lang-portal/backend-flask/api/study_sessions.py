from flask import Blueprint, jsonify, request

bp = Blueprint("study_sessions", __name__)

@bp.route("/", methods=["GET"])
def get_study_sessions():
    # Returns a paginated list of study sessions.
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
            "total_pages": 5,
            "total_items": 100,
            "items_per_page": 100
        }
    }
    return jsonify(response_data)

@bp.route("/<int:id>", methods=["GET"])
def get_study_session(id):
    # Returns details for a specific study session.
    response_data = {
        "id": 123,
        "activity_name": "Vocabulary Quiz",
        "group_name": "Basic Greetings",
        "start_time": "2025-02-08T17:20:23-05:00",
        "end_time": "2025-02-08T17:30:23-05:00",
        "review_items_count": 20
    }
    return jsonify(response_data)

@bp.route("/<int:id>/words", methods=["GET"])
def get_study_session_words(id):
    # Returns a paginated list of words associated with a specific study session.
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



@bp.route("/<int:id>/words/<int:word_id>/review", methods=["POST"])
def review_word(id, word_id):
    # Extract the 'correct' field from the JSON payload
    data = request.get_json()
    correct = data.get("correct", False)

    # Return a static JSON response simulating a review record creation
    response_data = {
        "success": True,
        "word_id": word_id,
        "study_session_id": id,
        "correct": correct,
        "created_at": "2025-02-08T17:33:07-05:00"
    }
    return jsonify(response_data)