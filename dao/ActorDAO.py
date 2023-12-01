from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionDB


class ActorDAO(ABC):
    conn_obj = ConnexionDB().getConnexion()

    @abstractmethod
    def insertOne(self, obj) -> int:
        pass

    @abstractmethod
    def insertMany(self, objList) -> int:
        pass

    @abstractmethod
    def findOne(self, pattern) -> object:
        pass

    @abstractmethod
    def findAll(self) -> list:
        pass

    @abstractmethod
    def findOneByOne(self, patter) -> list:
        pass
