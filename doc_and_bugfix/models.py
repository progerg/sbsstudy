from sqlite3 import Connection
from contextlib import closing


def create_table(conn: Connection):
    """
    Create a new table in the SQLite database if it does not already exist.

    Args:
        conn: The Connection object for the database.
    """
    with closing(conn.cursor()) as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)
        conn.commit()


def insert_user(conn: Connection, user_name: str, user_age: int):
    """
    Insert a new user into the users table.

    Args:
        conn: The Connection object for the database.
        user_name: The name of the user.
        user_age: The age of the user.
    """
    with closing(conn.cursor()) as cursor:
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (user_name, user_age))
        conn.commit()
