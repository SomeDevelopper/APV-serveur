from model.ActorM import Actor
from model.MovieM import Movie


class Role:

    def __init__(self):
        self.__id_actor: Actor = None
        self.__id_movie: Movie = None
        self.__role: str = None

    def setActorId(self, actorId: Actor) -> None:
        self.__id_actor = actorId

    def getActorId(self) -> int:
        return self.__id_actor

    def setMovieId(self, movieId: Movie) -> None:
        self.__id_movie = movieId

    def getMovieId(self) -> int:
        return self.__id_movie

    def setRole(self, role) -> None:
        self.__role = role

    def getRole(self) -> str:
        return self.__role
