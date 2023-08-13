from ListElement import ListElement
import utils
import sys

OPERATION_MENU = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", "Exit")

def main(lists):
    list_manager_options = [list_element.name for list_element in lists] + ["Exit"]
    selected_list_name = utils.menu("Select a list to manage", list_manager_options, utils.MENU_CURSOR_COLOR, color_options="light_cyan")

    if(selected_list_name != "Exit"):
        for list in lists:
            if(list.name == selected_list_name):
                selected_list = list
                break
        choice = None

        while(choice != OPERATION_MENU[-1]):
            list_content = [f"- {element}" for element in list.content]

            if(len(list_content) > 0):
                longer_element = max(list_content, key=len)

                for i, element in enumerate(list_content):
                    list_content[i] = element.ljust(len(longer_element))

                title_menu = [f"{list.name} content :\n"] + list_content
            else:
                title_menu = selected_list.name + " (empty)"
            choice = utils.menu(title_menu, OPERATION_MENU, utils.MENU_CURSOR_COLOR)

            if(choice == OPERATION_MENU[0]):
                sys.stdout.write("\n")

                while(True):
                    new_element = input(f" Enter the element to add to '{selected_list.name}' : ")
                    new_element = new_element.strip()

                    sys.stdout.write("\n")
                    sys.stdout.write("\033[K") # deletes potencily previous message error

                    if(len(new_element) < 3):
                        sys.stdout.write("\033[31m Elements cannot be shorter than 3 characters \033[0m")

                    elif(len(new_element) > 20):
                        sys.stdout.write("\033[31m Elements cannot be longer than 20 characters \033[0m")

                    elif(not new_element.replace(" ","").replace("-","").isalnum()):
                        sys.stdout.write("\033[31m Elements cannot contain special characters \033[0m")

                    elif(new_element in [element for element in selected_list.content]):
                        sys.stdout.write(f"\033[31m Element '{new_element}' already exists in '{selected_list.name}'\033[0m")
                    else:
                        break

                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.write("\033[K")

                selected_list.add(new_element)

            elif(choice == OPERATION_MENU[1]):
                remove_options = [element for element in selected_list.content] + ["Cancel"]
                if(len(remove_options) > 1):
                    element_to_rm = utils.menu("Choose an element to remove", remove_options, utils.MENU_CURSOR_COLOR, color_options="light_magenta")

                    if(element_to_rm != remove_options[-1]):
                        sure_to_rm = utils.menu(f"You are about to remove '{element_to_rm}' from '{selected_list.name}'", ("Ok", "Cancel"), "red", initial_cursor_position=-1)

                        if(sure_to_rm == "Ok"):
                            selected_list.remove(element_to_rm)
                else:
                    print("\n\033[95m The list is empty so there is no element to remove \033[0m\n")
                    input(" Press enter to continue...")

            elif(choice == OPERATION_MENU[2]):
                if(len(selected_list.content) > 0):
                    sure_to_clear = utils.menu(f"You are about to clear list '{selected_list.name}'", ("Ok", "Cancel"), "red", initial_cursor_position=-1)

                    if(sure_to_clear == "Ok"):
                        selected_list.empty()
                else:
                    print("\n\033[95m The list is already empty \033[0m\n")
                    input(" Press enter to continue...")

            elif(choice == OPERATION_MENU[3]):
                sure_to_clear = utils.menu(f"You are about to delete list '{selected_list.name}'", ("Ok", "Cancel"), "red", initial_cursor_position=-1)

                if(sure_to_clear == "Ok"):
                    lists.remove(selected_list)
                    main(lists)
            else:
                main(lists)
    else:
        return