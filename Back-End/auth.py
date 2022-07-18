""" This file takes care of the authentication logic for users """

from create_db import conn, c

class User:
    def __init__(self, email, password, pin):
        self.email = email
        self.password = password
        self.pin = pin

    def __repr__(self):
        return self.email


def sign_up(email, password, pin):
    user = User(email, password, pin)
    c.execute( f"INSERT INTO user VALUES ('{user.email}', '{user.password}', '{user.pin}') ")

    conn.commit()
    conn.close()
    return (user.email, user.password, user.pin)



def login(email, password, pin):
    c.execute(f"SELECT * FROM user WHERE email = '{email}' ")
    data = c.fetchone()
    
    if data == None:
        conn.close()
        return "Error! Invalid user email"
        
    
    stored_password = data[1]
    stored_pin = data[2]

    if stored_password != password or stored_pin != pin:
        conn.close()
        return "Error! pin or password doesn't match"
    else:
        conn.close()
        return "Successfully Loged In!"

