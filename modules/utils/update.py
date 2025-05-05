from modules.controller.screen import *
from modules.menus import MENU_UPDATE

def update():
    print(MENU_UPDATE)
    try:
        case = int(input("->"))
    except ValueError:
        print("error, you entered an option that is not in the program")
        pause_screen()
    else:
        match case:
            case 1:
                pass
            case _:
                pause_screen()
                pass