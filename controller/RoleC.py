from dao.RoleDAO import *
from model import RoleM

class Role:
    @staticmethod
    def insert_data(objIns):
        try:
            r = RoleDAO().insertOne(objIns)
            if r != 0:
                return r
            return 'ERROR'
        except Exception as exception:
            print(f'''Error_MovieC.insert_data ::: {exception}''')
        return None
