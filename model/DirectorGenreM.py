from model.DirectorM import Director


class DirectorGenre:
    def __init__(self) -> None:
        self.__id_director: Director = None
        self.__genre: str = None

    def setDirectorId(self, director_id) -> None:
        self.__id_director = director_id

    def getDirectorId(self) -> int:
        return self.__id_director

    def setGenre(self, genre) -> None:
        self.__genre = genre

    def getGenre(self) -> str:
        return self.__genre
