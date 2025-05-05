NAME_FILE = "./data/tasks.json"

from modules.controller.screen import *
from modules.menus import MENU_ADD, MENU_ADD_STATE
def add():
    clean_screen()
    print(MENU_ADD)
    name = input("add the name of the task\n->")

    clean_screen()
    print(MENU_ADD)
    description = input("add the description of the task\n->")

    clean_screen()
    print(MENU_ADD_STATE)
    try:
        case = int(input("->"))
    except ValueError:
        print("error, you entered an option that is not in the program")
        pause_screen()
    else:
        match case:
            case 1:
                state = "TODO"
            case 2: 
                state = "DOING"
            case 3: 
                state = "DONE"
            case _:
                pause_screen()
                return add()
    
    # decidir si crear una funcion para crear un id o una unfcion de id
    clean_screen()
    print(MENU_ADD)
    print(f"Your task has the follow characteristics:\n- Name: {name}\n- Description: {description}\n - State: {state}\n")
    try:
        case = int(input("->"))
    except ValueError:
        print("error, you entered an option that is not in the program")
        pause_screen()
    else:
        match case:
            case 1:
                state = "TODO"
