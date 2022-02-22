import sqlite3
from models import Actor


class ActorManager:
    def __init__(self):
        self._connection = sqlite3.connect(
            '/media/disk_d/MA/django-orm/py-cinema-hall-manager/cinema_db.sqlite'
        )
        self.table_name = "actors"

    def all(self):
        actors_cursor = self._connection.execute(f"SELECT * FROM {self.table_name}")
        return [Actor(*row) for row in actors_cursor]

    def create(self, first_name, last_name):
        self._connection.execute(
            f"INSERT INTO {self.table_name} (first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._connection.commit()

    def update(self, id_to_update, first_name, last_name):
        self._connection.execute(
            f"UPDATE {self.table_name} SET "
            "first_name = ?,"
            "last_name = ?"
            "WHERE id = ?",
            (first_name, last_name, id_to_update, )
        )
        self._connection.commit()

    def delete(self, id_to_delete):
        self._connection.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (id_to_delete, )
        )
        self._connection.commit()