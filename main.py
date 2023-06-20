import json
import os

print("\n\x1b[94mBienvenue dans votre liste de course 🍽 🛍\x1b[0m")
menu_choice = ["1","2","3","4","5"]
current_directory = os.getcwd()
save_path = os.path.join(current_directory,"liste_de_course_sauvegarde.json")

if(os.path.exists(save_path)):
    with open(save_path,"r") as f:
        liste_de_course = json.load(f)
else:
    liste_de_course = []

while True:
    user_choice = input("\nChoisissez parmi les 5 options suivantes: \n1. Ajouter un élément à la liste de course \n2. Retirer un élément de la liste de course \n3. Afficher la liste de course \n4. Vider la liste de course \n5. Quitter \n\nVeuillez saisir votre choix : ")

    while user_choice not in menu_choice:
        print("\n \x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nOption saisie invalide \x1b[0m")
        user_choice = input("Veuillez réesayer : ")

    if user_choice == "1":
        ajout = input("\nEntrez l'élement à ajouter à liste de course : ")
        liste_de_course.append(ajout)
        print(f"\n\x1b[95mL'élément \"{ajout}\" a bien été ajouté à la liste\x1b[0m")
    elif user_choice == "2":
        suppr = input("\nEntrez l'élement à supprimer de la liste de course : ")
        if suppr in liste_de_course:
            liste_de_course.remove(suppr)
            print(f"\n\x1b[95mL'élément \"{suppr}\" a bien été supprimé de la liste de course\x1b[0m")
        else:
            print("\n\x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nL'élement saisi n'est pas dans la liste et ne peut donc être supprimé\x1b[0m")
    elif user_choice == "3":
        if len(liste_de_course) == 0:
            print("\n\x1b[95mLa liste est vide, choisissez l'option 1 pour y ajouter des éléments\x1b[0m")
        else:
            print("\n\x1b[95m\x1b[4mContenu de la liste:\x1b[0m")
            for i, element in enumerate(liste_de_course):
                print(f"\x1b[95m{i+1}. {element}\x1b[0m")
    elif user_choice == "4":
        confirm = input("\n\x1b[91mEtes vous vraiment sûr de vouloir écraser votre liste de course ? (oui/non)\x1b[0m ")
        while not (confirm == "oui" or confirm == "Oui" or confirm == "Non" or confirm == "non" or confirm == "nn"):
            print("\n \x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nOption saisie invalide \x1b[0m")
            confirm = input("\nVeuillez répondre par oui ou par non : ")
        if confirm == "Oui" or confirm == "oui":
            if not len(liste_de_course) == 0:
                liste_de_course.clear()
                print("\n\x1b[95mLa liste a été vidée de son contenu avec succès\x1b[0m")
            else:
                print("\n\x1b[95mLa liste est déjà vide\x1b[0m")
        elif confirm == "Non" or confirm == "non" or confirm == "nn":
            continue
    elif user_choice == "5":
        confirm = input("\n\x1b[91mVous êtes sur le point de quitter, voulez vous sauvegarder ? (oui/non/annuler)\x1b[0m ")
        while not (confirm == "oui" or confirm == "Oui" or confirm == "Non" or confirm == "non" or confirm == "nn" or confirm == "annuler" or confirm == "Annuler"):
            print("\n\x1b[91m\x1b[1m⚠ ERREUR\x1b[0m\x1b[91m\nOption saisie invalide\x1b[0m")
            confirm = input("\nVeuillez répondre par oui ou par non : ")
        if confirm == "Oui" or confirm == "oui":
            with open(save_path,"w") as f:
                json.dump(liste_de_course,f, indent=2)
            print("\n\x1b[95mVotre liste de course a bien été sauvegardé\x1b[0m")
            print("\nA bientôt ! 😜 ")
            break
        elif confirm == "Non" or confirm == "non" or confirm == "nn":
            print("\nA bientôt ! 😜 ")
            break
        elif confirm == "annuler" or confirm == "Annuler":
            continue
