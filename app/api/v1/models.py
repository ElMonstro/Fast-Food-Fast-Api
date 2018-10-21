import psycopg2
from app.api import application

class DbaseConnection:
    def __init__(self):

        db_name = application.config['DB_NAME']
        host = application.config['HOST']
        user = application.config['USER']
        password = application.config['PASSWORD']
        try:
            conn_string = 'dbname={} user={} host={} password={}'.format(db_name, user, host, password)
            self.conn = psycopg2.connect(conn_string)
        except:
            print('Connection not successful')
