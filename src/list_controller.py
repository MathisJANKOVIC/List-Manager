import json
import os
import re

class ListManager:
    lists: list[dict[str, list[str]]]

    def __init__(self):
        self.lists = []

    def find(self, list_name: str):
        for list in self.lists:
            if(list["name"] == list_name):
                return list
        return None

    def contains_list(self):
        return len(self.lists) > 0

    def contains_element(self, list_name: str, element: str):
        return element in self.find(list_name)["content"]

    def create(self, list_name: str):
        self.lists.append({"name": list_name, "content": []})

    def add_element(self, list_name: str, element: str):
        self.find(list_name)["content"].append(element)

    def rename(self, list_name: str, new_list_name: str):
        self.find(list_name)["name"] = new_list_name

    def remove_element(self, list_name: str, element: str):
        self.find(list_name)["content"].remove(element)

    def clear(self, list_name: str):
        self.find(list_name)["content"].clear()

    def delete(self, list_name: str):
        self.lists.remove(self.find(list_name))

    def load_data(self, file_path: str):
        if(os.path.exists(file_path) and os.path.getsize(file_path) > 0):
            with open(file_path, "r", encoding="utf-8") as file:
                self.lists = json.load(file)

    def save(self, file_path: str):
        with open(file_path, "w", encoding="utf-8") as save_file:
            json.dump(self.lists, save_file, indent=4)
