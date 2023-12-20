from dao.MovieGenreDAO import *
from model import MovieGenreM

class MovieGenre:
    @staticmethod
    def insert_data(objIns):
        try:
            mg = MovieGenreDAO().insertOne(objIns)
            if mg == None:
                return 'ERROR'
            return mg
        except Exception as exception:
            print(f'''Error_MovieC.insert_data ::: {exception}''')
        return None
