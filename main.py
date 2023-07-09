from list_manager import ListElement
import console_menu
import color
import json
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
        while(True):
            new_list_name = input("\n Enter the name of the list to create : ")
            new_list_name = new_list_name.strip()

            if(len(new_list_name) < 3):
                os.system("cls" if os.name == "nt" else "clear")
                print("\n " + color.red("List name cannot be shorter than 3 characters"))
            elif(len(new_list_name) > 20):
                os.system("cls" if os.name == "nt" else "clear")
                print("\n " + color.red("List name cannot be longer than 20 characters"))
            elif(not new_list_name.replace(" ","").isalnum()):
                os.system("cls" if os.name == "nt" else "clear")
                print("\n " + color.red("List name cannot contain special characters"))
            elif(new_list_name in [list_element.name for list_element in lists]):
                os.system("cls" if os.name == "nt" else "clear")
                print(("\n " + color.red(f"List '{new_list_name}' already exists")))
            else:
                break

        new_list_element = ListElement(new_list_name)
        lists.append(new_list_element)

        print("\n " + color.magenta(f"List '{new_list_name}' has been successfully created \n"))
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

                list_content = [" "*11 + color.magenta(f"- {element}") for element in l.content]
                longer_element = max(list_content, key=len)

                for i in range (len(list_content)):
                    if(len(list_content[i]) < len(longer_element)):
                        list_content[i] = list_content[i].ljust(len(longer_element))

                title = [f"{l.name} content :\n"] + list_content
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
            print("\n " + color.red("You haven't created any list yet \n"))
            input(" Press enter to continue...")

    elif(main_choice == MAIN_MENU[2]):
        list_to_save: list = []

        for list_element in lists:
            list_to_save.append({"name" : list_element.name, "content" : list_element.content})
        with open(SAVE_PATH, "w") as file:
            json.dump(list_to_save, file, indent=4)

        exit()
