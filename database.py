import sqlite3


connection = sqlite3.connect('student.db') # Database connection

cursur = connection.cursor() # created a cursor

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25) NOT NULL,
    COURSE VARCHAR(25) NOT NULL,
    SECTION VARCHAR(25) NOT NULL,
    MARKS INT
);
"""
cursur.execute(create_table_query)

# Insert records into the table
sql_query =""" INSERT INTO STUDENT (ID, NAME, COURSE, SECTION, MARKS) VALUES(?,?,?,?,?)"""
values = [ (1, 'Student1', 'Data Science', 'A', 80),
           (2, 'Student2', 'Data Science', 'B', 90), 
           (3, 'Student3', 'Data Science', 'A', 85), 
           (4, 'Student4', 'DevOps', 'B', 75), 
           (5, 'Student5', 'DevOps', 'A', 95), 
           (6, 'Student6', 'DevOps', 'B', 85)
           
         ]

cursur.executemany(sql_query, values) # execute the INSERT statement multiple times with the values


connection.commit() # commit the changes

data = cursur.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)
    

connection.close() # close the database connection



