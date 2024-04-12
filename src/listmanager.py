import json
import os

class ListManagerError(Exception): pass

class ListNotFoundError(ListManagerError): pass

class ItemNotFoundError(ListManagerError): pass

class NamingError(ListManagerError): pass

class TooShortNameError(NamingError): pass

class TooLongNameError(NamingError): pass

class InvalidNameError(NamingError): pass

class AlreadyTakenNameError(NamingError): pass

class ListManager:
    _lists: dict[str, list[str]]
    MIN_NAME_LENGTH = 1
    MAX_NAME_LENGTH = 20

    def __init__(self) -> None:
        self._lists = {}

    def _ensure_list_exists(self, list_name: str) -> None:
        if(list_name not in self._lists.keys()):
            raise ListNotFoundError

    def _check_list_name(self, name: str) -> None:
        if(name in self._lists.keys()):
            raise AlreadyTakenNameError
        if(len(name) < self.MIN_NAME_LENGTH):
            raise TooShortNameError
        if(len(name) > self.MAX_NAME_LENGTH):
            raise TooLongNameError
        if(not name.replace(" ","").replace("-","").replace("_","").replace("'","").isalnum()): # todo
            raise InvalidNameError

    def has_lists(self) -> bool:
        return len(self._lists) > 0

    def get_list_names(self) -> list[str]:
        return list(self._lists.keys())

    def create_list(self, name: str) -> None:
        self._check_list_name(name)
        self._lists[name] = []

    def rename_list(self, name: str, new_name: str) -> None:
        self._ensure_list_exists(name)
        self._check_list_name(new_name)
        self._lists[new_name] = self._lists.pop(name)

    def clear_list(self, name: str) -> None:
        self._ensure_list_exists(name)
        self._lists[name].clear()

    def delete_list(self, name: str) -> None:
        self._ensure_list_exists(name)
        del self._lists[name]

    def _contains_item(self, list_name: str, item: str) -> bool:
        return item in self._lists[list_name]

    def _ensure_item_exists(self, list_name: str, item: str) -> None:
        if(not self._contains_item(list_name, item)):
            raise ItemNotFoundError

    def _check_item(self, item: str, list_name: str) -> None:
        if(self._contains_item(list_name, item)):
            raise AlreadyTakenNameError
        if(len(item) < self.MIN_NAME_LENGTH):
            raise TooShortNameError
        if(len(item) > self.MAX_NAME_LENGTH):
            raise TooLongNameError
        if(item.startswith("'") or item.endswith("'")): # todo
            raise InvalidNameError

    def has_items(self, list_name: str) -> bool:
        self._ensure_list_exists(list_name)
        return len(self._lists[list_name]) > 0

    def get_items(self, list_name: str) -> list[str]:
        self._ensure_list_exists(list_name)
        return self._lists[list_name]

    def add_item(self, list_name: str, item: str) -> None:
        self._ensure_list_exists(list_name)
        self._check_item(item, list_name)
        self._lists[list_name].append(item)

    def remove_item(self, list_name: str, item: str) -> None:
        self._ensure_list_exists(list_name)
        self._ensure_item_exists(list_name, item)
        self._lists[list_name].remove(item)

    def load(self, file_path: str) -> None:
        if(os.path.exists(file_path) and os.path.getsize(file_path) > 0):
            with open(file_path, "r", encoding="utf-8") as file:
                self._lists = json.load(file)

    def save(self, file_path: str) -> None:
        with open(file_path, "w", encoding="utf-8") as save_file:
            json.dump(self._lists, save_file, indent=4)
