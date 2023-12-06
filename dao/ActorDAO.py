from dao.ModelDAO import ModelDAO
from model.ActorM import Actor


class ActorDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Actor) -> int:
        pass

    def insertAll(self, objInsList:list[Actor]=[]) -> int:
        pass

    def findOne(self, pattern) -> Actor:
        pass

    def findAll(self) -> list[Actor]:
        pass

    def findOneByOne(self, pattern) -> list[Actor]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Actor]:
        pass

    def updateOne(self, cleAnc, objModif: Actor) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> object:
        pass

    def createRole(self, role) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
