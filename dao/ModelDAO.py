from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionDB


class ModelDAO(ABC):

    connect_objet = ConnexionDB().getConnexion()

    @abstractmethod
    def insertOne(self, objIns) -> int:
        pass

    @abstractmethod
    def insertAll(self, objInsList: list) -> int:
        pass

    @abstractmethod
    def findOne(self, pattern) -> list:
        pass

    @abstractmethod
    def findAll(self) -> list:
        pass

    @abstractmethod
    def findOneByOne(self, pattern) -> list:
        pass

    @abstractmethod
    def findOneWithLike(self, patternLike) -> list:
        pass

    @abstractmethod
    def updateOne(self, cleAnc, objModif) -> int:
        pass

    @abstractmethod
    def deleteOne(self, cleSup) -> int:
        pass

    # REQUETE SEANCE 4/5:
    # 1- Moyenne des ranks de films dans une année donnée
    # 2- CASE WHEN : Filtre par rank sur les films
    # 3- 
    # 4-

    @abstractmethod
    def createUser(self, pwd, user) -> int:
        pass

    @abstractmethod
    def createRole(self, role) -> int:
        pass

    @abstractmethod
    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    @abstractmethod
    def attributeRole(self, user, role) -> int:
        pass
