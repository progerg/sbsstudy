from os import getenv
from asyncpg import create_pool, Pool

# The URL of the database, fetched from the environment variables.
DATABASE_URL = getenv("DATABASE_URL")


async def create_db_pool() -> Pool:
    """
    Creates a connection pool to the database.

    It uses the DATABASE_URL to establish a connection pool to the database.

    :return: An instance of asyncpg.Pool, which can be used to manage database connections.
    """

    return await create_pool(DATABASE_URL)
