from Repository import Repository
from Controller import Controller
from UI import UI

def main():
    r=Repository()
    c=Controller(r)
    u=UI(c)
    u.menu()

main()