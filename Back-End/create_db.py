"""
This file was created to show how the database was created.
In this file there is also examples how to manipulate the database.
"""

import sqlite3 


conn = sqlite3.connect("database.db")

c = conn.cursor()

def create_user_table():
        c.execute("""CREATE TABLE user(
                email VARCHAR(100) unique,
                password VARCHAR(50),
                pin INTEGER(4)
                )""")
        conn.commit()
        conn.close()


def create_password_table():
        c.execute("""CREATE TABLE password (
                user INTEGER,
                app VARCHAR(50),
                username VARCHAR(50),
                email VARCHAR(100),
                password VARCHAR(50),
                description TEXT           

        )""")
        conn.commit()
        conn.close()



def examples_with_users():
        ## Create a user
        c.execute("INSERT INTO user VALUES('example@gmail.com', 'password', '1234' )")
        conn.commit()

        ## Select user from database
        c.execute("SELECT * FROM user WHERE email='example@gmail.com'")

        print(c.fetchone())


def examples_with_passwords():
        
        ## Create a password
        # c.execute("INSERT INTO password VALUES (1, 'google', 'username', 'example@gmail.com', 'password', 'some description' )")
        conn.commit()

        ## Get password from database
        c.execute("SELECT * FROM password WHERE (user=1 AND app='app_name')")
        print(c.fetchone())
        conn.close()

