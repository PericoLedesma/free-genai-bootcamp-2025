from flask import Flask, jsonify
from flask_cors import CORS
from words import bp  # Importing the Blueprint from words.py

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-react requests

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from backend Flask!"})

# Registering the Blueprint with a URL prefix
app.register_blueprint(bp, url_prefix="/api/words")

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)