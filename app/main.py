import eel
from auth import login, sign_up


eel.init("web")


eel.start("login.html", size=(500, 450) )