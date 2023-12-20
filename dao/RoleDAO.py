from dao.ModelDAO import ModelDAO
from model.RoleM import Role


class RoleDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Role) -> int:
        try:
            query = '''INSERT INTO role (id_movie, id_actor, role)
                        VALUES (%s, %s, %s)'''
            self.cur.execute(
                query, (objIns.getMovieId(), objIns.getActorId(), objIns.getRole(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_RoleDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[Role] = []) -> int:
        pass

    def findOne(self, pattern) -> Role:
        pass

    def findAll(self) -> list[Role]:
        pass

    def findOneByOne(self, pattern) -> list[Role]:
        pass

    def findOneWithLike(self, patternLike) -> list[Role]:
        pass

    def updateOne(self, cleAnc, objModif: Role) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def getAverageRankForYear(self, year) -> list:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
