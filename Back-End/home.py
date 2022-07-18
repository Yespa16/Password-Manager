"""
This file takes care of creating new password and fetching all passwords logic.
"""

from create_db import conn, c

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


def create_password(user, app, password, username="", email="", description=""):
    password = Password(user, app, password, username, email, description)
    c.execute(f"INSERT INTO password VALUES ({password.user}, '{password.app.lower()}', '{password.username}', '{password.email}', '{password.password}', '{password.description}')")
    conn.commit()
    conn.close()
    return (password.user, password.app)






def get_passwords(user):
    c.execute(f"SELECT * FROM password WHERE user={user}")
    return c.fetchall()

