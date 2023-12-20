from dao.ModelDAO import ModelDAO
from model.RoleM import Role


class RoleDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Role) -> int:
        try:
            query = '''INSERT INTO Role (idActor, role) 
                       VALUES (%s, %s);'''
            self.cur.execute(query, (objIns.getidActor(), objIns.getRole()))
            self.cur.connection.commit() 
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_BrandsDAO.insererUn() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[Role] = []) -> int:
        pass

    def findOne(self, pattern) -> Role:
        pass

    def findAll(self) -> list[Role]:
        def trouverTout(self) -> list[Role]:
            
        try:
            query = '''SELECT * FROM role;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] 

            if len(res)>0:

                for r in res:
                    ro = Role()

                    ro.setidActor(r[0])
                    ro.setid(r[1])

                    liste_b.append(ro)

                return liste_ro

            else:

                return None
        except Exception as e:
            print(f"Error_RoleDAO.FindAll() ::: {e}")
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[Role]:
        pass

    def findOneWithLike(self, patternLike) -> list[Role]:
        pass

    def updateOne(self, cleAnc, objModif: Role) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM Role WHERE Role = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_RoleDAO.deleteOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()


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
