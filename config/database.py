from decouple import config, UndefinedValueError

class DatabaseConfig :
    """Database configuration management"""

    def __init__(self):
        try:
            self.host = config('DB_HOST')
            self.port = config('DB_PORT', cast=int)
            self.database = config('DB_NAME')
            self.user = config('DB_USER')
            self.password = config('DB_PASSWORD')
        except UndefinedValueError as e:
            print(f"The .env file is not set correctly, configuration error: {e}")
            print("Create an .env file and include your database informations")

    def get_connection_params(self) -> dict:
        """Needed to connect to PostgreSQL via psycopg2 library"""
        return {
            'host': self.host,
            'port': self.port,
            'database': self.database,
            'user': self.user,
            'password': self.password,
        }