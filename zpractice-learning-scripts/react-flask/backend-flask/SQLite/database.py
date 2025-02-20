'''


'''


import sqlite3

DATABASE_NAME = "test_DB.db"

def get_db_connection():
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing results like dictionaries
    return conn

def create_tables():
    """Create database tables if they don't exist."""
    conn = get_db_connection()
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
    conn.close()

def add_values():
    conn = sqlite3.connect("test_DB.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO test_DB (german, english) VALUES (?, ?)", ("Hallo", "Hello"))
    cursor.execute("INSERT INTO test_DB (german, english) VALUES (?, ?)", ("Welt", "World"))

    conn.commit()
    conn.close()



if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully.")
    add_values()
    print("Values added to the database")
