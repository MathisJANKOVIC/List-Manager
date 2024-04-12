from listmanager import ListManager, AlreadyTakenNameError, TooShortNameError, TooLongNameError, InvalidNameError
import console

import pythonclimenu

class UIManager:
    list_manager: ListManager
    MESSAGE_COLORS = {"info": "light_magenta", "error": "red"}
    MIN_MARGIN_LIST_CONTENT = 11
    CONFIRM_OPTIONS = ("Ok", "Cancel")

    def __init__(self) -> None:
        self.list_manager = ListManager()

    def create_list(self) -> None:
        console.move_cursor_down()
        while(True):
            list_name = console.prompt("Enter the name of the list to create :")
            list_name = list_name.strip()

            console.move_cursor_down()
            console.clear_line() # deletes potencily previous message error

            try:
                self.list_manager.create_list(list_name)
            except AlreadyTakenNameError:
                console.write(f"List '{list_name}' already exists, please choose another name ", self.MESSAGE_COLORS["error"])
            except TooShortNameError:
                console.write(f"List name must be at least {ListManager.MIN_NAME_LENGTH} character long ", self.MESSAGE_COLORS["error"])
            except TooLongNameError:
                console.write(f"List name must be at most {ListManager.MAX_NAME_LENGTH} characters long ", self.MESSAGE_COLORS["error"])
            except InvalidNameError:
                console.write("List name must be alphanumeric ", self.MESSAGE_COLORS["error"])
            else:
                console.write(f"List '{list_name}' has been successfully created \n\n", self.MESSAGE_COLORS["info"])
                console.prompt("Press enter to continue...")
                return

            console.move_cursor_up(lines=2)
            console.clear_line() # deletes user input

    def rename_list(self, list_name: str) -> str:
        console.move_cursor_down()
        while(True):
            try:
                new_list_name = console.prompt("Enter the name of the list to rename :").strip()
            except KeyboardInterrupt:
                console.move_cursor_down()
                console.write("Operation canceled \n\n", self.MESSAGE_COLORS["info"])
                console.prompt("Press enter to continue...")
                return

            console.move_cursor_down()
            console.clear_line() # deletes potencily previous message error

            try:
                self.list_manager.rename_list(list_name, new_list_name)
            except AlreadyTakenNameError as e:
                console.write(f"List '{new_list_name}' already exists, please choose another name ", self.MESSAGE_COLORS["error"])
            except TooShortNameError:
                console.write(f"List name must be at least {ListManager.MIN_NAME_LENGTH} character long ", self.MESSAGE_COLORS["error"])
            except TooLongNameError:
                console.write(f"List name must be at most {ListManager.MAX_NAME_LENGTH} characters long ", self.MESSAGE_COLORS["error"])
            except InvalidNameError:
                console.write("List name must be alphanumeric ", self.MESSAGE_COLORS["error"])
            else:
                console.write(f"List '{list_name}' has been successfully created \n\n", self.MESSAGE_COLORS["info"])
                console.prompt("Press enter to continue...")
                return new_list_name

            console.move_cursor_up(lines=2)
            console.clear_line() # deletes user input

    def add_element_to_list(self, list_name: str):
        console.move_cursor_down()
        while(True):
            new_element = console.prompt(f"Enter the element to add to list '{list_name}' :")
            new_element = new_element.strip()

            console.move_cursor_down()
            console.clear_line()

            try:
                self.list_manager.add_item(list_name, new_element)
            except AlreadyTakenNameError:
                console.write(f"Element '{new_element}' already exists in list '{list_name}', please choose another name ", self.MESSAGE_COLORS["error"])
            except TooShortNameError:
                console.write(f"Element name must be at least {ListManager.MIN_NAME_LENGTH} character long ", self.MESSAGE_COLORS["error"])
            except TooLongNameError:
                console.write(f"Element name must be at most {ListManager.MAX_NAME_LENGTH} characters long ", self.MESSAGE_COLORS["error"])
            except InvalidNameError:
                console.write("Element name must be alphanumeric ", self.MESSAGE_COLORS["error"])
            else:
                console.write(f"Element '{new_element}' has been successfully added to list '{list_name}' \n\n", self.MESSAGE_COLORS["info"])
                console.prompt("Press enter to continue...")
                return

            console.move_cursor_up(lines=2)
            console.clear_line()

    def remove_element_from_list(self, list_name: str):
        if(not self.list_manager.has_items(list_name)):
            console.move_cursor_down()
            console.write(f"You cannot remove an element, the list is empty \n\n", self.MESSAGE_COLORS["info"])
            console.prompt("Press enter to continue...")
            return

        rm_options = self.list_manager.get_items(list_name) + ["Cancel"]
        rm_options_color = [None if option == "Cancel" else self.MESSAGE_COLORS["info"] for option in rm_options]

        sure_to_rm = None
        element_to_rm = 0
        # While the user doesn't cancel the operation or doesn't select an element to remove
        while(sure_to_rm != self.CONFIRM_OPTIONS[0] and element_to_rm != rm_options[-1]):
            element_to_rm = pythonclimenu.menu(
                title = "Choose an element to remove",
                options = rm_options,
                cursor_color = "blue",
                options_color = rm_options_color,
                initial_cursor_position = element_to_rm
            )

            if(element_to_rm != rm_options[-1]):
                sure_to_rm = pythonclimenu.menu(
                    title = f"You are about to remove '{element_to_rm}' from '{list_name}'",
                    options = self.CONFIRM_OPTIONS,
                    cursor_color = "red",
                    initial_cursor_position = -1
                )

                if(sure_to_rm == self.CONFIRM_OPTIONS[0]):
                    self.list_manager.remove_item(list_name, element_to_rm)

    def clear_list(self, list_name: str):
        if(self.list_manager.has_items(list_name)):
            sure_to_clear = pythonclimenu.menu(f"You are about to clear list '{list_name}'", self.CONFIRM_OPTIONS, "red", initial_cursor_position=-1)
            if(sure_to_clear == self.CONFIRM_OPTIONS[0]):
                self.list_manager.clear_list(list_name)
        else:
            console.move_cursor_down()
            console.write(f"The list is already empty, you cannot clear it \n\n", self.MESSAGE_COLORS["info"])
            console.prompt("Press enter to continue...")

    def delete_list(self, list_name: str):
        sure_to_delete = pythonclimenu.menu(f"You are about to delete list '{list_name}'", self.CONFIRM_OPTIONS, "red", initial_cursor_position=-1)

        if(sure_to_delete == self.CONFIRM_OPTIONS[0]):
            self.list_manager.delete_list(list_name)
            return True
        else:
            return False
