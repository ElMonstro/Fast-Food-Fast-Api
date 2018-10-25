import psycopg2
import json
from app.api import application

class DbaseConnection:
    def __init__(self):

        db_name = application.config['DB_NAME']
        host = application.config['HOST']
        user = application.config['USER']
        password = application.config['PASSWORD']
        try:
            conn_string = 'dbname={} user={} host={} password={};'.format(db_name, user, host, password)
            self.conn = psycopg2.connect(conn_string)
        except:
            print('Connection not successful')
        
        self.cursor = self.conn.cursor()
        try:
            sql_string = '''
            DROP TABLE IF EXISTS orders;
            DROP TABLE IF EXISTS users;
            CREATE TABLE orders(id int auto_increment PRIMARY KEY, email varchar(255), items JSON,);
            CREATE TABLE users(id int PRIMARY KEY, email varchar(255), password varchar(255),);'''
            self.cursor.execute(sql_string)
        except:
            print('Table not created')
        

    def save(self):
        self.conn.commit()
    
    def insert_order(self, item):
        item_json = json.dumps(item[1])
        sql_string = 'INSERT INTO orders(email, items) VALUES({}, {})'.format(item[0], item_json)
        try:
            self.cursor.execute(sql_string)
        except:
            print('Item not inserted')
        

    
    def get_all_items(self, table):
        sql_string = 'SELECT * FROM {}'.format(table)
        self.cursor.execute(sql_string)
        items = self.cursor.fetchall()
        return items

    def get_item(self, id, table):
        sql_string = 'SELECT * FROM {} WHERE ID = {}'.format(table.upper, str(id))
        self.cursor.execute(sql_string)
        item = self.cursor.fetchone()
        return item
    

        
        

