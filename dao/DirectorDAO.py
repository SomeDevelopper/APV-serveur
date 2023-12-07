from dao.ModelDAO import ModelDAO
from model.DirectorM import Director


class DirectorDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Director) -> int:
        pass

    def insertAll(self, objInsList: list[Director] = []) -> int:
        pass

    def findOne(self, pattern) -> Director:
        pass

    def findAll(self) -> list[Director]:
        pass

    def findOneByOne(self, pattern) -> list[Director]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Director]:
        pass

    def updateOne(self, cleAnc, objModif: Director) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> object:
        pass

    def createRole(self, role) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
