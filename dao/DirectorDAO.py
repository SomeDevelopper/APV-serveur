from dao import ModelDAO
from model.DirectorM import Director


class DirectorDAO(ModelDAO.ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet DirectorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Director) -> int:
        try:
            query = '''INSERT INTO director (id_director, firstname, lastname)
                        VALUES (%s, %s, %s)'''
            self.cur.execute(
                query, (objIns.getid_director(), objIns.getDirectorFirstname(), objIns.getDirectorLastname(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_DirectorDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[Director] = []) -> int:
        try:
            query = '''INSERT INTO director (id_director, firstname, lastname) 
                           VALUES (%s, %s, %s);'''
            self.cur.executemany(query, [(obj.getid_director(), obj.getDirectorFirstname(), obj.getDirectorLastname()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorDAO.insertAll ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, id_director) -> Director:
        '''
            Find Director by id in database
        '''
        try:
            query = '''SELECT * from director WHERE id_director = %s'''
            self.cur.execute(query, (id_director,))
            res = self.cur.fetchone()
            if res:
                director = Director()
                director.setid_director(res[0])
                director.setDirectorFirstname(res[1])
                director.setDirectorLastname(res[2])
                return director
            else:
                return None
        except Exception as exception:
            print(f'''Error_DirectorDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()


    def findAll(self) -> list[Director]:
        try:
            query = '''SELECT * FROM director'''
            self.cur.execute(query)
            res = self.cur.fetchall()

            list_director = []

            if len(res) > 0:
                for row in res:
                    director = Director()
                    director.setid_director(row[0])
                    director.setDirectorFirstname(row[1])
                    director.setDirectorLastname(row[2])

                    list_director.append(director)
                return list_director
            else:
                return None
        except Exception as error:
            print(f'Return DirectorDAO.findAll() ::: {error}')
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[Director]:
        try:
            query = '''SELECT * FROM director WHERE firstname = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchall()

            list_director = []

            if len(res) > 0:
                for r in res:
                    d = Director()
                    d.setid_director(r[0])
                    d.setDirectorFirstname(r[1])
                    d.setDirectorLastname(r[2])
                    list_director.append(d)

                return list_director
            else:
                return None
        except Exception as e:
            print(f"Erreur_DirectorDAO.findOneByOne ::: {e}")
        finally:
            self.cur.close()


    def findOneWithLike(self, patternLike) -> list[Director]:
        '''
            Find one director with 'LIKE' in database
        '''
        try:
            query = '''SELECT * FROM director WHERE firstname LIKE %s'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()

            list_director = []
            if len(res) > 0:
                for direc in res:
                    director = Director()
                    director.setid_director(direc[0])
                    director.setDirectorFirstname(direc[1])
                    director.setDirectorLastname(direc[2])
                    list_director.append(director)
                return list_director
            else:
                return None
        except Exception as exception:
            print(f'''Error_DirectorDAO.findOneWithLike ::: {exception}''')
        finally:
            self.cur.close()

    def updateOne(self, cleAnc, objModif: Director) -> int:
        try:
            query = '''UPDATE director SET firstname = %s, lastname = %s
                           WHERE id_director = %s;'''
            self.cur.execute(query, (objModif.getDirectorFirstname(), objModif.getDirectorLastname(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorDAO.updateOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM director WHERE id_director = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorDAO.deleteOne() ::: {e}")
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
        try:
            query = '''select id_actor, firstname, lastname, substr(firstname, %s, %s) as initiale from actor a'''
            self.cur.execute(query, (start, nb_letter,))
            res = self.cur.fetchall()
            if len(res) > 0:
                return res
            else:
                return None

        except Exception as exception:
            print(f'''Error_DirectorDAO.getSubStr ::: {exception}''')
            return None
        finally:
            self.cur.close()


    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
