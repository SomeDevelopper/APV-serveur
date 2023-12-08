from dao import ModelDAO
from model.DirectorM import Director


class DirectorDAO(ModelDAO.ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Director) -> int:
        pass

    def insertAll(self, objInsList: list[Director] = []) -> int:
        pass

    def findOne(self, pattern) -> Director:
        pass

    def findAll(self) -> list[Director]:
        try:
            query = '''SELECT * FROM director'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            list_director = []

            if len(res) > 0:
                for row in res:
                    director = Director()
                    director.setIdDirector(row[0])
                    director.setDirectorFirstname(row[1])
                    director.setDirectorLastname(row[2])

                    list_director.append(director)
                    print(res)
                return list_director
            else:
                return None
        except Exception as error:
            print(f'Return DirectorDAO.findAll() ::: {error}')
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[Director]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Director]:
        pass

    def updateOne(self, cleAnc, objModif: Director) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPriviliege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
