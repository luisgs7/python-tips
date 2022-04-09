from typing import Type
from interfaces.database import database

class MyUseCase:

    def __init__(self, database: Type[database]) -> None:
        self.database = database

    def search_something(self):
        self.database.select()

    def insert_something(self):
        self.database.insert()

