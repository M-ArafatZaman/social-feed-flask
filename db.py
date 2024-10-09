import sqlite3

DATABASE_NAME = "users.db"

def create_table():
    """Create a Users table in the database with name, email, password and date of creation"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()

def insert_user(name, email, password):
    """Insert a new user into the Users table"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Users (name, email, password) VALUES (?, ?, ?)
        """,
        (name, email, password)
    )
    conn.commit()
    conn.close()

def get_all_users():
    """Get all users from the Users table"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT * FROM Users
        """
    )
    users = cursor.fetchall()
    conn.close()
    return users