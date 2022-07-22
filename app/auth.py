import sys, os
import json 


""" This file takes care of the authentication logic for users """

from create_db import conn, c
import eel 


class User:
    def __init__(self, email, password, pin):
        self.email = email
        self.password = password
        self.pin = pin

    def __repr__(self):
        return self.email


@eel.expose
def sign_up(email, password, pin):
    response = {"type": "OK", "message": "Everything is OK"}
    # Check whether user exists
    c.execute(f"SELECT * FROM user WHERE email='{email}'")
    if c.fetchall() != None:
        response["type"] = "Error"
        response["message"] = "User already exists!"
        return json.dumps(response)
        
    try: 
        user = User(email, password, int(pin))
        c.execute( f"INSERT INTO user VALUES ('{user.email}', '{user.password}', '{user.pin}') ")

        conn.commit()
        response["type"] = "Success"
        response["message"] = "Successfully created new user"
        response["vars"] = {"user_id": c.lastrowid}
        return json.dumps(response)

    except:
        response["type"] = "Error"
        response["message"] = "Something was wrong. Please try again"
        return json.dumps(response)




@eel.expose
def login(email, password, pin):
    c.execute(f"SELECT rowid, * FROM user WHERE email = '{email}' ")
    data = c.fetchone()
    response = {"type": "OK", "message": "Everything is OK"}

    if data == None:
        print("Error! Invalid user email!")
        response["type"] = "Error"
        response["message"] = "Invalid email"
        
        return json.dumps(response)

    stored_password = data[2]
    stored_pin = data[3]
    if stored_password != password or stored_pin != int(pin):
        response["type"] = "Error"
        response["message"] = "Invalid password or pin"
        print("Error! pin or password doesn't match")
        return json.dumps(response)

    else:
        user_id = data[0]
        response["type"] = "Success"
        response["message"] = "Successfully Logged In"
        response["vars"] = {"user_id": user_id}
        print("Successfully logged in")
        return json.dumps(response)

if __name__ == "__main__":
    conn.close()
