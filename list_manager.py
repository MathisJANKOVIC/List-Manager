from pathlib import Path
import json

class ListElement:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content

        # print(f"List '{self.name}\' has been successfuly created")

    def add(self, element):
        self.content.append(element)
        

    def delete(self, element):
        if(element in self.content):
            self.content.remove(element)
            print(f"\n\x1b[95m\"{element}\" has been successfully deleted from {self.name} \x1b[0m \n")
        else:
            print(f"\n\x1b[91m\"{element}\" is not part of {self.name} ⚠ \x1b[0m \n")

    def empty(self):
        if(len(self.content) > 0):
            self.content.clear()
            print(f"\n\x1b[95m{self.name} has been emptied successfully \x1b[0m \n")
        else:
            print(f"\n\x1b[95m{self.name} is already empty ⚠\x1b[0m \n")

    def save(self):
        save_path = Path.cwd() / "save.json"
        with open(save_path,"r") as f:
            json.dump(self.content,f, indent=2)

        # print(f"\n\x1b[95m{self.name} has been saved successfully \x1b[0m \n")

    def display(self):
        print(f"{self.name} :")
        for element in self.content:
            print(f"- {element}")
