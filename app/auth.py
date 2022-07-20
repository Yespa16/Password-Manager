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
    try: 
        user = User(email, password, int(pin))
        c.execute( f"INSERT INTO user VALUES ('{user.email}', '{user.password}', '{user.pin}') ")

        conn.commit()
        conn.close()
        response["type"] = "Success"
        response["message"] = "Successfully created new user"
        return json.dumps(response)

    except:
        response["type"] = "Error"
        response["message"] = "Something was wrong. Please try again"
        return json.dumps(response)




@eel.expose
def login(email, password, pin):
    c.execute(f"SELECT * FROM user WHERE email = '{email}' ")
    data = c.fetchone()
    response = {"type": "OK", "message": "Everything is OK"}
    print(password, pin)

    if data == None:
        print("Error! Invalid user email!")
        response["type"] = "Error"
        response["message"] = "Invalid email"
        
        return json.dumps(response)

    stored_password = data[1]
    stored_pin = data[2]
    if stored_password != password or stored_pin != int(pin):
        response["type"] = "Error"
        response["message"] = "Invalid password or pin"
        print("Error! pin or password doesn't match")
        return json.dumps(response)

    else:
        response["type"] = "Success"
        response["message"] = "Successfully Logged In"
        print("Successfully logged in")
        return json.dumps(response)

if __name__ == "__main__":
    conn.close()
