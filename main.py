from list_controller import ListManager
import manage_list
import pythonclimenu

SAVE_PATH = "save.json"

list_manager = ListManager()
list_manager.load_data_from(SAVE_PATH)

choice = 0
while(True):
    choice = pythonclimenu.menu(
        title = "Welcome to List Manager",
        options = ("Create a new list", "Select an existing list", "Save and quit"),
        cursor_color = "blue",
        initial_cursor_position = choice
    )

    if(choice == 0):
        list_manager.create_list()
    elif(choice == 1):
        if(len(list_manager.lists) > 0):
            manage_list.main(list_manager)
        else:
            print("\n\033[95m You haven't created any list yet \033[0m\n")
            input(" Press enter to continue...")
    else:
        list_manager.save(SAVE_PATH)
        exit()
