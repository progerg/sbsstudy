import sqlite3
from sqlite3 import Connection


def connect_to_db(db_name: str) -> Connection:
    """
    Connect to a SQLite database. If the database does not exist, it will be created.

    Args:
        db_name (str): The name of the database file.

    Returns:
        Connection object: The Connection object for the database.
    """
    return sqlite3.connect(db_name)
