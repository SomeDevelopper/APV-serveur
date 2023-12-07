from dao.ModelDAO import ModelDAO
from model.MovieGenreM import MovieGenre


class MovieGenre(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieGenre) -> int:
        pass

    def insertAll(self, objInsList: list[MovieGenre] = []) -> int:
        pass

    def findOne(self, pattern) -> MovieGenre:
        pass

    def findAll(self) -> list[MovieGenre]:
        pass

    def findOneByOne(self, pattern) -> list[MovieGenre]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[MovieGenre]:
        pass

    def updateOne(self, cleAnc, objModif: MovieGenre) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> object:
        pass

    def createRole(self, role) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
