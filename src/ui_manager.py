from list_controller import ListManager
import pythonclimenu
import sys

class Console:
    ANSICOLORS: tuple = ("default", "red", "green", "yellow", "blue", "magenta", "cyan", "white")

    @staticmethod
    def eraseline():
        sys.stdout.write("\033[K")

    @staticmethod
    def move_cursor_up(line_number: int = 1):
        sys.stdout.write("\033[F" * line_number)

    @staticmethod
    def move_cursor_down(line_number: int = 1):
        sys.stdout.write("\n" * line_number)

    @staticmethod
    def write(text: str, color: str = None, margin: int = 1):
        text = " " * margin + text
        if(color is None):
            sys.stdout.write(text)
        else:
            if(color.startswith("light")):
                sys.stdout.write(f"\033[9{Console.ANSICOLORS.index(color.removeprefix('light_'))}m{text}\033[0m")
            else:
                sys.stdout.write(f"\033[3{Console.ANSICOLORS.index(color)}m{text}\033[0m")

    @staticmethod
    def prompt(text: str, color: str = None, margin: int = 1) -> str:
        Console.write(text + " ", color, margin)
        return input()

class UIManager:
    list_manager: ListManager
    LIST_CONTENT_MIN_MARGIN: int = 11
    CONFIRM_OPTIONS: tuple = ("Ok", "Cancel")

    def __init__(self, list_manager: ListManager):
        self.list_manager = list_manager

    def check_list_name_validity(self, list_name: str, rename: bool = False):
        same_list_name = self.list_manager.find(list_name)

        if(len(list_name) < 3):
            Console.write("List name cannot be shorter than 3 characters", "red")

        elif(len(list_name) > 20):
            Console.write("List name cannot be longer than 20 characters", "red")

        elif(not list_name.replace(" ","").replace("-","").replace("_","").isalnum()):
            Console.write("List name cannot contain special characters", "red")

        elif(same_list_name is not None):
            if(rename and same_list_name["name"] == list_name):
                Console.write("The new list name cannot be the same as the old", "red")
            else:
                Console.write(f"List '{list_name}' already exists", "red")
        else:
            return True

        return False

    def create_list(self):
        Console.move_cursor_down()

        while(True):
            list_name = Console.prompt("Enter the name of the list to create :")
            list_name = list_name.strip()

            Console.move_cursor_down()
            Console.eraseline() # deletes potencily previous message error

            if(self.check_list_name_validity(list_name)):
                break

            Console.move_cursor_up(2)
            Console.eraseline() # deletes user input

        self.list_manager.create(list_name)

        Console.write(f"List '{list_name}' has been successfully created \n\n", "light_magenta")
        Console.prompt("Press enter to continue...")

    def rename_list(self, list_name: str):
        Console.move_cursor_down()

        while(True):
            new_list_name = Console.prompt(f"Enter the new name for the list :")
            new_list_name = new_list_name.strip()

            Console.move_cursor_down()
            Console.eraseline()

            if(self.check_list_name_validity(new_list_name, rename=True)):
                break

            Console.move_cursor_up(2)
            Console.eraseline()

        self.list_manager.rename(list_name, new_list_name)

        Console.write(f"List '{list_name}' has been successfully renamed into '{new_list_name}' \n\n", "light_magenta")
        Console.prompt("Press enter to continue...")

    def add_element_to_list(self, list_name: str):
        Console.move_cursor_down()

        while(True):
            new_element = Console.prompt(f"Enter the element to add to list '{list_name}' :")
            new_element = new_element.strip()

            Console.move_cursor_down()
            Console.eraseline()

            if(len(new_element) == 0):
                Console.write("Elements cannot be empty", "red")

            elif(len(new_element) > 20):
                Console.write("Elements cannot be longer than 20 characters", "red")

            elif(self.list_manager.contains_element(list_name, new_element)):
                Console.write(f"Element '{new_element}' already exists in '{list_name}'", "red")
            else:
                break

            Console.move_cursor_up(2)
            Console.eraseline()

        self.list_manager.add_element(list_name, new_element)

    def remove_element_from_list(self, list_name: str):
        list = self.list_manager.find(list_name)

        if(len(list["content"]) > 0):
            rm_options = list["content"] + ["Cancel"]
            rm_options_color = [None if option == "Cancel" else "light_magenta" for option in rm_options]

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
                        self.list_manager.remove_element(list_name, element_to_rm)
        else:
            Console.write(f"You cannot remove an element, the list is empty \n\n", "light_magenta")
            Console.prompt("Press enter to continue...")

    def clear_list(self, list_name: str):
        list = self.list_manager.find(list_name)

        if(len(list["content"]) > 0):
            sure_to_clear = pythonclimenu.menu(f"You are about to clear list '{list_name}'", self.CONFIRM_OPTIONS, "red", initial_cursor_position=-1)
            if(sure_to_clear == self.CONFIRM_OPTIONS[0]):
                self.list_manager.clear(list_name)
        else:
            Console.write(f"\nThe list is already empty, you cannot clear it \n\n", "light_magenta")
            Console.prompt("Press enter to continue...")

    def delete_list(self, list_name: str):
        sure_to_delete = pythonclimenu.menu(f"You are about to delete list '{list_name}'", self.CONFIRM_OPTIONS, "red", initial_cursor_position=-1)

        if(sure_to_delete == self.CONFIRM_OPTIONS[0]):
            self.list_manager.delete(list_name)
            return True
        else:
            return False
