from .config import create_db_pool
from asyncpg import Pool
from functools import wraps

db_pool = None


async def get_db_pool() -> Pool:
    """
    Get the database pool. If the pool does not exist, create it.

    :return: The database pool.
    """

    global db_pool
    if db_pool is None:
        db_pool = await create_db_pool()
    return db_pool


def db_connection(func):
    """
    Decorator that provides a database connection to a function.

    :param func: The function to be decorated.
    :return: The decorated function.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with (await get_db_pool()).acquire() as connection:
            return await func(*args, **kwargs, connection=connection)
    return wrapper

