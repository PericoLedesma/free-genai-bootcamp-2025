from flask import Flask, jsonify
from flask_cors import CORS
from words import bp  # Importing the Blueprint from words.py
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-react requests
print("Flask app created successfully on : ", app.url_map)
database_path = "SQlite/test_DB.db"

def get_db_connection():
    conn = sqlite3.connect(database_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/api/database", methods=["GET"])
def get_words():
    conn = get_db_connection()
    print("Connection established: ", conn)
    cursor = conn.cursor()


    # Query to get all table names
    print("Fetching table names...")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print("Tables: ", tables)

    print("Fetching all rows from test_DB table...")
    cursor.execute("SELECT * FROM test_DB")
    words = cursor.fetchall()
    conn.close()

    words_list = [dict(word) for word in words]
    return jsonify({"words": words_list})


@app.route('/api/message', methods=['GET'])
def get_message():
    print("Sending message: Hello from backend Flask!")
    return jsonify({"message": "api/message: Hello from backend Flask!"})

# Registering the Blueprint with a URL prefix
app.register_blueprint(bp, url_prefix="/api/words")

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
