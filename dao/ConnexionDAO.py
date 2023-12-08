import yaml
import psycopg2

import logging


class ConnexionDB:
    def __init__(self) -> None:
        self.cnx = None
        self.params = None

    def getConnexion(self):
        try:
            print("Get Params from config.yaml in progress")
            with open("config/config.yaml", "r") as filc:
                data = yaml.safe_load(filc)
            # config = data["postgreSQL_access"]
            host = data['host']
            port = data['port']
            db = data['database']
            user = data['user']
            passwd = data['passwd']

            self.cnx = psycopg2.connect(
                database=db, user=user, password=passwd, host=host, port=port)
            logging.info('Database connected successfully')
            print(f"Database connected successfully")
        except Exception as error:
            print(f"Connection Error: {error}")
        return self.cnx
