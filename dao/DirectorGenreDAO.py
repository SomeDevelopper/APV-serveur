from dao.ModelDAO import ModelDAO
from model.DirectorGenreM import DirectorGenre


class DirectorGenreDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet DirectorGenreDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: DirectorGenre) -> int:
        try:
            query = '''INSERT INTO director_genre (id_director, genre)
                        VALUES (%s, %s)'''
            self.cur.execute(
                query, (objIns.getDirectorId(), objIns.getGenre(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_DirectorGenreDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[DirectorGenre] = []) -> int:
        try:
            query = '''INSERT INTO director_genre (id_director, genre) 
                           VALUES (%s, %s);'''
            self.cur.executemany(query, [(obj.getDirectorId(), obj.getGenre()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorGenreDAO.insertAll ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, pattern) -> DirectorGenre:
        try:
            query = '''SELECT * FROM director_genre WHERE id_director = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchone()
            if res:
                dg = DirectorGenre()
                dg.setDirectorId(res[0])
                dg.setGenre(res[1])
                return dg
            else:
                return None
        except Exception as exception:
            print(f'''Error_DirectorGenreDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findAll(self) -> list[DirectorGenre]:
        try:
            query = '''SELECT * FROM actor a;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_dg = []
            if len(res) > 0:
                for dirg in res:
                    dg = DirectorGenre()
                    dg.setActorId(dirg[0])
                    dg.setFirstname(dirg[1])
                    dg.setLastname(dirg[2])
                    list_dg.append(dg)
                return list_dg
            else:
                return None
        except Exception as exception:
            print(f"Error_DirectorGenreDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[DirectorGenre]:
        try:
            query = '''SELECT * FROM director_genre WHERE genre = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchall()

            list_dg = []

            if len(res) > 0:
                for r in res:
                    dg = DirectorGenre()
                    dg.setActorId(r[0])
                    dg.setFirstname(r[1])
                    dg.setLastname(r[2])
                    list_dg.append(dg)

                return list_dg
            else:
                return None
        except Exception as e:
            print(f"Erreur_DirectorGenreDAO.findOneByOne ::: {e}")
        finally:
            self.cur.close()

    def findOneWithLike(self, patternLike) -> list[DirectorGenre]:
        try:
            query = '''SELECT * FROM director_genre WHERE genre LIKE %s'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()
            list_dg = []
            if len(res) > 0:
                for r in res:
                    dg = DirectorGenre()
                    dg.setActorId(r[0])
                    dg.setFirstname(r[1])
                    dg.setLastname(r[2])
                    list_dg.append(dg)
                return list_dg
            else:
                return None
        except Exception as exception:
            print(f'''Error_DirectorGenreDAO.findOneWithLike ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def updateOne(self, cleAnc, objModif: DirectorGenre) -> int:
        try:
            query = '''UPDATE director_genre SET role = %s
                           WHERE id_director = %s;'''
            self.cur.execute(query, (objModif.getGenre(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorGenreDAO.updateOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM director_genre WHERE id_director = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_DirectorGenreDAO.deleteOne() ::: {e}")
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
