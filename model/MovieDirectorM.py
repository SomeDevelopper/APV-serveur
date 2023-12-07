from model.DirectorM import Director
from model.MovieM import Movie


class MovieDirector:
    def __init__(self) -> None:
        self.__id_director: Director = None
        self.__id_movie: Movie = None

    def setDirectorId(self, director_id: Director) -> None:
        self.__id_director = director_id

    def getDirectorId(self) -> int:
        return self.__id_director

    def setMovieId(self, movie_id: Movie) -> None:
        self.__id_movie = movie_id

    def getMovieId(self) -> int:
        return self.__id_movie
