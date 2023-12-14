from dao.systadminDAO import *


class SystadminC:

    @staticmethod
    def createUser(passwd, user):
        try:
            sys: int = SystadminC().createUser(passwd, user)
            if sys == 0:
                return 'ERROR'
            return "CREATION D'UN NOUVEAU USER AVEC SUCCESS"
        except Exception as exception:
            print(f'''Erreur_systadminC.createUser ::: {exception}''')
        return None

    @staticmethod
    def createRole(role):
        try:
            sys: int = SystadminC().createRole(role)
            if sys == 0:
                return 'ERROR'
            return "CREATION D'UN NOUVEAU ROLE AVEC SUCCESS"
        except Exception as exception:
            print(f'''Erreur_systadminC.createRole ::: {exception}''')
        return None

    @staticmethod
    def attributePrivilegeRole(privileges, tables, roles):
        try:
            sys: int = Systadmin().attribuerPriviliege(privileges, tables, roles)
            if sys == 0:
                return "ERROR"
            return "ATTRIBUTION DE(S) PRIVILEGE(S) A UN ROLE AVEC SUCCES"
        except Exception as exception:
            print(f'Erreur_systadminC.attributePrivilegeRole ::: {exception}')
        return None

    @staticmethod
    def attributeRoleUser(user, role):
        try:
            sys: int = Systadmin().attributeRoleUser(user, role)
            if sys == 0:
                return 'ERROR'
            return "ATTRIBUTION DE(S) ROLE(S) A UN USER AVEC SUCCES"
        except Exception as exception:
            print(f'Error_systadminC.attributeRoleUser ::: {exception}')
