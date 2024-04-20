from interface.menu import MainMenu, ListMenu, ManageListMenu, ConfirmDeleteListMenu, ConfirmClearListMenu, DeleteItemMenu
from interface.listui import ListUI
from listmanager import ListManager

SAVE_PATH = "save.json"

list_manager = ListManager()
list_manager.load(SAVE_PATH)

listui = ListUI(list_manager)

main_menu = MainMenu()
choice = main_menu.options[0]

while(choice != main_menu.options[-1]):
    choice = main_menu.display(init_cursor_position=choice)

    if(choice == main_menu.options[0]):
        listui.create_list()
    elif(choice == main_menu.options[1]):
        if(not list_manager.has_lists()):
            listui.handle_no_lists()
            continue

        selected_list = 0
        while(True):
            list_menu = ListMenu(list_manager.list_names)
            selected_list = list_menu.display(init_cursor_position=selected_list)

            if(selected_list == ListMenu.RETURN["label"]):
                break

            action = 0
            while(action != ManageListMenu.RETURN["label"]):
                manage_list_menu = ManageListMenu(selected_list, list_manager.items(selected_list))
                action = manage_list_menu.display(init_cursor_position=action)

                if(action == manage_list_menu.options[0]):
                    listui.add_element_to_list(selected_list)

                elif(action == manage_list_menu.options[1]):
                    delete_item_menu = DeleteItemMenu(selected_list, list_manager.items(selected_list))
                    item_to_delete = delete_item_menu.display()
                    if(item_to_delete != delete_item_menu.options[-1]):
                        confirm_menu = ConfirmDeleteListMenu(selected_list)
                        confirm = confirm_menu.display()
                        if(confirm == confirm_menu.options[0]):
                            list_manager.remove_item_from(selected_list, item_to_delete)

                elif(action == manage_list_menu.options[2]):
                    selected_list = listui.rename_list(selected_list)

                elif(action == manage_list_menu.options[3]):
                    confirm_menu = ConfirmClearListMenu(selected_list)
                    confirm = confirm_menu.display()

                    if(confirm == confirm_menu.options[0]):
                        list_manager.clear_list(selected_list)

                elif(action == manage_list_menu.options[4]):
                    confirm_menu = ConfirmDeleteListMenu(selected_list)
                    confirm = confirm_menu.display()

                    if(confirm == confirm_menu.options[0]):
                        list_manager.delete_list(selected_list)
                        selected_list = 0
                        break

listui.list_manager.save(SAVE_PATH)
