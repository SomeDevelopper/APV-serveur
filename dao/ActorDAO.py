from dao.ModelDAO import ModelDAO
from model.ActorM import Actor


class ActorDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Actor) -> int:
        pass

    def insertAll(self, objInsList: list[Actor] = []) -> int:
        pass

    def findOne(self, idActor) -> Actor:
        '''
            find one actor by id in database
        '''
        try:
            query = '''SELECT * FROM actor WHERE id_actor = %s;'''
            self.cur.execute(query, (idActor,))
            res = self.cur.fetchone()
            if res:
                actor = Actor()
                actor.setActorId(res[0])
                actor.setFirstname(res[1])
                actor.setLastname(res[2])
                return actor
            else:
                return None
        except Exception as exception:
            print(f'''Error_ActorDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

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
                for a in res:
                    actor = Actor()
                    actor.setActorId(a[0])
                    actor.setFirstname(a[1])
                    actor.setLastname(a[2])
                    list_actor.append(actor)
                return list_actor
            else:
                return None
        except Exception as exception:
            print(f"Error_ActorDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()


    def findOneByOne(self, pattern) -> list[Actor]:
        pass

    def findOneWithLike(self, patternLike) -> list[Actor]:
        try:
            query = '''SELECT * FROM actor WHERE firstname LIKE %s'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()
            list_actor = []
            if len(res) > 0:
                for a in res:
                    actor = Actor()
                    actor.setActorId(a[0])
                    actor.setFirstname(a[1])
                    actor.setLastname(a[2])
                    list_actor.append(actor)
                print('DAO', list_actor)
                return list_actor
            else:
                return None
        except Exception as exception:
            print(f'''Error_ActorDAO.findOneWithLike ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def updateOne(self, cleAnc, objModif: Actor) -> int:
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
