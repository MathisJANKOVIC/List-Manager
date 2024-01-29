from ui_manager import UIManager
import pythonclimenu

OPERATION_OPTIONS = ("Add a new element", "Remove an element", "Change name", "Clear the list", "Discard the list", "Return")

def main(ui_manager: UIManager):
    initial_cursor_position = 0

    while(True):
        select_list_options = [list["name"] for list in ui_manager.list_manager.lists] + ["Return"]
        select_list_options_color = ["light_red" if option == "Return" else None for option in select_list_options]

        selected_option = pythonclimenu.menu(
            title = "Select a list to manage",
            cursor_color = "blue",
            options = select_list_options,
            options_color = select_list_options_color,
            initial_cursor_position = initial_cursor_position
        )

        if(selected_option != select_list_options[-1]):
            selected_list = ui_manager.list_manager.find(selected_option)

            operation_to_perform = 0
            while(operation_to_perform != OPERATION_OPTIONS[-1]):
                content_list = [f"- {element}" for element in selected_list['content']]

                if(len(content_list) > 0):
                    longer_element = max(content_list, key=len)

                    # Adjust the margin to the longest element else use a default margin
                    if(len(longer_element) > UIManager.LIST_CONTENT_MIN_MARGIN):
                        for i, element in enumerate(content_list):
                            content_list[i] = element.ljust(len(longer_element))
                    else:
                        for i, element in enumerate(content_list):
                            content_list[i] = element.ljust(UIManager.LIST_CONTENT_MIN_MARGIN)

                    operation_title = [f"{selected_list['name']} content :\n"] + content_list
                    operation_title_color = ["light_magenta" if line.startswith("-") else None for line in operation_title]
                else:
                    operation_title = selected_list['name'] + " (empty)"
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
                    ui_manager.add_element_to_list(selected_list['name'])

                elif(operation_to_perform == OPERATION_OPTIONS[1]):
                    ui_manager.remove_element_from_list(selected_list['name'])

                elif(operation_to_perform == OPERATION_OPTIONS[2]):
                    ui_manager.rename_list(selected_list['name'])
                    selected_option = selected_list['name']

                elif(operation_to_perform == OPERATION_OPTIONS[3]):
                    ui_manager.clear_list(selected_list['name'])

                elif(operation_to_perform == OPERATION_OPTIONS[4]):
                    if(ui_manager.delete_list(selected_list['name'])):
                        break
                else:
                    initial_cursor_position = selected_option
        else:
            return
