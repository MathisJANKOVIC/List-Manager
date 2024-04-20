from abc import ABC, abstractmethod
import pythonclimenu

from listmanager import ListManager

class Menu(ABC):
    CURSOR_COLOR = "blue"
    RETURN = {"label": "Return", "color": "light_red"}

    @property
    @abstractmethod
    def options(self) -> list[str]: ...

    @abstractmethod
    def display(self, init_cursor_position: int | str = 0) -> str: ...

class MainMenu(Menu):
    _OPTIONS = ("Create a new list", "Select a list", "Save and quit")

    @property
    def options(self) -> list[str]:
        return list(self._OPTIONS)

    def display(self, init_cursor_position: int | str = 0) -> str:
        return pythonclimenu.menu(
            title="Welcome to List Manager",
            cursor_color=Menu.CURSOR_COLOR,
            options=self.options,
            initial_cursor_position=init_cursor_position
        )

class ListMenu(Menu):
    _options: list[str]

    def __init__(self, list_names: list[str]) -> None:
        self._options = list_names + [Menu.RETURN["label"]]

    @property
    def options(self) -> list[str]:
        return self._options

    def display(self, init_cursor_position: int | str = 0) -> str:
        return pythonclimenu.menu(
            title="Select a list to manage",
            cursor_color=Menu.CURSOR_COLOR,
            options=self.options,
            options_color=[Menu.RETURN["color"] if option == Menu.RETURN["label"] else None for option in self.options],
            initial_cursor_position=init_cursor_position
        )

class ManageListMenu(Menu):
    _MIN_MARGIN_LIST_CONTENT = 11
    _OPTIONS = ("Add a new element", "Remove an element", "Change name", "Clear the list", "Discard the list", Menu.RETURN["label"])
    _COLORS = {"items": "light_magenta", "actions": "light_yellow"}

    _title: str | list[str]
    _title_colors: list[str] | None
    _option_colors: list[str]

    def __init__(self, list_name: str, items: list[str]) -> None:

        if(len(items) == 0):
            self._title = f"{list_name} (empty)"
            self._title_colors = None
        else:
            content_list = [f"- {item}" for item in items]
            longer_element = max(content_list, key=len)

            # Adjust the margin to the longest element else use a default margin
            if(len(longer_element) > self._MIN_MARGIN_LIST_CONTENT):
                for i, element in enumerate(content_list):
                    content_list[i] = element.ljust(len(longer_element))
            else:
                for i, element in enumerate(content_list):
                    content_list[i] = element.ljust(self._MIN_MARGIN_LIST_CONTENT)

            self._title = [f"{list_name} content :\n"] + content_list
            self._title_colors = [self._COLORS["items"] if line.startswith("-") else None for line in self._title]

        self._option_colors = [
            Menu.RETURN["color"] if option == Menu.RETURN["label"] else self._COLORS["actions"] for option in self._OPTIONS
        ]

    @property
    def options(self) -> list[str]:
        return list(self._OPTIONS)

    def display(self, init_cursor_position: int | str = 0) -> str:
        return pythonclimenu.menu(
            title=self._title,
            options=self.options,
            cursor_color=Menu.CURSOR_COLOR,
            title_color=self._title_colors,
            options_color=self._option_colors,
            initial_cursor_position=init_cursor_position
        )

class ConfirmMenu(Menu):
    _CURSOR_COLOR = "red"
    _OPTIONS = ("Ok", "Cancel")
    _title: str

    def __init__(self, message: str) -> None:
        self._title = message

    @property
    def options(self) -> list[str]:
        return list(self._OPTIONS)

    def display(self, init_cursor_position: int | str = 0) -> str:
        return pythonclimenu.menu(
            title=self._title,
            options=self.options,
            cursor_color=self._CURSOR_COLOR,
            initial_cursor_position=init_cursor_position
        )

class ConfirmClearListMenu(ConfirmMenu):
    def __init__(self, list_name: str) -> None:
        super().__init__(f"Are you sure you want to clear '{list_name}' ?")

class ConfirmDeleteListMenu(ConfirmMenu):
    def __init__(self, list_name: str) -> None:
        super().__init__(f"Are you sure you want to delete '{list_name}' ?")

class ConfirmDeleteItemMenu(ConfirmMenu):
    def __init__(self, list_name: str, item_name: str) -> None:
        super().__init__(f"Are you sure you want to delete '{item_name}' from {list_name} ?")

class DeleteItemMenu(Menu):
    list_name: str
    _options: list[str]
    options_color: list[str]
    LIST_COLORS = "light_magenta"

    def __init__(self, list_name: str, items: list[str]) -> None:
        self.list_name = list_name
        self._options = items + [Menu.RETURN["label"]]

    @property
    def options(self) -> list[str]:
        return self._options

    def display(self, init_cursor_position: int | str = 0) -> str:
        return pythonclimenu.menu(
            title=f"Select an item to delete from '{self.list_name}'",
            options=self.options,
            cursor_color=Menu.CURSOR_COLOR,
            options_color=[None if option == Menu.RETURN["label"] else self.LIST_COLORS for option in self.options],
            initial_cursor_position=init_cursor_position
        )
