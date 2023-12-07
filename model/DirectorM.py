class Director:

    def __init__(self) -> None:
        self.__id_directord: int = None
        self.__firstname: str = None
        self.__lastname: str = None

    def setDirectorId(self, directorId) -> None:
        self.__id_directord = directorId

    def getDirectorId(self) -> int:
        return self.__id_directord

    def setDirectorFirstname(self, firstname) -> None:
        self.__firstname = firstname

    def getDirectorFirstname(self) -> str:
        return self.__firstname

    def setDirectorLastname(self, lastname) -> None:
        self.__lastname = lastname

    def getDirectorLastname(self) -> str:
        return self.__lastname
