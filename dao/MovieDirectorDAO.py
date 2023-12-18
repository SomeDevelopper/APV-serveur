from dao.ModelDAO import ModelDAO
from model.MovieDirectorM import MovieDirector


class MovieDirectorDirectorDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieDirector) -> int:
        pass

    def insertAll(self, objInsList: list[MovieDirector] = []) -> int:
        pass

    def findOne(self, pattern) -> MovieDirector:
        pass

    def findAll(self) -> list[MovieDirector]:
        pass

    def findOneByOne(self, pattern) -> list[MovieDirector]:
        pass

    def findOneWithLike(self, patternLike) -> list[MovieDirector]:
        pass

    def updateOne(self, cleAnc, objModif: MovieDirector) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
