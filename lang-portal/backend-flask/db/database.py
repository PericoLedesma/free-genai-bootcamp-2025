# database.py

# Libraries and modules
import os
import sqlite3




def bootstrap_db(DATABASE_PATH, log) -> sqlite3.Connection:
    # Initialize the SQLite database connection.
    log.info(" - Connecting to database...")
    db_dir = os.path.dirname(DATABASE_PATH)
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
        log.info("Created database directory: %s", db_dir)

    # Database initialization function
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        log.info("Connected to database: %s", DATABASE_PATH)
        return conn
    except sqlite3.Error as e:
        log.error("Failed to connect to database: %s", e)
        raise


def create_tables(conn, log):
    """Create database tables if they don't exist."""
    log.info(" - Creating tables...")
    cursor = conn.cursor()

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS test_DB (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        german TEXT NOT NULL,
                        english TEXT NOT NULL,
                        correct_count INTEGER DEFAULT 0,
                        wrong_count INTEGER DEFAULT 0
                        )
                    """)

    conn.commit() # Ensures all changes are written to the database file.


def add_values(conn, log):
    log.info(" - Adding values to tables...")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO test_DB (german, english) VALUES (?, ?)", ("Hallo", "Hello"))
    cursor.execute("INSERT INTO test_DB (german, english) VALUES (?, ?)", ("Welt", "World"))

    conn.commit()