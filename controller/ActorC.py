from dao.ActorDAO import ActorDAO
from model import ActorM


class Actor:

    # Find All Actor in Database
    @staticmethod
    def findAllActor():
        try:
            a: list[ActorM.Actor] | str = ActorDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'''Error_ActorC.findAllActor ::: {exception}''')
        return None

    # Find one actor with idActor in Database
    @staticmethod
    def findOneActor(idActor):
        pass

    # Add one actor in Database
    @staticmethod
    def addActor(idActor, firstname, lastname, gender):
        pass

    # Update one actor in Database
    @staticmethod
    def updateActor(idActor, firstname, lastname, gender):
        pass

    # Delete One Actor in Database
    @staticmethod
    def deleteActor(idActor):
        pass
