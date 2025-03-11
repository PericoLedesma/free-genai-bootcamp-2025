#!/usr/bin/env python3

# Libraries and modules
import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

from api import words, groups, study_sessions, study_activities, dashboard, reset, main
from api.test_endpoints import run_api_tests
from db.database import *

# Import internal modules
# models/db.py provides the database connection functionality.
# from internal.models import db

# Each service encapsulates business logic.
# from internal.service.dashboard_service import DashboardService
# from internal.service.word_service import WordService
# from internal.service.groups_service import GroupsService
# from internal.service.study_activities_service import StudyActivitiesService
# from internal.service.study_sessions_service import StudySessionsService
# # handlers/__init__.py exports a function to register all HTTP routes.
# from internal.handlers import register_routes
# # middleware/error_handler.py provides a global error handler.
# from internal.middleware.error_handler import error_handler



# Parameters:
HOST = "127.0.0.1"
PORT = 8000

DATABASE_NAME = "test_DB.db"
DATABASE_PATH = os.path.join(".", "db", DATABASE_NAME)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("backend-server")

# ------------ Code ------------ #
def bootstrap_endpoints(app):
    app.register_blueprint(main.bp, url_prefix="/")
    app.register_blueprint(words.bp, url_prefix="/api/words")
    app.register_blueprint(groups.bp, url_prefix="/api/groups")
    app.register_blueprint(study_sessions.bp, url_prefix="/api/study_sessions")
    app.register_blueprint(study_activities.bp, url_prefix="/api/study_activities")
    app.register_blueprint(dashboard.bp, url_prefix="/api/dashboard")
    app.register_blueprint(reset.bp, url_prefix="/api/reset")
    logging.info(" - Endpoints registered successfully.")
    # run_api_tests(f"http://{HOST}:{PORT}")
    # logging.info(app.url_map)


def create_app() -> Flask:
    app = Flask(__name__)  # Create a Flask application instance (app) with the name of the module (__name__)
    log.info(" - Flask app created successfully")
    bootstrap_endpoints(app)  # Register the API endpoints with the Flask  app
    CORS(app)  # Enable CORS for frontend requests

    # app.register_error_handler(Exception, error_handler) # Register a global error handler (to catch exceptions and return JSON errors) todo

    # conn = bootstrap_db(DATABASE_PATH, log)
    # create_tables(conn, log)
    # add_values(conn, log)


    # # Instantiate service objects that encapsulate your business logic.
    # dashboard_service = DashboardService(conn)
    # word_service = WordService(conn)
    # groups_service = GroupsService(conn)
    # study_activities_service = StudyActivitiesService(conn)
    # study_sessions_service = StudySessionsService(conn)
    #
    # # Register HTTP routes/handlers with the Flask app.
    # register_routes(
    #     app,
    #     dashboard_service,
    #     word_service,
    #     groups_service,
    #     study_activities_service,
    #     study_sessions_service
    # )
    #
    return app


if __name__ == "__main__":
    log.info(f"Starting Backend server at https://{HOST}:{PORT} .....")
    app = create_app()
    log.info(" - Server started successfully.")
    app.run(host=HOST, port=PORT)  # ssl_context=('cert.pem', 'key.pem')
