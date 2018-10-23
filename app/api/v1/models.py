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
        
        self.cursor = self.conn.cursor()
        try:
            sql_string = 'CREATE TABLE orders test(id PRIMARY KEY, customer_name varchar, items JSON,)'
            self.cursor.execute(sql_string)
        except:
            print('Table not created')
        

    def save(self):
        self.conn.commit()
    
    def insert(self, table, item):
        pass


    
    def get_all_items(self, table):
        sql_string = 'SELECT * FROM {}'.format(table)
        self.cursor.execute(sql_string)

    def get_item(self, id, table):
        sql_string = 'SELECT * FROM {} WHERE ID = {}'.format(table, str(id))
        self.cursor.execute(sql_string)

    

        
        

