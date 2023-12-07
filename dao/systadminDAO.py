from dao.ModelDAO import ModelDAO


class Systadmin(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet DAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns) -> int:
        pass

    def insertAll(self, objInsList: list) -> int:
        pass

    def findOne(self, pattern) -> object:
        pass

    def findAll(self) -> list:
        pass

    def findOneByOne(self, pattern) -> list:
        pass

    def findOneByOneWithLike(self, patternLike) -> list:
        pass

    def updateOne(self, cleAnc, objModif) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> int:
        '''
        Create new user in DB
        '''
        pass

    def createRole(self, role) -> int:
        '''
        Create new role in DB
        '''
        pass

    def attribuerPriviliege(self, privileges: str, tables: str, role: str) -> int:
        '''
        Attribute Privilège to a role
        '''
        pass

    def attributeRole(self, user, role) -> int:
        '''
        Attribute role to user
        '''
        pass
