from model.MovieM import Movie


class MovieGenre:
    def __init__(self) -> None:
        self.__id_movie: Movie = None
        self.__genre: str = None

    def setMovieId(self, movie_id) -> None:
        self.__id_movie = movie_id

    def getMovieId(self) -> int:
        return self.__id_movie

    def setGenre(self, genre) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre
