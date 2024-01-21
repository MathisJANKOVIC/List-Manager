import pythonclimenu
import sys

OPERATION_OPTIONS = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", "Return")
CONFIRM_OPTIONS = ("Ok", "Cancel")
LIST_CONTENT_MIN_MARGIN = 11

def main(lists):
    initial_cursor_position = 0

    while(True):
        select_options = [list_element.name for list_element in lists] + ["Return"]
        select_options_color = ["light_red" if option == "Return" else "white" for option in select_options]

        selected_option_index = pythonclimenu.menu(
            title = "Select a list to manage",
            cursor_color = "blue",
            options = select_options,
            options_color = select_options_color,
            initial_cursor_position = initial_cursor_position
        )

        if(selected_option_index != select_options.index("Return")):
            for list_element in lists:
                if(list_element.name == select_options[selected_option_index]):
                    selected_list = list_element
                    break

            operation_to_perform_index = 0
            while(operation_to_perform_index != OPERATION_OPTIONS.index("Return")):
                list_content = [f"- {element}" for element in list_element.content]

                if(len(list_content) > 0):
                    longer_element = max(list_content, key=len)

                    # Adjust the margin to the longest element else use a default margin
                    if(len(longer_element) > LIST_CONTENT_MIN_MARGIN):
                        for i, element in enumerate(list_content):
                            list_content[i] = element.ljust(len(longer_element))
                    else:
                        for i, element in enumerate(list_content):
                            list_content[i] = element.ljust(LIST_CONTENT_MIN_MARGIN)

                    title_operation_menu = [f"{list_element.name} content :\n"] + list_content
                    title_operation_color = ["light_magenta" if line.startswith("-") else "white" for line in title_operation_menu]
                else:
                    title_operation_menu = selected_list.name + " (empty)"
                    title_operation_color = "white"

                operation_options_color = ["light_red" if option == "Return" else "light_yellow" for option in OPERATION_OPTIONS]

                operation_to_perform_index = pythonclimenu.menu(
                    title = title_operation_menu,
                    options = OPERATION_OPTIONS,
                    cursor_color = "blue",
                    title_color = title_operation_color,
                    options_color = operation_options_color,
                    initial_cursor_position = operation_to_perform_index
                )

                if(operation_to_perform_index == 0): # add new element
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

                elif(operation_to_perform_index == 1): # remove an element
                    if(len(selected_list.content) > 0):
                        rm_options = selected_list.content + ["Cancel"]

                        sure_to_rm = None
                        element_to_rm = 0

                        # While the user doesn't cancel the operation or doesn't select an element to remove
                        while(sure_to_rm != 0 and element_to_rm != rm_options.index("Cancel")):
                            rm_options_color = ["white" if option == "Cancel" else "light_magenta" for option in rm_options]

                            element_to_rm = pythonclimenu.menu(
                                title = "Choose an element to remove",
                                options = rm_options,
                                cursor_color = "blue",
                                options_color = rm_options_color,
                                initial_cursor_position = element_to_rm
                            )

                            if(element_to_rm != rm_options.index("Cancel")):
                                sure_to_rm = pythonclimenu.menu(
                                    title = f"You are about to remove '{rm_options[element_to_rm]}' from '{selected_list.name}'",
                                    options = CONFIRM_OPTIONS,
                                    cursor_color = "red",
                                    initial_cursor_position = -1
                                )

                                if(sure_to_rm == 0):
                                    selected_list.remove(rm_options[element_to_rm])
                    else:
                        print("\n\033[95m You cannot remove an element, the list is empty \033[0m\n")
                        input(" Press enter to continue...")

                elif(operation_to_perform_index == 2): # empty the list
                    if(len(selected_list.content) > 0):
                        sure_to_clear = pythonclimenu.menu(f"You are about to clear list '{selected_list.name}'", CONFIRM_OPTIONS, "red", initial_cursor_position=-1)

                        if(sure_to_clear == 0):
                            selected_list.clear()
                    else:
                        print("\n\033[95m The list is already empty \033[0m\n")
                        input(" Press enter to continue...")

                elif(operation_to_perform_index == 3): # delete the list
                    sure_to_delete = pythonclimenu.menu(f"You are about to delete list '{selected_list.name}'", CONFIRM_OPTIONS, "red", initial_cursor_position=-1)

                    if(sure_to_delete == 0):
                        lists.remove(selected_list)
                        initial_cursor_position = 0
                        break
                else:
                    initial_cursor_position = selected_option_index
        else:
            return
