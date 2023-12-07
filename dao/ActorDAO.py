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

    def insertAll(self, objInsList: list[Actor] = []) -> int:
        pass

    def findOne(self, pattern) -> Actor:
        pass

    def findAll(self) -> list[Actor]:
        '''
        find all actor in database
        '''
        try:
            query = '''SELECT * FROM actor a;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_actor = []
            if len(res) > 0:
                for r in res:
                    actor = Actor()
                    actor.setActorId(r[0])
                    actor.setFirstname(r[1])
                    actor.setLastname(r[2])
                    actor.setGender(r[3])
                    list_actor.append(actor)
                return list_actor
            else:
                return None
        except Exception as error:
            print(f"Error_ActorDOA.findAll() ::: {error}")

    def findOneByOne(self, pattern) -> list[Actor]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Actor]:
        pass

    def updateOne(self, cleAnc, objModif: Actor) -> int:
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
