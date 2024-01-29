from list_controller import ListManager
from ui_manager import UIManager
import manage_list

import pythonclimenu

SAVE_PATH = "save.json"
MAIN_OPTIONS = ("Create a new list", "Select an existing list", "Save and quit")

ui_manager = UIManager(ListManager())
ui_manager.list_manager.load_data(SAVE_PATH)

choice = MAIN_OPTIONS[0]
while(True):
    choice = pythonclimenu.menu("Welcome to List Manager", MAIN_OPTIONS, "blue", initial_cursor_position=choice)

    if(choice == MAIN_OPTIONS[0]):
        ui_manager.create_list()
    elif(choice == MAIN_OPTIONS[1]):
        manage_list.main(ui_manager)
    else:
        ui_manager.list_manager.save(SAVE_PATH)
        exit()
