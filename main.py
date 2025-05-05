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
                print("thanks for using our program :)")
                pause_screen()
            case _:
                print("error, you entered an option that is not in the program")
                pause_screen()
                return program()


if __name__ == "__main__":
    program()