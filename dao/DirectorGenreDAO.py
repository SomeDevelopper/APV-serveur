from dao.ModelDAO import ModelDAO
from model.DirectorGenreM import DirectorGenre


class DirectorGenreDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: DirectorGenre) -> int:
        pass

    def insertAll(self, objInsList: list[DirectorGenre] = []) -> int:
        pass

    def findOne(self, pattern) -> DirectorGenre:
        pass

    def findAll(self) -> list[DirectorGenre]:
        pass

    def findOneByOne(self, pattern) -> list[DirectorGenre]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[DirectorGenre]:
        pass

    def updateOne(self, cleAnc, objModif: DirectorGenre) -> int:
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
