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
    
    def searchDirector(idDirector):
        try:
            d: DirectorM.Director = DirectorDAO().findOne(idDirector)
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

