from list_controller import ListManager
import manage_list
import pythonclimenu

SAVE_PATH = "save.json"
MAIN_OPTIONS = ("Create a new list", "Select an existing list", "Save and quit")

list_manager = ListManager()
list_manager.load_data_from(SAVE_PATH)

choice = 0
while(True):
    choice = pythonclimenu.menu("Welcome to List Manager", MAIN_OPTIONS, "blue", initial_cursor_position=choice)

    if(choice == MAIN_OPTIONS[0]):
        list_manager.create_list()
    elif(choice == MAIN_OPTIONS[1]):
        if(len(list_manager.lists) > 0):
            manage_list.main(list_manager)
        else:
            print("\n\033[95m You haven't created any list yet \033[0m\n")
            input(" Press enter to continue...")
    else:
        list_manager.save(SAVE_PATH)
        exit()
