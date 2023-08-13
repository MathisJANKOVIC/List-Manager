from ListElement import ListElement
import sys

def main(lists):
    sys.stdout.write("\n")

    while(True):
        new_list_name = input(" Enter the name of the list to create : ")
        new_list_name = new_list_name.strip()

        if(len(new_list_name) < 3):
            sys.stdout.write("\n\033[31m List name cannot be shorter than 3 characters \033[0m")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

        elif(len(new_list_name) > 20):
            sys.stdout.write("\n\033[31m List name cannot be longer than 20 characters \033[0m")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

        elif(not new_list_name.replace(" ","").replace("-","").isalnum()):
            sys.stdout.write("\n\033[31m List name cannot contain special characters other than '-'\033[0m")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

        elif(new_list_name in [list_element.name for list_element in lists]):
            sys.stdout.write(f"\n\033[31m List '{new_list_name}' already exists \033[0m")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")
        else:
            break

    new_list_element = ListElement(new_list_name)
    lists.append(new_list_element)

    sys.stdout.write("\n")
    sys.stdout.write("\033[K")
    print(f"\033[95m List '{new_list_name}' has been successfully created \n\033[0m")
    input(" Press enter to continue... ")