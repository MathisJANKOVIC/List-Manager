from list_manager import ListElement
import console_menu
from color import Color
import json
import os

SAVE_PATH = "save.json"

MAIN_MENU = ("Create a new list", "Select an existing list", "Save and quit")
ACTION_MENU = ("Add a new element", "Remove an element", "Empty the list", "Quit")

TERMINAL_WIDTH = os.get_terminal_size().columns

lists: list[ListElement] = []

if(os.path.exists(SAVE_PATH)):
    with open("save.json", "r") as file :
        json_lists = json.load(file)

        for json_list in json_lists:
            lists.append(ListElement(json_list["name"], json_list["content"]))

choice: str = None

while(choice != MAIN_MENU[2]):
    choice = console_menu.console_menu("Welcome to List Manager", MAIN_MENU, "blue")

    if(choice == MAIN_MENU[0]):
        while(True):
            new_list_name = input("\n Enter the name of the list to create : ")
            new_list_name = new_list_name.strip()

            if(len(new_list_name) < 3):
                print("\n " + Color.red("List name cannot be shorter than 3 characters"))
            elif(not new_list_name.replace(" ","").isalnum()):
                print("\n " + Color.red("List name cannot contain special characters"))
            elif(new_list_name in [list_element.name for list_element in lists]):
                print(("\n " + Color.red(f"List name '{new_list_name}' already exists")))
            else:
                break

        list_element = ListElement(new_list_name)
        lists.append(list_element)

        print("\n " + Color.magenta(f"List '{new_list_name}' has been successfully created"))
        input(" Press enter to contiune...")

    elif(choice == MAIN_MENU[1]):
        for i, list_element in enumerate(lists):
            print(f"{i+1}. {list_element.name}")

        list_choice = input("Choose a list : ")
        while(not list_choice.isdecimal() and list_choice not in list(range(len(lists)))):
            print("Please choose a correct option \n")
            list_choice = input("Choose a list : ")
        a = input("ok")

with open("save.json", "w") as file:
    lists = vars(lists)
    json.dump(lists, file, indent=4)
# print("\nChoisissez parmi les 5 options suivantes: \n")
#     print(" \n")

#     if(user_choice == "1"):
#         ajout = input("\nEntrez l'élement à ajouter à liste de course : ")
#         liste_de_course.append(ajout)
#         print(f"\n\x1b[95mL'élément \"{ajout}\" a bien été ajouté à la liste\x1b[0m")
#     elif(user_choice == "2"):
#         suppr = input("\nEntrez l'élement à supprimer de la liste de course : ")
#         if suppr in liste_de_course:
#             liste_de_course.remove(suppr)
#             print(f"\n\x1b[95mL'élément \"{suppr}\" a bien été supprimé de la liste de course\x1b[0m")
#         else:
#             print("\n\x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nL'élement saisi n'est pas dans la liste et ne peut donc être supprimé\x1b[0m")
#     elif user_choice == "3":
#         if len(liste_de_course) == 0:
#             print("\n\x1b[95mLa liste est vide, choisissez l'option 1 pour y ajouter des éléments\x1b[0m")
#         else:
#             print("\n\x1b[95m\x1b[4mContenu de la liste:\x1b[0m")
#             for i, element in enumerate(liste_de_course):
#                 print(f"\x1b[95m{i+1}. {element}\x1b[0m")
#     elif user_choice == "4":
#         confirm = input("\n\x1b[91mEtes vous vraiment sûr de vouloir écraser votre liste de course ? (oui/non)\x1b[0m ")
#         while not (confirm == "oui" or confirm == "Oui" or confirm == "Non" or confirm == "non" or confirm == "nn"):
#             print("\n \x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nOption saisie invalide \x1b[0m")
#             confirm = input("\nVeuillez répondre par oui ou par non : ")
#         if confirm == "Oui" or confirm == "oui":
#             if not len(liste_de_course) == 0:
#                 liste_de_course.clear()
#                 print("\n\x1b[95mLa liste a été vidée de son contenu avec succès\x1b[0m")
#             else:
#                 print("\n\x1b[95mLa liste est déjà vide\x1b[0m")
#         elif confirm == "Non" or confirm == "non" or confirm == "nn":
#             # continue
#     elif user_choice == "5":
#         confirm = input("\n\x1b[91mVous êtes sur le point de quitter, voulez vous sauvegarder ? (oui/non/annuler)\x1b[0m ")
#         while not (confirm == "oui" or confirm == "Oui" or confirm == "Non" or confirm == "non" or confirm == "nn" or confirm == "annuler" or confirm == "Annuler"):
#             print("\n\x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nOption saisie invalide\x1b[0m")
#             confirm = input("\nVeuillez répondre par oui ou par non : ")
#         if confirm == "Oui" or confirm == "oui":
#             with open(save_path,"w") as f:
#                 json.dump(liste_de_course,f, indent=2)
#             print("\n\x1b[95mVotre liste de course a bien été sauvegardé\x1b[0m")
#             print("\nA bientôt ! 😜 ")
#             break
#         elif confirm == "Non" or confirm == "non" or confirm == "nn":
#             print("\nA bientôt ! 😜 ")
#             break
#         elif confirm == "annuler" or confirm == "Annuler":
#             continue