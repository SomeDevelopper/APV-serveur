class Movie:

    def __init__(self):
        self.__id_movie: int = None
        self.__name: str = ''
        self.__year: int = None
        self.__rank: float = None

    def setMovieId(self, movie_id) -> None:
        self.__id_movie = movie_id

    def getMovieId(self) -> int:
        return self.__id_movie

    def setMovieName(self, movie_name) -> None:
        self.__name = movie_name

    def getMovieName(self) -> str:
        return self.__name

    def setMovieYear(self, movie_year) -> None:
        self.__year = movie_year

    def getMovieYear(self) -> int:
        return self.__year

    def setMovieRank(self, movie_rank) -> None:
        self.__rank = movie_rank

    def getMovieRank(self) -> float:
        return self.__rank
