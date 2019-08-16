import sys

_author_ = 'Hubert Stefanski'


def show_author():
    print("written by : " + _author_ + "\n")


def exit_system():
    show_author()
    sys.exit("Program has been run succesfully and terminated")


def print_name(first_name):
    if first_name == "Hubert":
        print("Witam " + first_name + "!\n")
        exit_system()
    else:
        print("Hello " + first_name + "!\n")
        exit_system()
    return


age = None
age = int(input("Age confirmation, how Old are you? "))

while age is not None:
    if age >= 18:

        print("you may proceed ")
        print_name(first_name=input("what's your name? "))
    else:
        print("sorry you may not proceed\n")
        exit_system()
        break
else:
    print("Sorry, you have provided a non-numeric or NULL value, please try again")
