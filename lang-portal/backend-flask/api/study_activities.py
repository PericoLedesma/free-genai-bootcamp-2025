from flask import Blueprint, jsonify, request

bp = Blueprint("study_activities", __name__)

@bp.route('/<int:id>', methods=['GET'])
def get_study_activity(id):
    # Return static data for a study activity.
    response_data = {
        "id": 1,
        "name": "Vocabulary Quiz",
        "thumbnail_url": "https://example.com/thumbnail.jpg",
        "description": "Practice your vocabulary with flashcards"
    }
    return jsonify(response_data)

@bp.route('/<int:id>/study_sessions', methods=['GET'])
def get_study_activity_study_sessions(id):
    # Return static study sessions data with pagination.
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
            "items_per_page": 20
        }
    }
    return jsonify(response_data)

@bp.route('', methods=['POST'])
def create_study_activity():
    # Extract request parameters (e.g., group_id and study_activity_id)
    data = request.get_json()
    # Process data here as needed, e.g., save to the database.
    # For now, we return a static response.
    response_data = {
        "id": 124,
        "group_id": 123
    }
    return jsonify(response_data)