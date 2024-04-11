from asyncpg import Record

from .base_dao import BaseDAO


class UserDAO(BaseDAO):
    """
    User Data Access Object (DAO) class.

    This class inherits from the BaseDAO class and provides methods to interact with the user data in the database.
    """

    async def get_user_by_id(self, telegram_id: int) -> Record | None:
        """
        Get user by telegram id.

        It sends a SQL query to the database to fetch a user record by its telegram id.

        :param telegram_id: The telegram id of the user to be fetched.
        :return: A dictionary representing the fetched user record. If no record is found, it returns None.
        """

        query = "SELECT * FROM tg_users WHERE telegram_id = $1"
        return await self.fetchval(query, telegram_id)

    async def create_user(self, tg_id: int, first_name: str, last_name: str, username: str) -> str:
        """
        Create a new user.

        It sends a SQL command to the database to create a new user record.

        :param tg_id: The id of the new user from telegram.
        :param first_name: The first name of the new user from telegram.
        :param last_name: The last name of the new user from telegram.
        :param username: The username of the new user from telegram.
        :return: The status of the executed command. It does not return any fetched records.
        """

        query = "INSERT INTO tg_users (tg_id, first_name, last_name, username) VALUES ($1, $2, $3, $4)"
        return await self.execute(query, tg_id, first_name, last_name, username)

    async def get_all_users_count(self) -> int:
        """
        Get the total number of users.

        It sends a SQL query to the database to fetch the total number of user records.

        :return: A representing the total number of user records.
        """

        query = "SELECT COUNT(*) FROM tg_users"
        result = await self.fetchval(query)
        return result.get("count")
