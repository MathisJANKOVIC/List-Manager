from listmanager import ListManager, AlreadyTakenNameError, TooShortNameError, TooLongNameError, InvalidNameError
from . import console

class ListUI:
    list_manager: ListManager
    MESSAGE_COLORS = {"info": "light_magenta", "error": "red"}

    def __init__(self, list_manager: ListManager) -> None:
        self.list_manager = list_manager

    def create_list(self) -> None:
        console.move_cursor_down()
        while(True):
            try:
                list_name = console.prompt("Enter the name of the list to create :").strip()
            except KeyboardInterrupt:
                return

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
                return list_name

            console.move_cursor_down()
            console.clear_line() # deletes potencily previous message error

            try:
                self.list_manager.rename_list(list_name, new_list_name)
            except AlreadyTakenNameError:
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

    def add_element_to_list(self, list_name: str) -> None:
        console.move_cursor_down()
        while(True):
            try:
                new_element = console.prompt(f"Enter the element to add to list '{list_name}' :").strip()
            except KeyboardInterrupt:
                return

            console.move_cursor_down()
            console.clear_line()

            try:
                self.list_manager.add_item_to(list_name, new_element)
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


    def handle_no_lists(self) -> None:
        console.move_cursor_down()
        console.write("No lists found, please create one first \n", self.MESSAGE_COLORS["info"])
        console.prompt("Press enter to continue...")