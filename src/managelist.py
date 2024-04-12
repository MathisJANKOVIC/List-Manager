from uimanager import UIManager
import console
import pythonclimenu

OPERATION_OPTIONS = ("Add a new element", "Remove an element", "Change name", "Clear the list", "Discard the list", "Return")

def main(uimanager: UIManager):
    initial_cursor_position = 0

    while(True):
        if(not uimanager.list_manager.has_lists()):
            console.move_cursor_down()
            console.write("It appears you have no lists, let's create a new one\n\n", UIManager.MESSAGE_COLORS["info"])
            console.prompt("Press enter to continue...")
            return

        select_list_options = uimanager.list_manager.get_list_names() + ["Return"]
        select_list_options_color = ["light_red" if option == "Return" else None for option in select_list_options]

        selected_option = pythonclimenu.menu(
            title = "Select a list to manage",
            cursor_color = "blue",
            options = select_list_options,
            options_color = select_list_options_color,
            initial_cursor_position = initial_cursor_position
        )

        if(selected_option != select_list_options[-1]):

            operation_to_perform = 0
            while(operation_to_perform != OPERATION_OPTIONS[-1]):
                content_list = [f"- {element}" for element in uimanager.list_manager.get_items(selected_option)]

                if(uimanager.list_manager.has_items(selected_option)):
                    longer_element = max(content_list, key=len)

                    # Adjust the margin to the longest element else use a default margin
                    if(len(longer_element) > UIManager.MIN_MARGIN_LIST_CONTENT):
                        for i, element in enumerate(content_list):
                            content_list[i] = element.ljust(len(longer_element))
                    else:
                        for i, element in enumerate(content_list):
                            content_list[i] = element.ljust(UIManager.MIN_MARGIN_LIST_CONTENT)

                    operation_title = [f"{selected_option} content :\n"] + content_list
                    operation_title_color = ["light_magenta" if line.startswith("-") else None for line in operation_title]
                else:
                    operation_title = selected_option + " (empty)"
                    operation_title_color = None

                operation_options_color = ["light_red" if option == "Return" else "light_yellow" for option in OPERATION_OPTIONS]

                operation_to_perform = pythonclimenu.menu(
                    title = operation_title,
                    options = OPERATION_OPTIONS,
                    cursor_color = "blue",
                    title_color = operation_title_color,
                    options_color = operation_options_color,
                    initial_cursor_position = operation_to_perform
                )

                if(operation_to_perform == OPERATION_OPTIONS[0]):
                    uimanager.add_element_to_list(selected_option)

                elif(operation_to_perform == OPERATION_OPTIONS[1]):
                    uimanager.remove_element_from_list(selected_option)

                elif(operation_to_perform == OPERATION_OPTIONS[2]):
                    selected_option = uimanager.rename_list(selected_option)

                elif(operation_to_perform == OPERATION_OPTIONS[3]):
                    uimanager.clear_list(selected_option)

                elif(operation_to_perform == OPERATION_OPTIONS[4]):
                    if(uimanager.delete_list(selected_option)):
                        break
                else:
                    initial_cursor_position = selected_option
        else:
            return
