from flask import Blueprint, jsonify

# Create a Blueprint instance
bp = Blueprint("words", __name__)


# http://127.0.0.1:5000/api/words/
@bp.route("/", methods=["GET"])
def get_words():
    json = {
        "items": [
            {
                "german": "Hallo",
                "english": "hello",
                "correct_count": 5,
                "wrong_count": 2
            }
        ],
        "pagination": {
            "current_page": 1,
            "total_pages": 5,
            "total_items": 500,
            "items_per_page": 100
        }
    }
    return jsonify(json)


# http://127.0.0.1:5000/api/words/hallo
@bp.route("/<word>", methods=["GET"])
def get_word_detail(word):
    json = {
        "german": word,
        "english": "hello",
        "stats": {
            "correct_count": 5,
            "wrong_count": 2
        },
        "groups": [
            {
                "id": 1,
                "name": "Basic Greetings"
            }
        ]
    }
    return jsonify(json)