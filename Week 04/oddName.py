"""
Chloe Jane Coleman
"""


def main():
    name = get_name()
    print(name[::2])


def get_name():
    name = input("Please enter your name")
    while name == "":
        name = input("Your name must have at least one character \nPlease enter your name")
    return name


main()
