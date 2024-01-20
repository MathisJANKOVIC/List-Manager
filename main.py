from list_element import ListElement
import create_list
import manage_list

import pythonclimenu
import json
import sys
import os

SAVE_PATH = "save.json"
MAIN_MENU = ("Create a new list", "Select an existing list", "Save and quit")

lists: list[ListElement] = []

if(os.path.exists(SAVE_PATH) and os.path.getsize(SAVE_PATH) > 0):
    with open(SAVE_PATH, "r", encoding="utf-8") as save_file:
        saved_lists: list = json.load(save_file)

        for saved_list in saved_lists:
            list_element = ListElement(saved_list["name"], saved_list["content"])
            lists.append(list_element)

choice = 0
while(True):
    choice = pythonclimenu.menu("Welcome to List Manager", MAIN_MENU, "blue", initial_cursor_position=choice)

    if(choice == 0):
        create_list.main(lists)
    elif(choice == 1):
        if(len(lists) > 0):
            manage_list.main(lists)
        else:
            print("\n\033[95m You haven't created any list yet \033[0m\n")
            input(" Press enter to continue...")
    else:
        lists_to_save: list = []

        for list_element in lists:
            lists_to_save.append({"name" : list_element.name, "content" : list_element.content})

        with open(SAVE_PATH, "w", encoding="utf-8") as save_file:
            json.dump(lists_to_save, save_file, indent=4)

        sys.exit()
