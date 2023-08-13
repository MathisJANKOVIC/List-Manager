from ListElement import ListElement
import list_manager
import list_creation
import utils

import json
import sys
import os

SAVE_PATH = "save.json"
MAIN_MENU = ("Create a new list", "Select an existing list", "Save and quit")

lists: list[ListElement] = []

if(os.path.exists(SAVE_PATH) and os.path.getsize(SAVE_PATH) > 0):
    with open(SAVE_PATH, "r", encoding="utf8") as file:
        saved_lists: list = json.load(file)

        for saved_list in saved_lists:
            list_element = ListElement(saved_list["name"], saved_list["content"])
            lists.append(list_element)

while(True):
    choice = utils.menu("Welcome to List Manager", MAIN_MENU, utils.MENU_CURSOR_COLOR)

    if(choice == MAIN_MENU[0]):
        list_creation.main(lists)
    elif(choice == MAIN_MENU[1]):
        if(len(lists) > 0):
            list_manager.main(lists)
        else:
            print("\n\033[95m You haven't created any list yet \033[0m\n")
            input(" Press enter to continue...")
    elif(choice == MAIN_MENU[2]):
        lists_to_save: list = []

        for list_element in lists:
            lists_to_save.append({"name" : list_element.name, "content" : list_element.content})

        with open(SAVE_PATH, "w", encoding="utf8") as file:
            json.dump(lists_to_save, file, indent=4)

        sys.exit()
