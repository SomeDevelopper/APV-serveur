class User:

    def __init__(self) -> None:
        self.__uid: int = None
        self.__name: str = None

    def setUid(self, uid) -> None:
        self.__uid = uid
    
    def getUid(self) -> int:
        return self.__uid
    
    def setName(self, name) -> None:
        self.__name = name

    def getName(self) -> str:
        self.__name
