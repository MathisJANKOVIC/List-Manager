import utils
import sys

OPERATION_OPTIONS = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", utils.EXIT_OPTION)
CONFIRMATION_OPTIONS = ("Ok", "Cancel")
LIST_CONTENT_MIN_MARGIN = 11

def main(lists, initial_cursor_position=0):
    list_manager_options = [list_element.name for list_element in lists] + [utils.EXIT_OPTION]
    selected_list_name = utils.menu("Select a list to manage", list_manager_options, utils.MENU_CURSOR_COLOR, initial_cursor_position)

    if(selected_list_name != utils.EXIT_OPTION):
        for list in lists:
            if(list.name == selected_list_name):
                selected_list = list
                break

        action = OPERATION_OPTIONS[0]
        while(action != utils.EXIT_OPTION):
            list_content = [f"- {element}" for element in list.content]

            if(len(list_content) > 0):
                longer_element = max(list_content, key=len)

                if(len(longer_element) < LIST_CONTENT_MIN_MARGIN): # a changer
                    for i, element in enumerate(list_content):
                        list_content[i] = element.ljust(LIST_CONTENT_MIN_MARGIN)
                else:
                    for i, element in enumerate(list_content):
                        list_content[i] = element.ljust(len(longer_element))

                title_menu = [f"{list.name} content :\n"] + list_content
            else:
                title_menu = selected_list.name + " (empty)"


            action = utils.menu(title_menu, OPERATION_OPTIONS, utils.MENU_CURSOR_COLOR, color_options="light_yellow", initial_cursor_position=action)

            if(action == OPERATION_OPTIONS[0]):
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

            elif(action == OPERATION_OPTIONS[1]):
                if(len(selected_list.content) > 0):
                    rm_options = selected_list.content + ["Cancel"]

                    sure_to_rm = None
                    element_to_rm = 0
                    while(sure_to_rm != CONFIRMATION_OPTIONS[0] and element_to_rm != rm_options[-1]):
                        element_to_rm = utils.menu("Choose an element to remove", rm_options, utils.MENU_CURSOR_COLOR, color_options="light_magenta", initial_cursor_position=element_to_rm)

                        if(element_to_rm != rm_options[-1]):
                            sure_to_rm = utils.menu(f"You are about to remove '{element_to_rm}' from '{selected_list.name}'", CONFIRMATION_OPTIONS, "red", initial_cursor_position=-1)

                            if(sure_to_rm == CONFIRMATION_OPTIONS[0]):
                                selected_list.remove(element_to_rm)
                else:
                    print("\n\033[95m You cannot remove an element, the list is empty \033[0m\n")
                    input(" Press enter to continue...")

            elif(action == OPERATION_OPTIONS[2]):
                if(len(selected_list.content) > 0): ###
                    sure_to_clear = utils.menu(f"You are about to clear list '{selected_list.name}'", CONFIRMATION_OPTIONS, "red", initial_cursor_position=-1)

                    if(sure_to_clear == CONFIRMATION_OPTIONS[0]):
                        selected_list.clear()
                else:
                    print("\n\033[95m The list is already empty \033[0m\n")
                    input(" Press enter to continue...")

            elif(action == OPERATION_OPTIONS[3]):
                sure_to_clear = utils.menu(f"You are about to delete list '{selected_list.name}'", CONFIRMATION_OPTIONS, "red", initial_cursor_position=-1)

                if(sure_to_clear == CONFIRMATION_OPTIONS[0]):
                    lists.remove(selected_list)
                    main(lists)
            else:
                main(lists, selected_list_name)
    else:
        return