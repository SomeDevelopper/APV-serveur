from dao.ModelDAO import ModelDAO
from model.MovieM import Movie


class MovieDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: Movie) -> int:
        pass

    def insertAll(self, objInsList: list[Movie] = []) -> int:
        pass

    def findOne(self, idMovie) -> Movie:
        '''
            Find one movie by id in database
        '''
        try:
            query = '''SELECT * FROM movie WHERE id_movie = %s;'''
            self.cur.execute(query, (idMovie,))
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
        pass

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
