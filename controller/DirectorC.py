from dao.DirectorDAO import *
from model import DirectorM


class Director:

    @staticmethod
    def get_all_director() -> str | DirectorM.Director:
        try:
            dDAO = DirectorDAO()
            call: list[DirectorM.Director] | str = dDAO.findAll()

            if call == None:
                return 'Error'

            return call
        except Exception as exception:
            print(f'''Error_DirectorC.get_all_movie ::: {exception}''')
        return None
    
    def searchDirector(id_director):
        try:
            d: DirectorM.Director = DirectorDAO().findOne(id_director)
            if d == None:
                return 'ERROR'
            return d
        except Exception as exception:
            print(f'''Error_DirectorC.searchDirector ::: {exception}''')
        return None
    
    def search_director_by_name(patternLike):
        try:
            d: list[DirectorM.Director] | str = DirectorDAO().findOneWithLike(patternLike)
            if d == None:
                return 'ERROR'
            return d
        except Exception as exception:
            print(f'''Error_DirectorC.search_director_by_name ::: {exception}''')
        return None
    
    @staticmethod
    def insert_data(objIns):
        try:
            d = DirectorDAO().insertOne(objIns)
            if d != 0:
                return d
            return 'ERROR'
        except Exception as exception:
            print(f'''Error_MovieC.insert_data ::: {exception}''')
        return None
    
    @staticmethod
    def get_initiale(start, nb_letter):
        try:
            d = DirectorDAO().getSubStr(start, nb_letter)
            if d == None:
                return 'ERROR'
            return d
        except Exception as exception:
            print(f'''Error_DirecorC.get_initiale ::: {exception}''')
        return None

