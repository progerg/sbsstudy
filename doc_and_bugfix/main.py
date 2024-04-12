from database import connect_to_db
from config import DB_PATH
from models import create_table, insert_user


def main():
    """
    Main function of the program.

    This function connects to the database, creates a table, and inserts a user into the table.
    The database connection is managed using a context manager, which automatically closes the connection when done.

    The user 'Alice' with age 30 is inserted into the table as an example.
    Modify this function to insert different users or to perform different database operations.
    """

    with connect_to_db(DB_PATH) as conn:
        create_table(conn)
        insert_user(conn, 'Alice', 30)


if __name__ == "__main__":
    main()
