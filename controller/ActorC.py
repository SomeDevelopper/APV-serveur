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

    # Find one actor with id_actor in Database
    @staticmethod
    def searchActor(id_actor):
        '''
        Search Actor by id
        '''
        try:
            a: ActorM.Actor = ActorDAO().findOne(id_actor)
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'''Error_ActorC.searchActor ::: {exception}''')
        return None
    
    @staticmethod
    def search_actor_by_title(pattern):
        '''
            Search Actor by Name in database
        '''
        try:
            a: list[ActorM.Actor] | str = ActorDAO().findOneWithLike(pattern)
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'''Error_ActorC.search_actor_by_title ::: {exception}''')
        return None
    
    @staticmethod
    def insert_data(objIns):
        try:
            a = ActorDAO().insertOne(objIns)
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'''Error_MovieC.insert_data ::: {exception}''')
        return None
    
    @staticmethod
    def get_ntile_actor():
        try:
            a = ActorDAO().getNtileData()
            if a != 0:
                return a
            return 'ERROR'
        except Exception as exception:
            print(f"Error_ActorC.get_ntile_actor ::: {exception}")
        return None