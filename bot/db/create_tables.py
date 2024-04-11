from asyncpg import Connection

from db.pool import db_connection


@db_connection
async def create_user_table(connection: Connection) -> None:
    """
    Create the user table.

    This function creates the user table in the database if it does not exist.

    :return: None
    """

    await connection.execute("""
    CREATE TABLE IF NOT EXISTS tg_users (
        id SERIAL PRIMARY KEY,
        tg_id BIGINT NOT NULL,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255),
        username VARCHAR(255),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)


async def init_database() -> None:
    """
    Initialize the database.

    This function initializes the database by creating the required tables.

    :return: None
    """

    await create_user_table()
