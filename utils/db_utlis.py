import sqlite3

def get_data_from_database(sql_query):
    database ='student.db'
    with sqlite3.connect(database) as connnection:
        return connnection.execute(sql_query)
        