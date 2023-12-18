from dao.DirectorDAO import *
from model import DirectorM


class Director:

# Find All Director in Database
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
    
# Find One Director in Database
@staticmethod
def FindOneDirectorGenre(idDirector):
        
        try:

            dDAO = DirectorDAO()

            d: DirectorM.Director = dDAO.findOne(idDirector)

            if d==None :
                return "ERROR"

            return d

        except Exception as e:
            print(f'Error_Director.FindOneDirector() ::: {e}')

        return None

# Add one Director in Database
@staticmethod
def AddDirector(idDirector, fisrtname, lastname):
        try:

            dDAO = DirectorDAO()

            objD = DirectorM.Director()

            objD.setIdDirector(idDirector)
            objD.setDirectorFirstname(fisrtname)
            objD.setDirectorLastname(lastname)

            d: int = dDAO.insertOne(objD)

            if d==0 :
                return "ERROR"

            return "Director added successfully"

        except Exception as e:
            print(f'Error_Director.AddDirector() ::: {e}')

        return None

# Update one Director in Database
@staticmethod
def updateDirector(idDirector, fisrtname, lastname):
        try:

            dDAO = DirectorDAO()

            objD = DirectorM.Director()

            objD.setIdDirector(idDirector)
            objD.setDirectorFirstname(fisrtname)
            objD.setDirectorLastname(lastname)

            d: int = dDAO.updateOne(idDirector, fisrtname, lastname)

            if d==0 :
                return "ERROR"

            return "Director updated successfully"

        except Exception as e:
            print(f'Error_DirectorGenreC.updateDirectorGenre() ::: {e}')

# Delete One Director in Database
@staticmethod
def deleteDirector(idDirector):
        try:

            dDAO = DirectorDAO()

            d: int = dDAO.deleteOne(idDirector)

            if d==0 :
                return "ERROR"

            return "Director deleted successfully"

        except Exception as e:
            print(f'Error_DirectorC.deleteDirector() ::: {e}')

        return None