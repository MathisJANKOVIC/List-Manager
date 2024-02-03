from list_manager import ListManager
from uimanager import UIManager
import manage_list

import pythonclimenu

SAVE_PATH = "save.json"
MAIN_OPTIONS = ("Create a new list", "Select an existing list", "Save and quit")

uimanager = UIManager(ListManager())
uimanager.list_manager.load_data(SAVE_PATH)

choice = MAIN_OPTIONS[0]
while(True):
    choice = pythonclimenu.menu("Welcome to List Manager", MAIN_OPTIONS, "blue", initial_cursor_position=choice)

    if(choice == MAIN_OPTIONS[0]):
        uimanager.create_list()
    elif(choice == MAIN_OPTIONS[1]):
        manage_list.main(uimanager)
    else:
        uimanager.list_manager.save(SAVE_PATH)
        exit()
