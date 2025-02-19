from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-react requests

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({"message": "Hello from backend Flask!"})

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)