from dao.ModelDAO import ModelDAO
from model.MovieGenreM import MovieGenre


class MovieGenre(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet MovieGenreDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieGenre) -> int:
        try:
            query = '''INSERT INTO actor (idMovie, genre)
                        VALUES (%s, %s)'''
            self.cur.execute(
                query, (objIns.getidMovie, objIns.getGenre))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.insertOne ::: {exception}''')
            return 0
        finally:
            self.cur.close()

    def insertAll(self, objInsList: list[MovieGenre] = []) -> int:
        try:
            query = '''INSERT INTO actor (idMovie, genre)
                        VALUES (%s, %s)'''
            self.cur.executemany(query, [(MovieGenre.getIdMovie(), MovieGenre.getGenre(
            )) for MovieGenre in objInsList])
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount > 0 else 0
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.insertAll ::: {exception}''')
            self.cur.connection.rollback()
        finally:
            self.cur.close()

    def findOne(self, idMovie) -> MovieGenre:
        try:
            query = '''SELECT * FROM actor WHERE idMovie = %s;'''
            self.cur.execute(query, (idMovie))
            res = self.cur.fetchone()

            if res:
                MovieGenre = MovieGenre()
                MovieGenre.setIdMovie(res[0])
                MovieGenre.setGenre(res[1])
                return MovieGenre
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.findOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findAll(self) -> list[MovieGenre]:
        try:
            query = '''SELECT * FROM MovieGenre;'''
            self.cur.execute(query)
            res = self.cur.fetchall()
            list_MovieGenre = []
            if len(res) > 0:
                for mg in res:
                    MovieGenre = MovieGenre()
                    MovieGenre.setIdMovie(a[0])
                    MovieGenre.setGenre(a[1])
                    list_MovieGenre.append(actor)
                return list_MovieGenre
            else:
                return None
        except Exception as exception:
            print(f"Error_MovieGenreDOA.findAll() ::: {exception}")
            return None
        finally:
            self.cur.close()

    def findOneByOne(self, pattern) -> list[MovieGenre]:
        try:
            query = '''SELECT * FROM MovieGenre WHERE genre = %s'''
            self.cur.execute(query, (pattern))
            res = self.cur.fetchall()
            list_MovieGenre = []
            if len(res) > 0:
                for a in res:
                    MovieGenre = MovieGenre()
                    MovieGenre.setIdMovie(a[0])
                    MovieGenre.setGenre(a[1])
                    list_MovieGenre.append(actor)
                return list_MovieGenre
            else:
                return None
        except Exception as exception:
            print(f'''Error_MovieGenreDAO.findOneByOne ::: {exception}''')
            return None
        finally:
            self.cur.close()

    def findOneByOneWithLike(self, patternLike) -> list[MovieGenre]:
        pass

    def UpdateOne(self, cleAnc, objModif: MovieGenre) -> int:
        
        try:
            query = '''UPDATE moviegenre SET genre = %s, WHERE idMovie = %s;'''
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
            query = f'''DELETE FROM MovieGenre WHERE idMovie = %s;'''
            self.cur.execute(query, (cleSup,))
            self.cur.connection.commit()
            return self.cur.rowcount if self.cur.rowcount!=0 else 0
        except Exception as e:
            print(f"Erreur_MovieGenreDAO.supprimerUn() ::: {e}")
            self.cur.connection.rollback()
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
