class Movie:

    def __init__(self):
        self.__movie_id: int = None
        self.__movie_name: str = ''
        self.__movie_year: int = None
        self.__movie_rank: float = None

    def setMovieId(self, movie_id) -> None:
        self.__movie_id = movie_id

    def getMovieId(self) -> int:
        return self.__movie_id

    def setMovieName(self, movie_name) -> None:
        self.__movie_name = movie_name

    def getMovieName(self) -> str:
        return self.__movie_name

    def setMovieYear(self, movie_year) -> None:
        self.__movie_year = movie_year

    def getMovieYear(self) -> int:
        return self.__movie_year

    def setMovieRank(self, movie_rank) -> None:
        self.__movie_rank = movie_rank

    def getMovieRank(self) -> float:
        return self.__movie_rank
