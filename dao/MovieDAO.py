from dao.ModelDAO import ModelDAO
from model.MovieM import Movie


class MovieDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Movie) -> int:
        pass

    def insertAll(self, objInsList: list[Movie] = []) -> int:
        pass

    def findOne(self, pattern) -> Movie:
        pass

    def findAll(self) -> list[Movie]:
        pass

    def findOneByOne(self, pattern) -> list[Movie]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Movie]:
        pass

    def updateOne(self, cleAnc, objModif: Movie) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> object:
        pass

    def createRole(self, role) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
