from dao.MovieDAO import MovieDAO
from model import MovieM

class Movie:

    @staticmethod
    def searchMovie(idMovie):
        try:
            m: MovieM.Movie = MovieDAO().findOne(idMovie)
            if m == None:
                return 'ERROR'
            return m
        except Exception as exception:
            print(f'''Error_MovieC.searchMovie ::: {exception}''')
        return None
    
    @staticmethod
    def get_all_movie():
        try:
            m: list[MovieM.Movie] | str = MovieDAO().findAll()
            if m == None:
                return 'ERROR'
            return m
        except Exception as exception:
            print(f'''Error_MovieC.get_all_movie ::: {exception}''')
        return None
    
    @staticmethod
    def search_movie_by_title(patternLike):
        try:
            m: list[MovieM.Movie] | str() = MovieDAO().findOneWithLike(patternLike)
            if m == None:
                return 'ERROR'
            return m
        except Exception as exception:
            print(f'''Error_MovieC.search_movie_by_title ::: {exception}''')
        return None