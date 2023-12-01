from model.DirectorM import Director


class DirectorGenre:
    def __init__(self) -> None:
        self.__director_id: Director = None
        self.__genre: str = None
        self.__prob: float = None

    def setDirectorId(self, director_id) -> None:
        self.__director_id = director_id

    def getDirectorId(self) -> int:
        return self.__director_id

    def setGenre(self, genre) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre

    def setProd(self, prob) -> None:
        self.__prob = prob

    def getProb(self) -> float:
        return self.__prob
