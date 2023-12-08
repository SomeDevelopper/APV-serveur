from dao.DirectorDAO import *
from model import DirectorM


class Director:

    @staticmethod
    def findDirector() -> str | DirectorM.Director:
        try:
            dDAO = DirectorDAO()
            call: list[DirectorM.Director] | str = dDAO.findAll()

            if call == None:
                return 'Error'

            return call
        except Exception as error:
            print(error)
        return None
