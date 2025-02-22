
from flask import Blueprint, render_template_string

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET"])
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