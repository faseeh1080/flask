import mysql.connector
from flask import g

def get_cursor():
    if "cnx" not in g:
        g.cnx = mysql.connector.connect(user='root', password='mysqlroot',
                                    host='127.0.0.1',
                                    database='example_db')
    
    cursor = g.cnx.cursor(dictionary=True)
    return cursor

def close_cnx(e=None):
    cnx = g.pop('cnx', None)

    if cnx is not None:
        cnx.close()

def init_app(app):
    app.teardown_appcontext(close_cnx)
