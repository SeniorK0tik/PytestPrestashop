from typing import Optional

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

from configuration.ui import get_ui_config
from utils.logger_loguru.logger import logger


class PrestaMySQL:
    def __init__(self, connection: Connection):
        self._connection = connection

    @property
    def connection(self) -> Connection:
        return self._connection

    def create_cursor(self) -> Cursor:
        return self._connection.cursor()

    def execute_command(self, *args, command: str = 'execute') -> None:
        with self._connection.cursor() as cursor:
            if command == 'execute':
                cursor.execute(*args)
            else:
                raise TypeError('No such command: %s' % command)
            self.connection.commit()

    def delete_email_subscriber(self, email: str) -> None:
        self.execute_command("DELETE FROM ps_emailsubscription WHERE email = %s", (email,))
        logger.info('User FROM table ps_emailsubscription was DELETED with email: {}'.format(email))

    def delete_user(self, email) -> None:
        self.execute_command("DELETE FROM ps_customer WHERE email = %s", (email,))
        logger.info('User FROM table ps_custumer was DELETED with email: {}'.format(email))


def connect_db(
        host: str,
        port: int,
        user: str,
        password: Optional[str],
        database: str,
) -> Connection:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


if __name__ == '__main__':
    conf = get_ui_config()
    connection = connect_db(
        host=conf.db.host,
        port=conf.db.port,
        user=conf.db.user,
        password=conf.db.password,
        database=conf.db.db_name
    )
    t = PrestaMySQL(connection)
