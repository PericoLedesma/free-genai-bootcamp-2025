# The entry point of the application.
# This file contains the main function that starts the Flask server.

# main.py
from flask import Flask, render_template_string
from api import words, groups, study_sessions, study_activities, dashboard, reset

app = Flask(__name__)

app.register_blueprint(words.bp, url_prefix="/api/words")
app.register_blueprint(groups.bp, url_prefix="/api/groups")
app.register_blueprint(study_sessions.bp, url_prefix="/api/study_sessions")
app.register_blueprint(study_activities.bp, url_prefix="/api/study_activities")
app.register_blueprint(dashboard.bp, url_prefix="/api/dashboard")
app.register_blueprint(reset.bp, url_prefix="/api/reset")



 # ------------------------------------------------------------------- #
@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask Backend</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background: #f4f4f4; margin: 50px; }
            .container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); display: inline-block; }
            h1 { color: #333; } p { color: #666; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask Backend Running</h1>
            <p>Backend is up and running!</p>     
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)