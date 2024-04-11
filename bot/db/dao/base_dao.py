from asyncpg import Connection, Record


class BaseDAO:
    """
    Base class for all DAOs. It provides a connection to the
    database and methods to fetch and execute queries.
    """

    def __init__(self, connection: Connection):
        """
        Initializes the DAO with a connection to the database.

        :param connection: An asyncpg connection to the database.
        """

        self.connection = connection

    async def fetch(self, query, *args) -> list[Record]:
        """
        Fetches data from the database.

        It sends a SQL query to the database and returns the result.

        :param query: A string containing a SQL query to be executed.
        :param args: Additional arguments to be passed to the query. These should be parameters to be used in the query.
        :return: A list of records fetched from the database.
        """

        return await self.connection.fetch(query, *args)

    async def execute(self, query, *args) -> str:
        """
        Executes a command in the database.

        It sends a SQL command to the database and does not return any result.

        :param query: A string containing a SQL command to be executed.
        :param args: Additional arguments to be passed to the command. These should be parameters to be used in the
        command.
        :return: The status of the executed command. It does not return any fetched records.
        """

        return await self.connection.execute(query, *args)

    async def fetchval(self, query, *args) -> Record | None:
        """
        Fetches a single value from the database.

        It sends a SQL query to the database and returns a single value.

        :param query: A string containing a SQL query to be executed.
        :param args: Additional arguments to be passed to the query. These should be parameters to be used in the query.
        :return: A single value fetched from the database.
        """

        return await self.connection.fetchval(query, *args)
