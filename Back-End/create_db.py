"""
This file was created to show how the database was created.
In this file there is also examples how to manipulate the database.
"""

import sqlite3 


conn = sqlite3.connect("database.db")

c = conn.cursor()

def create_database():
        c.execute("""CREATE TABLE user(
                email VARCHAR(100) unique,
                password VARCHAR(50),
                pin INTEGER(4)
                )""")
        conn.commit()
        conn.close()



def examples():
        ## Create a user
        c.execute("INSERT INTO user VALUES('example1@gmail.com', 'password', '1234' )")
        conn.commit()

        ## Select user from
        c.execute("SELECT * FROM user WHERE email='codingyespa@gmail.com' ")

        print(c.fetchone())



        conn.close()
