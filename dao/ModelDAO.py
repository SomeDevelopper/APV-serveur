from abc import ABC, abstractmethod
from dao.ConnexionDAO import ConnexionBD


class ModelDAO(ABC):

    connect_objet = ConnexionBD().getConnexion()

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
    def findOneByOneWithLike(self, patternLike) -> list:
        pass

    @abstractmethod
    def updateOne(self, cleAnc, objModif) -> int:
        pass

    @abstractmethod
    def deleteOne(self, cleSup) -> int:
        pass

    # REQUETE SEANCE 4/5:
    # 1- Moyenne des ranks de films dans une année donnée
    # 2- CASE WHEN : Filtre par rank
    # 3-
    # 4-

    @abstractmethod
    def createUser(self, pwd, user) -> object:
        pass

    @abstractmethod
    def createRole(self, role) -> int:
        pass

    @abstractmethod
    def attributeRole(self, user, role) -> int:
        pass
