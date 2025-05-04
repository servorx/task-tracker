from modules.imports import *

def program():
    clean_screen()
    print(MENU_MAIN)
    try:
        casos = int(input("->"))
    except ValueError:
        pause_screen()
        return program()
    else:
        match casos:
            case 1:
                add()
                return program()
            case 2:
                delete()
                return program()
            case 3:
                show()
                return program()
            case 4:
                update()
                return program()
            case 5:
                pause_screen()
            case _:
                print("error, ingreso una opcion que no se encuentra en el programa")
                pause_screen()
                return program()


if __name__ == "__main__":
    while True:
        program()