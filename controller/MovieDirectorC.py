from dao.MovieDirectorDAO import *
from model import MovieDirectorM


class MovieDirector:

    @staticmethod
    def get_movie_director(pattern) -> str | MovieDirectorM.MovieDirector:
        try:
            md: MovieDirectorM.MovieDirector = MovieDirectorDAO().findOne(pattern)
            if md == None:
                return 'ERROR'
            return md
        except Exception as exception:
            print(
                f'''Error_MovieDirectorC.get_movie_director ::: {exception}''')
        return None
