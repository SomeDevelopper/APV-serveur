class Director:

    def __init__(self) -> None:
        self.__id_director: int = None
        self.__firstname: str = None
        self.__lastname: str = None

    def setIdDirector(self, directorId) -> None:
        self.__id_director = directorId

    def getIdDirector(self) -> int:
        return self.__id_director

    def setDirectorFirstname(self, firstname) -> None:
        self.__firstname = firstname

    def getDirectorFirstname(self) -> str:
        return self.__firstname

    def setDirectorLastname(self, lastname) -> None:
        self.__lastname = lastname

    def getDirectorLastname(self) -> str:
        return self.__lastname
