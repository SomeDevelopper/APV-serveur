from dao.DirectorGenreDAO import *
from model import DirectorGenreM

class DirectorGenre:

    # Find All DirectorGenre in Database
    @staticmethod
    def findAllDirectorGenre():
        try:
            a: list[DirectorGenreM.DirectorGenre] | str = DirectorGenreDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'Error_DirectorGenreC.findAllDirectorGenre ::: {exception}')
        return None
    
# Find One DirectorGenre in Database
@staticmethod
def FindOneDirectorGenre(director_id):
        
        try:

            dgDAO = DirectorGenreDAO()

            dg: DirectorGenreM.DirectorGenre = dgDAO.findOne(director_id)

            if dg==None :
                return "ERROR"

            return dg

        except Exception as e:
            print(f'Error_DirectorGenreC.FindOneDirectorGenre() ::: {e}')

        return None

# Add one DirectorGenre in Database
@staticmethod
def AddDirectorGenre(director_id, genre):
        try:

            dgDAO = DirectorGenreDAO()

            objDG = DirectorGenreM.DirectorGenre()

            objDG.setDirectorId(director_id)
            objDG.setGenre(genre)

            dg: int = dgDAO.insertOne(objDG)

            if dg==0 :
                return "ERROR"

            return "DirectorGenre added successfully"

        except Exception as e:
            print(f'Error_DirectorGenreC.AddDirectorGenre() ::: {e}')

        return None

# Update one DirectorGenre in Database
@staticmethod
def updateDirectorGenre(director_id, genre):
        try:

            dgDAO = DirectorGenreDAO()

            objDG = DirectorGenreM.DirectorGenre()

            objDG.setDirectorId(director_id)
            objDG.setGenre(genre)

            dg: int = dgDAO.updateOne(director_id, genre)

            if dg==0 :
                return "ERROR"

            return "DirectorGenre updated successfully"

        except Exception as e:
            print(f'Error_DirectorGenreC.updateDirectorGenre() ::: {e}')

# Delete One DirectorGenre in Database
@staticmethod
def deleteDirectorGenre(director_id):
        try:

            dgDAO = DirectorGenreDAO()

            dg: int = dgDAO.deleteOne(director_id)

            if dg==0 :
                return "ERROR"

            return "DirectorGenre deleted successfully"

        except Exception as e:
            print(f'Error_DirectorGenreC.deleteDirectorGenre() ::: {e}')

        return None