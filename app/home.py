"""
This file takes care of creating new password and fetching all passwords logic.
"""

from create_db import conn, c
import eel, json

class Password:
    def __init__(self, user, app, password, username="", email="", description="",):
        self.user = user
        self.app = app
        self.password = password
        self.username = username
        self.email = email
        self.description = description

    
    def __repr__(self):
        return f"User: {self.user}\nApp: {self.app}"

@eel.expose
def create_password(user, app, password, username="", email="", description=""):

    response = {"type": "OK", "message": "Everything is OK"}
    try:
        
        password = Password(user, app, password, username, email, description)
        c.execute(f"INSERT INTO password VALUES ({password.user}, '{password.app.lower()}', '{password.username}', '{password.email}', '{password.password}', '{password.description}')")
        conn.commit()
        response["type"] = "Success"
        response["Message"] = "Password successfully added to database!"
        return json.dumps(response)
    except:
        response["type"] = "Error"
        response["message"] = "Something went wrong. Please try again."
        return json.dumps(response)





@eel.expose
def get_passwords(user_id):
    c.execute(f"SELECT app, email, username, password, description FROM password WHERE user={int(user_id)} ")
    return json.dumps(c.fetchall())

