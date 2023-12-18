from dao.MovieGenreDAO import *
from model import MovieGenreM

class MovieGenre:

    # Find All MovieGenre in Database
    @staticmethod
    def findAllMovieGenre():
        try:
            a: list[MovieGenreM.MovieGenre] | str = MovieGenreDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'Error_MovieGenreC.findAllMovieGenre ::: {exception}')
        return None
    
# Find One MovieGenre in Database
@staticmethod
def FindOneMovieGenre(idMovie):
        
        try:

            mgDAO = MovieGenreDAO()

            mg: MovieGenreM.MovieGenre = mgDAO.findOne(idMovie)

            if mg==None :
                return "ERROR"

            return mg

        except Exception as e:
            print(f'Error_MovieGenreeC.FindOneMovieGenre() ::: {e}')

        return None

# Add one MovieGenre in Database
@staticmethod
def AddMovieGenre(idMovie, genre):
        try:

            mgDAO = MovieGenreDAO()

            objMG = MovieGenreM.MovieGenre()

            objMG.setMovieId(idMovie)
            objMG.setGenre(genre)

            mg: int = mgDAO.insertOne(objMG)

            if mg==0 :
                return "ERROR"

            return "MovieGenre added successfully"

        except Exception as e:
            print(f'Error_MovieGenreC.AddMovieGenre() ::: {e}')

        return None

# Update one MovieGenre in Database
@staticmethod
def updateMovieGenre(idMovie, genre):
        try:

            mgDAO = MovieGenreDAO()

            objMG = MovieGenreM.MovieGenre()

            objMG.setMovieId(idMovie)
            objMG.setGenre(genre)

            mg: int = mgDAO.updateOne(idMovie, genre)

            if mg==0 :
                return "ERROR"

            return "MovieGenre updated successfully"

        except Exception as e:
            print(f'Error_MovieGenreC.updateMovieGenre() ::: {e}')

# Delete One MovieGenre in Database
@staticmethod
def deleteMovieGenre(idMovie):
        try:

            mgDAO = MovieGenreDAO()

            mg: int = mgDAO.deleteOne(idMovie)

            if mg==0 :
                return "ERROR"

            return "MovieGenre deleted successfully"

        except Exception as e:
            print(f'Error_MovieGenreC.deleteMovieGenre() ::: {e}')

        return None