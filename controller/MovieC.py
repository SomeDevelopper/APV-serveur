from dao.MovieDAO import *
from model import MovieM

from dao.MovieDAO import *
from model import MovieM

class Movie:

    # Find All Movie in Database
    @staticmethod
    def findAllMovie():
        try:
            a: list[MovieM.Movie] | str = MovieDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'Error_MovieC.findAllMovie ::: {exception}')
        return None
    
# Find One Movie in Database
@staticmethod
def FindOneMovie(idMovie):
        
        try:

            mDAO = MovieDAO()

            m: MovieM.Movie = mDAO.findOne(idMovie)

            if m==None :
                return "ERROR"

            return m

        except Exception as e:
            print(f'Error_MovieC.FindOneMovie() ::: {e}')

        return None

# Add one Movie in Database
@staticmethod
def AddMovie(idMovie, name, year, rank):
        try:

            mDAO = MovieDAO()

            objM = MovieM.Movie()

            objM.setMovieId(idMovie)
            objM.setMovieName(name)
            objM.setMovieYear(year)
            objM.setMovieRank(rank)

            m: int = mDAO.InsertOne(objM)

            if m==0 :
                return "ERROR"

            return "Movie added successfully"

        except Exception as e:
            print(f'Error_MovieC.AddMovie() ::: {e}')

        return None

# Update one Movie in Database
@staticmethod
def updateMovie(idMovie, name, year, rank):
        try:

            mDAO = MovieDAO()

            objM = MovieM.Movie()

            objM.setMovieId(idMovie)
            objM.setMovieName(name)
            objM.setMovieYear(year)
            objM.setMovieRank(rank)

            m: int = mDAO.updateOne(idMovie, name, year, rank)

            if m==0 :
                return "ERROR"

            return "Movie updated successfully"

        except Exception as e:
            print(f'Error_MovieC.updateMovie() ::: {e}')

# Delete One Movie in Database
@staticmethod
def deleteMovie(idMovie):
        try:

            mDAO = MovieDAO()

            m: int = mDAO.deleteOne(idMovie)

            if m==0 :
                return "ERROR"

            return "Movie deleted successfully"

        except Exception as e:
            print(f'Error_MovieC.deleteMovie() ::: {e}')

        return None