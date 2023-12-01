from model.DirectorM import Director
from model.MovieM import Movie


class MovieDirector:
    def __init__(self) -> None:
        self.__director_id: Director = None
        self.__movie_id: Movie = None

    def setDirectorId(self, director_id: Director) -> None:
        self.__director_id = director_id

    def getDirectorId(self) -> int:
        return self.__director_id

    def setMovieId(self, movie_id: Movie) -> None:
        self.__movie_id = movie_id

    def getMovieId(self) -> int:
        return self.__movie_id
