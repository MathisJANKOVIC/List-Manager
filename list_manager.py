from ListElement import ListElement
import utils
import sys

OPERATION_MENU = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", "Exit")

def main(lists):
    list_manager_options = [list_element.name for list_element in lists] + ["Exit"]
    selected_list_name = utils.menu("Select a list to manage", list_manager_options, utils.MENU_CURSOR_COLOR)

    if(selected_list_name != list_manager_options[-1]):
        for list in lists:
            if(list.name == selected_list_name):
                selected_list = list
                break

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
                new_element = input(f" Enter the element to add to '{selected_list.name}' : ").strip()

                if(len(new_element) < 3):
                    sys.stdout.write("\n\033[31m element cannot be shorter than 3 characters \033[0m")
                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.write("\033[K")

                elif(len(new_element) > 20):
                    sys.stdout.write("\n\033[31m element cannot be longer than 20 characters \033[0m")
                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.write("\033[K")

                elif(not new_element.replace(" ","").replace("-","").isalnum()):
                    sys.stdout.write("\n\033[31m List name cannot contain special characters other than '-'\033[0m")
                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.write("\033[K")

                elif(new_element in [element for element in selected_list.content]):
                    sys.stdout.write(f"\n\033[31m Element '{new_element}' already exists in '{selected_list}'\033[0m")
                    sys.stdout.write("\033[F" * 2)
                    sys.stdout.write("\033[K")
                else:
                    break

            selected_list.add(new_element)
            # input(selected_list, type(selected_list), selected_list.add)

        elif(choice == OPERATION_MENU[1]):
            remove_options = [element for element in selected_list.content] + ["Cancel"]
            element_to_rm = utils.menu("Choose an element to remove", remove_options, utils.MENU_CURSOR_COLOR)

            if(element_to_rm != remove_options[-1]):
                sure_to_rm = utils.menu(f"Do you really want to remove '{element_to_rm}' from '{selected_list.name}' ?", ("Yes", "No"), "red", initial_cursor_position=-1)
                if(sure_to_rm == "Yes"):
                    selected_list.remove(element_to_rm)
        if(choice == OPERATION_MENU[2]):
            sure_to_clear = utils.menu(f"Are you sure to clear list '{selected_list.name}' ?", ("Yes", "No"), "red")

            if(sure_to_clear == "Yes"):
                selected_list.empty()
        elif(choice == OPERATION_MENU[3]):
            sure_to_clear = utils.menu(f"Are you sure to delete list '{selected_list.name}' ?", ("Yes", "No"), "red")

            if(sure_to_clear == "Yes"):
                lists.remove(selected_list)
        else:
            main(lists)
    else:
        return