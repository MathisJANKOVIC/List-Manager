from list_manager import ListElement
import console_menu
import termcolor

import json
import sys
import os

SAVE_PATH = "save.json"
MENU_CURSOR_COLOR = "blue"

MAIN_MENU = ("Create a new list", "Select an existing list", "Save and quit")
LIST_OPERATION_MENU = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", "Return")

TERMINAL_WIDTH = os.get_terminal_size().columns
lists: list[ListElement] = []

if(os.path.exists(SAVE_PATH) and os.path.getsize(SAVE_PATH) > 0):
    with open(SAVE_PATH, "r", encoding="utf8") as file:
        saved_lists: list = json.load(file)

        for saved_list in saved_lists:
            new_list_element = ListElement(saved_list["name"], saved_list["content"])
            lists.append(new_list_element)

while(True):
    main_choice = console_menu.console_menu("Welcome to List Manager", MAIN_MENU, MENU_CURSOR_COLOR)

    if(main_choice == MAIN_MENU[0]):
        sys.stdout.write("\n")
        while(True):
            new_list_name = input(" Enter the name of the list to create : ")
            new_list_name = new_list_name.strip()
            sys.stdout.write("\n")

            if(len(new_list_name) < 3):
                sys.stdout.write("\033[K")
                sys.stdout.write(termcolor.colored(" List name cannot be shorter than 3 characters", "red"))
                sys.stdout.write("\033[F" * 2)
                sys.stdout.write("\033[K")
            elif(len(new_list_name) > 20):
                sys.stdout.write("\033[K")
                sys.stdout.write(termcolor.colored(" List name cannot be longer than 20 characters", "red"))
                sys.stdout.write("\033[F" * 2)
                sys.stdout.write("\033[K")
            elif(not new_list_name.replace(" ","").isalnum()):
                sys.stdout.write("\033[K")
                sys.stdout.write(termcolor.colored(" List name cannot contain special characters", "red"))
                sys.stdout.write("\033[F" * 2)
                sys.stdout.write("\033[K")
            elif(new_list_name in [list_element.name for list_element in lists]):
                sys.stdout.write("\033[K")
                sys.stdout.write((termcolor.colored(f" List '{new_list_name}' already exists", "red")))
                sys.stdout.write("\033[F" * 2)
                sys.stdout.write("\033[K")
            else:
                break

        new_list_element = ListElement(new_list_name)
        lists.append(new_list_element)

        print("\n " + termcolor.colored(f"List '{new_list_name}' has been successfully created \n", "light_magenta"))
        input(" Press enter to continue...")

    elif(main_choice == MAIN_MENU[1]):
        if(len(lists) > 0):
            manage_list_options = [list_element.name for list_element in lists] + ["Return"]
            selected_list = console_menu.console_menu("Select a list to manage", manage_list_options, MENU_CURSOR_COLOR)

            if(selected_list == manage_list_options[-1]):
                continue
            else:
                for l in lists:
                    if(l.name == selected_list):
                        selected_list = l
                        break

                title = [f"{l.name} content :\n"]
                list_content = [f"- {element}" for element in l.content]
                if(len(list_content) > 0):
                    longer_element = max(list_content, key=len)

                    for i in range (len(list_content)):
                        if(len(list_content[i]) < len(longer_element)):
                            list_content[i] = list_content[i].ljust(len(longer_element))

                    title = [f"{l.name} content :\n"] + list_content
                else:
                    title = selected_list.name + "\033[41m(empty)\033[0m"
                choice = console_menu.console_menu(title, LIST_OPERATION_MENU, MENU_CURSOR_COLOR)

                if(choice == LIST_OPERATION_MENU[0]):
                    pass
                elif(choice == LIST_OPERATION_MENU[1]):
                    element_to_rm = console_menu.console_menu("Choose an element to remove", [element for element in selected_list.content] + ["Cancel"], MENU_CURSOR_COLOR)

                    if(element_to_rm != "Cancel"):
                        sure_to_rm = console_menu.console_menu(f"Are you sure to remove '{element_to_rm}' from '{selected_list.name}' ?", ("Yes", "No"), "red")
                        if(sure_to_rm == "Yes"):
                            selected_list.remove(element_to_rm)
                if(choice == LIST_OPERATION_MENU[2]):
                    sure_to_clear = console_menu.console_menu(f"Are you sure to clear list '{selected_list.name}' ?", ("Yes", "No"), "red")

                    if(sure_to_clear == "Yes"):
                        selected_list.empty()
                elif(choice == LIST_OPERATION_MENU[3]):
                    sure_to_clear = console_menu.console_menu(f"Are you sure to delete list '{selected_list.name}' ?", ("Yes", "No"), "red")

                    if(sure_to_clear == "Yes"):
                        lists.remove(selected_list)

        else:
            print("\n " + termcolor.colored("You haven't created any list yet \n", "red"))
            input(" Press enter to continue...")

    elif(main_choice == MAIN_MENU[2]):
        list_to_save: list = []

        for list_element in lists:
            list_to_save.append({"name" : list_element.name, "content" : list_element.content})
        with open(SAVE_PATH, "w", encoding="utf8") as file:
            json.dump(list_to_save, file, indent=4)

        sys.exit()
