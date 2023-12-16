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
        pass

    def insertAll(self, objInsList: list[Role] = []) -> int:
        pass

    def findOne(self, pattern) -> Role:
        pass

    def findAll(self) -> list[Role]:
        def trouverTout(self) -> list[Role]:
        '''
        Récupère tous les enregistrements de la table Role.

        :return: Une liste d'objets Role.
        '''
        try:
            query = '''SELECT * FROM role;'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            liste_b = [] 

            if len(res)>0:

                for r in res:
                    ro = Role()

                    ro.setBrandId(r[0])
                    ro.setBrandName(r[1])

                    liste_b.append(ro)

                return liste_ro

            else:

                return None
        except Exception as e:
            print(f"Erreur_RoleDAO.trouverTout() ::: {e}")
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[Role]:
        pass

    def findOneByOneWithLike(self, patternLike) -> list[Role]:
        pass

    def updateOne(self, cleAnc, objModif: Role) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        def creerRole(self, role) -> int:
        
        try:
            query = f'''CREATE ROLE {role};'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_SysAdminDAO.creerRole() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
