from dao.ModelDAO import ModelDAO
from model.MovieM import Movie


class MovieDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet MovieDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Movie) -> int:
        try:
            query = '''INSERT INTO movie (id_movie, name, year_movie, rank)
                        VALUES (%s, %s, %s, %s)'''
            self.cur.execute(
                query, (objIns.getMovieId(), objIns.getMovieName(), objIns.getMovieYear(), objIns.getMovieRank()))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[Movie] = []) -> int:
        try:
            query = '''INSERT INTO movie (id_movie, name, year_movie, rank) 
                           VALUES (%s, %s, %s, %s);'''
            self.cur.executemany(query, [(obj.getMovieId(), obj.getMovieName(), obj.getMovieYear(), obj.getMovieRank()) for obj in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MovieDAO.insertAll ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, id_movie) -> Movie:
        '''
            Find one movie by id in database
        '''
        try:
            query = '''SELECT * FROM movie WHERE id_movie = %s;'''
            self.cur.execute(query, (id_movie,))
            res = self.cur.fetchone()
            if res:
                movie = Movie()
                movie.setMovieId(res[0])
                movie.setMovieName(res[1])
                movie.setMovieYear(res[2])
                movie.setMovieRank(res[3])
                return movie
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()
    
    def findAll(self) -> list[Movie]:
        '''
            Get all movie from database
        '''
        try:
            query = '''SELECT * FROM movie m;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_movie = []
            if len(res) > 0:
                for m in res:
                    movie = Movie()
                    movie.setMovieId(m[0])
                    movie.setMovieName(m[1])
                    movie.setMovieYear(m[2])
                    movie.setMovieRank(m[3])
                    list_movie.append(movie)
                return list_movie
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieDOA.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()


    def findOneByOne(self, pattern) -> list[Movie]:
        try:
            query = '''SELECT * FROM movie WHERE name = %s;'''
            self.cur.execute(query, (pattern,))
            res = self.cur.fetchall()

            list_movie = []

            if len(res) > 0:
                for r in res:
                    movie = Movie()
                    movie.setMovieId(r[0])
                    movie.setMovieName(r[1])
                    movie.setMovieYear(r[2])
                    movie.setMovieRank(r[3])
                    list_movie.append(movie)

                return list_movie
            else:
                return None
        except Exception as e:
            print(f"Erreur_MovieDAO.findOneByOne ::: {e}")
        finally:
            self.cur.close()

    def findOneWithLike(self, patternLike) -> list[Movie]:
        '''
            Find one movie with 'LIKE' in database
        '''
        try:
            query = '''SELECT * FROM movie WHERE name LIKE %s;'''
            self.cur.execute(query, (patternLike,))
            res = self.cur.fetchall()

            list_movie = []
            if len(res) > 0:
                for mv in res:
                    movie = Movie()
                    movie.setMovieId(mv[0])
                    movie.setMovieName(mv[1])
                    movie.setMovieYear(mv[2])
                    movie.setMovieRank(mv[3])
                    list_movie.append(movie)
                return list_movie
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieDAO.findMovieWithLike ::: {exception}''')
        finally:
            self.cur.close()
            
    def updateOne(self, cleAnc, objModif: Movie) -> int:
        try:
            query = '''UPDATE movie SET id_movie = %s, WHERE id_movie = %s;'''
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
            query = '''DELETE FROM movie WHERE id_movie = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount != 0 else 0
        except Exception as e:
            print(f"Erreur_MovieDAO.deleteOne() ::: {e}")
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def getAverageRankForYear(self, year):
        '''
            Get average movie rank for specific year from database
        '''
        try:
            query = '''SELECT AVG(rank)::numeric(10) from movie where year_movie = %s'''
            self.cur.execute(query, (year,))
            res = self.cur.fetchall()
            if res:
                return res[0]
            else:
                return None


        except Exception as exception:
            print(f'''Error_MovieDAO.getAverageRankForYear ::: {exception}''')
        finally:
            self.cur.close()

    def getNtileData(self) -> list:
        pass

    def getCaseRank(self) -> list:
        try:
            query = '''select id_movie, name, year_movie, rank, 
                            case
                                when rank <= 3 then 'Null'
                                when rank > 3 and rank < 7 then 'Moyen'
                                else 'Bon'
                            end as evalutation
                        from movie m;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            if len(res) > 0:
                return res
            else:
                return None
        except Exception as exception:
            print(f'Error_MovieDAO.getCaseRank ::: {exception}')
            return None
        finally:
            self.cur.close()

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
