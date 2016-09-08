LOWER = 33
UPPER = 127


def main():
    letter_value = input("Enter a character: ")
    number_letter = ord(letter_value)
    print("The ASCII code for {} is {}".format(letter_value, number_letter))
    number_value = get_number(LOWER, UPPER)
    character_number = chr(number_value)
    print("The character for {} is {}".format(number_value, character_number))
    for x in range(LOWER, UPPER, 1):
        calc_character = chr(x)
        print("{:3} {:>6}".format(x, calc_character))


def get_number(lower, upper):
    user_num = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    while user_num < lower or user_num > upper:
        user_num = int(input("Enter a number between {} and {}: ".format(lower, upper)))
    return user_num


main()
