from dao.ModelDAO import ModelDAO
from model.MovieGenreM import MovieGenre


class MovieGenreDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet MovieGenreDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieGenre) -> int:
        try:
            query = '''INSERT INTO movie_genre (id_movie, genre)
                        VALUES (%s, %s)'''
            self.cur.execute(
                query, (objIns.getMovieId(), objIns.getGenre()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()
        

    def insertAll(self, objInsList: list[MovieGenre] = []) -> int:
        try:
            query = '''INSERT INTO movie_genre (id_movie, genre)
                        VALUES (%s, %s)'''
            self.cur.executemany(query, [(obj.getMovieId(), obj.getGenre(
            )) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.insertAll ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, id_movie) -> MovieGenre:
        try:
            query = '''SELECT * FROM movie_genre WHERE id_movie = %s;'''
            self.cur.execute(query, (id_movie))
            res = self.cur.fetchone()

            if res:
                m = MovieGenre
                m.setMovieId(res[0])
                m.setGenre(res[1])
                return m
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findAll(self) -> list[MovieGenre]:
        try:
            query = '''SELECT * FROM movie_genre;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_movieGenre = []
            if len(res) > 0:
                for mg in res:
                    movieGenre = MovieGenre()
                    movieGenre.setid_movie(mg[0])
                    movieGenre.setGenre(mg[1])
                    list_movieGenre.append(movieGenre)
                return list_movieGenre
            else:
                return None
        except Exception as exception:
            print(f"Error_MovieGenreDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[MovieGenre]:
        try:
            query = '''SELECT * FROM movie_genre WHERE genre = %s'''
            self.cur.execute(query, (pattern))
            res = self.cur.fetchall()
            list_MovieGenre = []
            if len(res) > 0:
                for mg in res:
                    movieGenre = MovieGenre()
                    movieGenre.setid_movie(mg[0])
                    movieGenre.setGenre(mg[1])
                    list_MovieGenre.append(movieGenre)
                return list_MovieGenre
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.findOneByOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findOneWithLike(self, patternLike) -> list[MovieGenre]:
        try:
            query = '''SELECT * FROM movie_genre WHERE genre LIKE %s'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()
            list_movie_genr = []
            if len(res) > 0:
                for m in res:
                    movie = MovieGenre()
                    movie.setActorId(m[0])
                    movie.setFirstname(m[1])
                    movie.setLastname(m[2])
                    list_movie_genr.append(movie)
                return list_movie_genr
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.findOneWithLike ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def updateOne(self, cleAnc, objModif: MovieGenre) -> int:
        try:
            query = '''UPDATE movie_genre SET genre = %s, WHERE id_movie = %s;'''
            self.cur.execute(query, (objModif.getGenre(), cleAnc))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Error_MovieGenreDAO.updateOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()
           

    def deleteOne(self, cleSup) -> int:
        try:
            query = '''DELETE FROM movie_genre WHERE id_movie = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_MovieGenreDAO.supprimerUn() ::: {e}")
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
