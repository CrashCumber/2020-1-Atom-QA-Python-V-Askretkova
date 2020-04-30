import pymysql


class LoggerConnection:

    def __init__(self):
        self.user = 'root'
        self.password = ''
        self.db_name = 'LOGS'

        self.host = '127.0.0.1'
        self.port = 3306

        self.connection = self.connect()

    def get_connection(self, db_created=False):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if db_created else None,
            charset='utf8',
            autocommit=True,
        )

    def connect(self):
        connection = self.get_connection()
        connection.query(f'DROP DATABASE if exists {self.db_name}')
        connection.query(f'CREATE DATABASE {self.db_name}')
        connection.close()

        return self.get_connection(db_created=True)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
