import sqlite3


class ConnectorToDB:
    """Класс для работы с БД"""
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)

    def get(self, query_fields: list, query_params: dict, limit_value: int = 1):
        with self.connection.cursor() as cursor:
            fields = '*'
            if query_fields:
                fields = query_fields
            return cursor.execute(f"SELECT {fields} FROM exlab WHERE query_params.keys() = ? LIMIT ?", (query_params.values(), limit_value))

