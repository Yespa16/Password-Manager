import eel
from auth import login, sign_up
from home import get_passwords, create_password

eel.init("web")


eel.start("login.html", size=(500, 450) )