class Actor:

    def __init__(self) -> None:
        self.__actor_id: int = None
        self.__first_name: str = ''
        self.__last_name: str = ''
        self.__gender: str = ''

    def setActorId(self, actorId) -> None:
        self.__actor_id = actorId

    def getActorId(self) -> int:
        return self.__actor_id

    def setFirstname(self, firstname) -> None:
        self.__first_name = firstname

    def getFirstname(self) -> str:
        return self.__first_name

    def setLastname(self, lastname) -> None:
        self.__last_name = lastname

    def getLastname(self) -> str:
        return self.__last_name

    def setGender(self, gender) -> None:
        self.__gender = gender

    def getGender(self) -> str:
        self.__gender
