import pythonclimenu
import json
import sys
import os

class ListElement:
    name: str
    content: list[str]

    def __init__(self, name, content=[]):
        self.name = name
        self.content = content

    @property
    def dict(self):
        return {"name" : self.name, "content" : self.content}

    def contains(self, element):
        return element in self.content

    def add(self, element):
        self.content.append(element)

    def remove(self, element):
        self.content.remove(element)

    def clear(self):
        self.content.clear()

class ListManager:
    lists: list[ListElement]

    def __init__(self, lists: list[ListElement] = []):
        self.lists = lists

    def find(self, list_name: str):
        for list_element in self.lists:
            if(list_element.name == list_name):
                return list_element
        return None

    def load_data_from(self, file_path: str):
        if(os.path.exists(file_path) and os.path.getsize(file_path) > 0):
            with open(file_path, "r", encoding="utf-8") as save_file:
                saved_lists: list = json.load(save_file)

            for saved_list in saved_lists:
                list_element = ListElement(saved_list["name"], saved_list["content"])
                self.lists.append(list_element)

    def save(self, file_path: str):
        lists_to_save: list[dict] = []

        for list_element in self.lists:
            lists_to_save.append(list_element.dict)

        with open(file_path, "w", encoding="utf-8") as save_file:
            json.dump(lists_to_save, save_file, indent=4)

    def create_list(self):
        sys.stdout.write("\n")

        while(True):
            new_list_name = input(" Enter the name of the list to create : ").strip()
            new_list_name = new_list_name

            sys.stdout.write("\n")
            sys.stdout.write("\033[K") # deletes potencily previous message error

            if(len(new_list_name) < 3):
                sys.stdout.write("\033[31m List name cannot be shorter than 3 characters \033[0m")

            elif(len(new_list_name) > 20):
                sys.stdout.write("\033[31m List name cannot be longer than 20 characters \033[0m")

            elif(not new_list_name.replace(" ","").replace("-","").replace("_","").isalnum()):
                sys.stdout.write("\033[31m List name cannot contain special characters\033[0m")

            elif(self.find(new_list_name) is not None):
                sys.stdout.write(f"\033[31m List '{new_list_name}' already exists \033[0m")
            else:
                break

            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K") # deletes user input

        self.lists.append(ListElement(new_list_name))

        print(f"\033[95m List '{new_list_name}' has been successfully created \n\033[0m")
        input(" Press enter to continue... ")

    def add_element_to(self, list_name: str):
        sys.stdout.write("\n")
        list_element: ListElement = self.find(list_name)

        while(True):
            new_element = input(f" Enter the element to add to list '{list_name}' : ")
            new_element = new_element.strip()

            sys.stdout.write("\n")
            sys.stdout.write("\033[K") # deletes potencily previous message error

            if(len(new_element) == 0):
                sys.stdout.write("\033[31m Elements cannot be empty \033[0m")

            elif(len(new_element) > 20):
                sys.stdout.write("\033[31m Elements cannot be longer than 20 characters \033[0m")

            elif(not new_element.replace(" ","").replace("-","").replace("_","").isalnum()):
                sys.stdout.write("\033[31m Elements cannot contain special characters \033[0m")

            elif(list_element.contains(new_element)):
                sys.stdout.write(f"\033[31m Element '{new_element}' already exists in '{list_name}'\033[0m")
            else:
                break

            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

        list_element.add(new_element)

    def remove_element_from(self, list_name: str):
        list_element: ListElement = self.find(list_name)

        if(len(list_element.content) > 0):
            rm_options = list_element.content + ["Cancel"]
            rm_options_color = ["white" if option == "Cancel" else "light_magenta" for option in rm_options]

            sure_to_rm = element_to_rm = None
            # While the user doesn't cancel the operation or doesn't select an element to remove
            while(sure_to_rm != 0 and element_to_rm != rm_options.index("Cancel")):
                element_to_rm = pythonclimenu.menu(
                    title = "Choose an element to remove",
                    options = rm_options,
                    cursor_color = "blue",
                    options_color = rm_options_color,
                    initial_cursor_position = element_to_rm
                )

                if(element_to_rm != rm_options.index("Cancel")):
                    sure_to_rm = pythonclimenu.menu(
                        title = f"You are about to remove '{rm_options[element_to_rm]}' from '{list_element.name}'",
                        options = ("Ok", "Cancel"),
                        cursor_color = "red",
                        initial_cursor_position = -1
                    )

                    if(sure_to_rm == 0):
                        list_element.remove(rm_options[element_to_rm])
        else:
            print("\n\033[95m You cannot remove an element, the list is empty \033[0m\n")
            input(" Press enter to continue...")

    def clear(self, list_name: str):
        list_element: ListElement = self.find(list_name)

        if(len(list_element.content) > 0):
            sure_to_clear = pythonclimenu.menu(f"You are about to clear list '{list_name}'", ("Ok", "Cancel"), "red", initial_cursor_position=-1)
            if(sure_to_clear == 0):
                list_element.clear()
        else:
            print("\n\033[95m The list is already empty \033[0m\n")
            input(" Press enter to continue...")
