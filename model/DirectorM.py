class Director:

    def __init__(self) -> None:
        self.__director_id: int = None
        self.__director_firstname: str = None
        self.__director_lastname: str = None

    def setDirectorId(self, directorId) -> None:
        self.__director_id = directorId

    def getDirectorId(self) -> int:
        return self.__director_id

    def setDirectorFirstname(self, firstname) -> None:
        self.__director_firstname = firstname

    def getDirectorFirstname(self) -> str:
        return self.__director_firstname

    def setDirectorLastname(self, lastname) -> None:
        self.__director_lastname = lastname

    def getDirectorLastname(self) -> str:
        return self.__director_lastname
