from asyncpg import Connection, Record

from db.dao.user_dao import UserDAO
from db.pool import db_connection


class UserService:
    """
    User Service class.

    This class provides methods to interact with the User Data Access Object (DAO) to fetch and manipulate user data.
    """

    @db_connection
    async def get_user(self, user_id: int, connection: Connection) -> Record:
        """
        Get user by id.

        It uses the UserDAO to fetch a user record by its id from the database.

        :param user_id: The id of the user to be fetched.
        :param connection: The database connection object (from decorator).
        :return: A dictionary representing the fetched user record. If no record is found, it returns None.
        """

        user_dao = UserDAO(connection)
        return await user_dao.get_user_by_id(user_id)

    @db_connection
    async def get_users_count(self, connection: Connection) -> int:
        """
        Get the total number of users.

        It uses the UserDAO to fetch the total number of user records from the database.

        :param connection: The database connection object (from decorator).
        :return: A representing the total number of user records.
        """

        user_dao = UserDAO(connection)
        return await user_dao.get_all_users_count()

    @db_connection
    async def create_user(self, tg_id: int, first_name: str, last_name: str, username: str, connection: Connection) -> str:
        """
        Create a new user.

        It uses the UserDAO to create a new user record in the database.

        :param tg_id: The id of the new user from telegram.
        :param first_name: The first name of the new user from telegram.
        :param last_name: The last name of the new user from telegram.
        :param username: The username of the new user from telegram.
        :param connection: The database connection object (from decorator).
        :return: The status of the executed command. It does not return any fetched records.
        """

        user_dao = UserDAO(connection)
        return await user_dao.create_user(tg_id, first_name, last_name, username)
