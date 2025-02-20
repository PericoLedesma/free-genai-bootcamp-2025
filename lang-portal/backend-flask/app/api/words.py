from flask import Blueprint, jsonify

# Create a Blueprint instance
bp = Blueprint("words", __name__)

# Define a route inside the Blueprint
@bp.route("/", methods=["GET"])
def get_words():
    return jsonify({"words": ["hello", "world", "flask", "blueprints"]})

@bp.route("/<word>", methods=["GET"])
def get_word_detail(word):
    return jsonify({"message": f"Details about the word: {word}"})