from dao.DirectorGenreDAO import *
from model import DirectorGenreM

class DirectorGenre:

    @staticmethod
    def insert_data(objIns):
        try:
            dg = DirectorGenreDAO().insertOne(objIns)
            if dg == None:
                return 'ERROR'
            return dg
        except Exception as exception:
            print(f'''Error_MovieC.insert_data ::: {exception}''')
        return None