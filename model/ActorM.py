class Actor:

    def __init__(self) -> None:
        self.__id_actor: int = None
        self.__firstname: str = ''
        self.__lastname: str = ''
        self.__gender: str = ''

    def setActorId(self, actorId) -> None:
        self.__id_actor = actorId

    def getActorId(self) -> int:
        return self.__id_actor

    def setFirstname(self, firstname) -> None:
        self.__firstname = firstname

    def getFirstname(self) -> str:
        return self.__firstname

    def setLastname(self, lastname) -> None:
        self.__lastname = lastname

    def getLastname(self) -> str:
        return self.__lastname

    def setGender(self, gender) -> None:
        self.__gender = gender

    def getGender(self) -> str:
        self.__gender
