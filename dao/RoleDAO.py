from dao.ModelDAO import ModelDAO
from model.RoleM import Role


class RoleDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet RoleDAO en établissant une connexion à la base de données.
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
        try:
            query = '''INSERT INTO role (id_movie, id_actor, role) 
                           VALUES (%s, %s, %s);'''
            self.cur.executemany(query, [(obj.getMovieId(), obj.getActorId(), obj.getRole()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_RoleDAO.insertAll ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, pattern) -> Role:
        try:
            query = '''SELECT * FROM role  WHERE id_movie = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchone()
            if res:
                r = Role()
                r.setActorId(res[0])
                r.setFirstname(res[1])
                r.setLastname(res[2])
                return r
            else:
                return None
        except Exception as exception:
            print(f'''Error_RoleDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findAll(self) -> list[Role]:
        try:
            query = '''SELECT * FROM role r;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_role = []
            if len(res) > 0:
                for r in res:
                    role = Role()
                    role.setActorId(r[0])
                    role.setFirstname(r[1])
                    role.setLastname(r[2])
                    list_role.append(role)
                return list_role
            else:
                return None
        except Exception as exception:
            print(f"Error_RoleDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[Role]:
        try:
            query = '''SELECT * FROM role WHERE role = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchall()

            list_role = []

            if len(res) > 0:
                for r in res:
                    role = Role()
                    role.setActorId(r[0])
                    role.setFirstname(r[1])
                    role.setLastname(r[2])
                    list_role.append(role)

                return list_role
            else:
                return None
        except Exception as e:
            print(f"Erreur_RoleDAO.findOneByOne ::: {e}")
        finally:
            self.cur.close()

    def findOneWithLike(self, patternLike) -> list[Role]:
        try:
            query = '''SELECT * FROM role WHERE role LIKE %s'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()
            list_role = []
            if len(res) > 0:
                for r in res:
                    role = Role()
                    role.setActorId(r[0])
                    role.setFirstname(r[1])
                    role.setLastname(r[2])
                    list_role.append(role)
                return list_role
            else:
                return None
        except Exception as e:
            print(f"Erreur_RoleDAO.findOneWithLike ::: {e}")
            return None
        finally:
            self.cur.close()

    def updateOne(self, cleAnc, objModif: Role) -> int:
        try:
            query = '''UPDATE role SET id_actor = %s, role = %s
                           WHERE id_actor = %s;'''
            self.cur.execute(query, (objModif.getActorId(), objModif.getRole(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_RoleDAO.updateOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM role WHERE id_movie = %s;'''
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

    def getCaseRank(self) -> list:
        pass
    
    def getNtileData(self) -> list:
        pass

    def getSubStr(self, start, nb_letter) -> list:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
