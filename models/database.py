import mariadb
import os


class Database:
    def __init__(self):
        self.host = os.environ.get('DB_HOST')
        self.port = int(os.environ.get('DB_PORT')) if os.environ.get('DB_PORT') else 3306
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.database = os.environ.get('DB_DATABASE')
        print('this is test.')
        print(self.host)
        print(self.port)
        print(self.database)

    def connect(self):
        conn = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user='root',
         password='admin',
         database='invinsense')

        if conn:
            print("Connected Successfully")
        else:
            print("Connection Not Established")

        return conn


