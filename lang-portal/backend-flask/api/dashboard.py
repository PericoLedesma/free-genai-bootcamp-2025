from flask import Blueprint, jsonify

# Create a Blueprint instance
bp = Blueprint("dashboard", __name__)


# http://127.0.0.1:5000/api/dashboard/
@bp.route('/last_study_session', methods=['GET'])
def last_study_session():
    # Return static data for the most recent study session.
    response_data = {
        "id": 123,
        "group_id": 456,
        "created_at": "2025-02-08T17:20:23-05:00",
        "study_activity_id": 789,
        "group_name": "Basic Greetings"
    }
    return jsonify(response_data)

@bp.route('/study_progress', methods=['GET'])
def study_progress():
    # Return static study progress statistics.
    response_data = {
        "total_words_studied": 3,
        "total_available_words": 124
    }
    return jsonify(response_data)

@bp.route('/quick-stats', methods=['GET'])
def quick_stats():
    # Return static quick overview statistics.
    response_data = {
        "success_rate": 80.0,
        "total_study_sessions": 4,
        "total_active_groups": 3,
        "study_streak_days": 4
    }
    return jsonify(response_data)
