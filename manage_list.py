from list_controller import ListManager
import pythonclimenu

OPERATION_OPTIONS = ("Add a new element", "Remove an element", "Empty the list", "Delete the list", "Return")
CONFIRM_OPTIONS = ("Ok", "Cancel")
LIST_CONTENT_MIN_MARGIN = 11

def main(list_manager: ListManager):
    initial_cursor_position = 0

    while(True):
        select_options = [list_element.name for list_element in list_manager.lists] + ["Return"]
        select_options_color = ["light_red" if option == "Return" else "white" for option in select_options]

        selected_option_index = pythonclimenu.menu(
            title = "Select a list to manage",
            cursor_color = "blue",
            options = select_options,
            options_color = select_options_color,
            initial_cursor_position = initial_cursor_position
        )

        if(selected_option_index != select_options.index("Return")):
            for list_element in list_manager.lists:
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
                    list_manager.add_element_to(selected_list.name)

                elif(operation_to_perform_index == 1): # remove an element
                    list_manager.remove_element_from(selected_list.name)

                elif(operation_to_perform_index == 2): # clear the list
                    list_manager.clear(selected_list.name)

                elif(operation_to_perform_index == 3): # delete the list
                    sure_to_delete = pythonclimenu.menu(f"You are about to delete list '{selected_list.name}'", CONFIRM_OPTIONS, "red", initial_cursor_position=-1)

                    if(sure_to_delete == 0):
                        list_manager.lists.remove(selected_list)
                        initial_cursor_position = 0
                        break
                else:
                    initial_cursor_position = selected_option_index
        else:
            return
