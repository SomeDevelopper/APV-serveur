from model.ActorM import Actor
from model.MovieM import Movie


class Role:

    def __init__(self):
        self.__actor_id: Actor = None
        self.__movie_id: Movie = None
        self.__role: str = None

    def setActorId(self, actorId: Actor) -> None:
        self.__actor_id = actorId

    def getActorId(self) -> int:
        return self.__actor_id

    def setMovieId(self, movieId: Movie) -> None:
        self.__movie_id = movieId

    def getMovieId(self) -> int:
        return self.__movie_id

    def setRole(self, role) -> None:
        self.__role = role

    def getRole(self) -> str:
        return self.__role
