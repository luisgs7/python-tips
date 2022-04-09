from abc import ABC, abstractclassmethod

class database(ABC):

    @abstractclassmethod
    def insert():
        raise Exception("Shoul implement method: insert")

    @abstractclassmethod
    def select():
        raise Exception("Shoul implement method: select")