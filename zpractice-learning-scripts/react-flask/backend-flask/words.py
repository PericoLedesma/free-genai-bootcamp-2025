from flask import Blueprint, jsonify

# Create a Blueprint instance
bp = Blueprint("words", __name__)

# Define a route inside the Blueprint
# curl http://127.0.0.1:5000/api/words/
@bp.route("/", methods=["GET"])
def get_words():
    return jsonify({"words": ["hello", "world", "flask", "blueprints"]})

# curl http://127.0.0.1:5000/api/words/python
@bp.route("/<word>", methods=["GET"])
def get_word_detail(word):
    return jsonify({"message": f"Details about the word: {word}"})