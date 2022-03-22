from distutils.command.config import config
#from flaskext.mysql import MySQL
import mariadb


def createConnection():
    conn = mariadb.connect(
         host='localhost',
         port= 3306,
         user='root',
         password='root',
         database='invinsense')
    print(conn)
    return conn