import menus
import manipulate_database
import search_product
import backup_database
import error_messages


def main_menu():
    while True:
        menus.main_menu()
        option = input(">  ").lower().strip()
        if option in ["v", "a", "b", "x"]:
            if option == "v":
                pass
            elif option == "a":
                pass
            elif option == "b":
                pass
            elif option == "x":
                break
        else:
            error_messages.menu_choice_error("v, a, b, x")



if __name__ == "__main__":
    main_menu()