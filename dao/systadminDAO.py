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

    def findOneWithLike(self, patternLike) -> list:
        pass

    def updateOne(self, cleAnc, objModif) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def getAverageRankForYear(self, year) -> list:
        pass

    def getCaseRank(self) -> list:
        pass
    
    def getNtileData(self) -> list:
        pass

    def getSubStr(self) -> list:
        pass
    
    def createUser(self, pwd: str, user: str) -> int:
        print('DAO', self)

        try:
            query = f'''CREATE USER {user} WITH PASSWORD {pwd};'''
            self.cur.execute(query)
            self.cur.connection.commit()
            print(self.cur.rowcount)
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_systadminDAO.createUser ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def createRole(self, role) -> int:
        try:
            query = f'''CREATE ROLE {role}'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_systadminDAO.createRole ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def attribuerPriviliege(self, privileges: str, tables: str, role: str) -> int:
        try:
            query = f'''GRANT {privileges} ON {tables} TO {role}'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(
                f'''Error_systadminDAO.attribuerPriviliege ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def attributeRole(self, user, role) -> int:
        try:
            query = f'''GRANT {role} TO {user}'''
            self.cur.execute(query)
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_systadminDAO.attributeRole ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()
