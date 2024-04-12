from uimanager import UIManager
import pythonclimenu
import managelist

SAVE_PATH = "save.json"
MAIN_OPTIONS = ("Create a new list", "Select an existing list", "Save and quit")

ui_manager = UIManager()
ui_manager.list_manager.load(SAVE_PATH)

choice = MAIN_OPTIONS[0]
while(True):
    choice = pythonclimenu.menu("Welcome to List Manager", MAIN_OPTIONS, "blue", initial_cursor_position=choice)

    if(choice == MAIN_OPTIONS[0]):
        ui_manager.create_list()
    elif(choice == MAIN_OPTIONS[1]):
        managelist.main(ui_manager)
    else:
        ui_manager.list_manager.save(SAVE_PATH)
        quit()
