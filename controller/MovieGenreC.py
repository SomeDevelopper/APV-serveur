from dao.MovieGenreDAO import *
from model import MovieGenreM

@staticmethod
    def visualiserMovieGenre():
        
        try:

            mgDAO = MovieGenreDAO()

            cs: list[MovieGenreM.Movie] = mgDAO.FindAll()

            if cs==None :
                return "ERROR"

            return cs

        except Exception as e:
            print(f'Error_MovieGenreC.visualiserMovieGenre() ::: {e}')

        return None

def modifierUn(idMovie, genre):
        
    
        try:

            mgDAO = MovieGenreDAO()

            objB = MovieGenreM.Brands()

            objB.setBrandName(nameB)

            mg: int = mgDAO.modifierUn(idB, objB)

            if b==0 :
                return "ERROR"

            return "MODIFICATION DE MovieGenre AVEC SUCCES"

        except Exception as e:
            print(f'Erreur_MovieGenreC.modifierUnMovieGenre() ::: {e}')

        return None