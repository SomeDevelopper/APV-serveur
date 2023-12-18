from dao.MovieDirectorDAO import *
from model import MovieDirectorM

class MovieDirector:

    # Find All MovieDirector in Database
    @staticmethod
    def findAllMovieDirector():
        try:
            a: list[MovieDirectorM.MovieDirector] | str = MovieDirectorDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'Error_MovieDirectorC.findAllMovieDirector ::: {exception}')
        return None
    
# Find One MovieDirector in Database
@staticmethod
def FindOneMovieDirector(idDirector):
        
        try:

            mdDAO = MovieDirectorDAO()

            md: MovieDirectorM.MovieDirector = mdDAO.findOne(idDirector)

            if md==None :
                return "ERROR"

            return md

        except Exception as e:
            print(f'Error_MovieDirectorC.FindOneMovieDirector() ::: {e}')

        return None

# Add one MovieDirector in Database
@staticmethod
def AddMovieDirector(idDirector, idMovie):
        try:

            mdDAO = MovieDirectorDAO()

            objMD = MovieDirectorM.MovieDirector()

            objMD.setDirectorId(idDirector)
            objMD.setMovieId(idMovie)

            md: int = mdDAO.insertOne(objMD)

            if md==0 :
                return "ERROR"

            return "MovieDirector added successfully"

        except Exception as e:
            print(f'Error_MovieDirectorC.AddMovieDirector() ::: {e}')

        return None

# Update one MovieDirector in Database
@staticmethod
def updateMovieDirector(idDirector, idMovie):
        try:

            mdDAO = MovieDirectorDAO()

            objMD = MovieDirectorM.MovieDirector()

            objMD.setDirectorId(idDirector)
            objMD.setMovieId(idMovie)

            md: int = mdDAO.updateOne(idDirector, idMovie)

            if md==0 :
                return "ERROR"

            return "MovieDirector updated successfully"

        except Exception as e:
            print(f'Error_MovieDirectorC.updateMovieDirector() ::: {e}')

# Delete One MovieDirector in Database
@staticmethod
def deleteMovieDirector(idDirector):
        try:

            mdDAO = MovieDirectorDAO()

            md: int = mdDAO.deleteOne(idDirector)

            if md==0 :
                return "ERROR"

            return "MovieDirector deleted successfully"

        except Exception as e:
            print(f'Error_MovieDirectorC.deleteMovieDirector() ::: {e}')

        return None