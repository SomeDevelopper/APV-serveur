from dao.RoleDAO import *
from model import RoleM

class Role:

    # Find All Role in Database
    @staticmethod
    def findAllRole():
        try:
            a: list[RoleM.DirectorGenre] | str = RoleDAO().findAll()
            if a == None:
                return 'ERROR'
            return a
        except Exception as exception:
            print(f'Error_RoleC.findAllRole ::: {exception}')
        return None
    
# Find One Role in Database
@staticmethod
def FindOneRole(idActor):
        
        try:

            rDAO = RoleDAO()

            r: RoleM.Role = rDAO.findOne(idActor)

            if r==None :
                return "ERROR"

            return r

        except Exception as e:
            print(f'Error_RoleC.FindOneRole() ::: {e}')

        return None

# Add one Role in Database
@staticmethod
def AddRole(idActor, idMovie, role):
        try:

            rDAO = RoleDAO()

            objR = RoleM.Role()

            objR.setActorId(idActor)
            objR.setMovieId(idMovie)
            objR.setRole(role)

            r: int = rDAO.insertOne(objR)

            if r==0 :
                return "ERROR"

            return "Role added successfully"

        except Exception as e:
            print(f'Error_RoleC.AddRole() ::: {e}')

        return None

# Update one Role in Database
@staticmethod
def updateRole(idActor, idMovie, role):
        try:

            rDAO = RoleDAO()

            objR = RoleM.Role()

            objR.setActorId(idActor)
            objR.setMovieId(idMovie)
            objR.setRole(role)

            r: int = rDAO.updateOne(idActor, idMovie, role)

            if r==0 :
                return "ERROR"

            return "Role updated successfully"

        except Exception as e:
            print(f'Error_RoleC.updateRole() ::: {e}')

# Delete One Role in Database
@staticmethod
def deleteRole(idActor):
        try:

            rDAO = RoleDAO()

            r: int = rDAO.deleteOne(idActor)

            if r==0 :
                return "ERROR"

            return "Role deleted successfully"

        except Exception as e:
            print(f'Error_RoleC.deleteRole() ::: {e}')

        return None

