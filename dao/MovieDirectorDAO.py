from dao import ModelDAO
from model.MovieDirectorM import MovieDirector


class MovieDirectorDAO(ModelDAO.ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet MovieDirectorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieDirector) -> int:
        try:
            query = '''INSERT INTO movie_director (id_movie, id_director)
                        VALUES (%s, %s)'''
            self.cur.execute(
                query, (objIns.getMovieId(), objIns.getDirectorId(),))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieDirectorDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[MovieDirector] = []) -> int:
        try:
            query = '''INSERT INTO movie_director (id_movie, id_director) 
                           VALUES (%s, %s, %s);'''
            self.cur.executemany(query, [(obj.getMovieId(), obj.getDirectorId()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MovieDirectorDAO.insertAll ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, pattern) -> MovieDirector:
        try:
            query = f'SELECT * FROM movie_director WHERE id_movie = %s'
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchone()
            if res:
                md = MovieDirector()
                md.setMovieId(res[0])
                md.setDirectorId(res[1])
                return md
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieDirectorDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findAll(self) -> list[MovieDirector]:
        try:
            query = '''SELECT * FROM movie_director md;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_md = []
            if len(res) > 0:
                for r in res:
                    md = MovieDirector()
                    md.setActorId(r[0])
                    md.setFirstname(r[1])
                    md.setLastname(r[2])
                    list_md.append(md)
                return list_md
            else:
                return None
        except Exception as exception:
            print(f"Error_MoviDirectorDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[MovieDirector]:
        pass

    def findOneWithLike(self, patternLike) -> list[MovieDirector]:
        pass

    def updateOne(self, cleAnc, objModif: MovieDirector) -> int:
        try:
            query = '''UPDATE movie_director SET id_director = %s
                           WHERE id_movie = %s;'''
            self.cur.execute(query, (objModif.getDirectorId(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MovieDirectorDAO.updateOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM movie_director WHERE id_movie = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MovieDirectorDAO.deleteOne() ::: {e}")
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
