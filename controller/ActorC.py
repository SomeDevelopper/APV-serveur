from dao.ActorDAO import *
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
    
# Find One Actor in Database
@staticmethod
def FindOneActor(ida):
        
        try:

            aDAO = ActorDAO()

            a: ActorM.Actor = aDAO.findOne(ida)

            if a==None :
                return "ERROR"

            return a

        except Exception as e:
            print(f'Error_Actor.FindOneActor() ::: {e}')

        return None

# Add one Actor in Database
@staticmethod
def AddActor(ida, nom, prenom, films):
        try:

            aDAO = ActorDAO()

            objA = ActorM.Actor()

            objA.setActorId(ida)
            objA.setFirstname(nom)
            objA.setLastname(prenom)
            objA.setActorMovie(films)

            a: int = aDAO.insertOne(objA)

            if a==0 :
                return "ERROR"

            return "Actor added successfully"

        except Exception as e:
            print(f'Error_Actor.AddActor() ::: {e}')

        return None

# Update one Actor in Database
@staticmethod
def updateActor(ida, nom, prenom, films):
        try:

            aDAO = ActorDAO()

            objA = ActorM.Actor()

            objA.setActorId(ida)
            objA.setFirstname(nom)
            objA.setLastname(prenom)
            objA.setActorMovie(films)

            a: int = aDAO.updateOne(ida, nom, prenom, films)

            if a==0 :
                return "ERROR"

            return "Actor updated successfully"

        except Exception as e:
            print(f'Error_ActorC.updateActor() ::: {e}')

# Delete One Actor in Database
@staticmethod
def deleteActor(ida):
        try:

            aDAO = ActorDAO()

            a: int = aDAO.deleteOne(ida)

            if a==0 :
                return "ERROR"

            return "Actor deleted successfully"

        except Exception as e:
            print(f'Error_ActorC.deleteActor() ::: {e}')

        return None