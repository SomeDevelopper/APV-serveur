from dao.ModelDAO import ModelDAO
from model.MovieDirectorM import MovieDirector


class MovieDirectorDAO(ModelDAO):
    def __init__(self):
        '''
        Initialise l'objet ActorDAO en établissant une connexion à la base de données.
        '''
        params = ModelDAO.modeleDAO.connect_objet
        self.cur = params.cursor()

    def insertOne(self, objIns: MovieDirector) -> int:
        pass

    def insertAll(self, objInsList: list[MovieDirector] = []) -> int:
        pass

    def findOne(self, pattern) -> MovieDirector:
        try:
            query = 'SELECT * FROM movie_director WHERE %s = %s'
            self.cur.execute(query, (pattern[0], pattern[1],))
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
        pass

    def findOneByOne(self, pattern) -> list[MovieDirector]:
        pass

    def findOneWithLike(self, patternLike) -> list[MovieDirector]:
        pass

    def updateOne(self, cleAnc, objModif: MovieDirector) -> int:
        pass

    def deleteOne(self, cleSup) -> int:
        pass

    def getAverageRankForYear(self, year) -> list:
        pass

    def createUser(self, pwd, user) -> int:
        pass

    def createRole(self, role) -> int:
        pass

    def attribuerPrivilege(self, privileges: str, tables: str, role: str) -> int:
        pass

    def attributeRole(self, user, role) -> int:
        pass
