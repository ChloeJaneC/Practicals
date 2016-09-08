LOWER = 33
UPPER = 127
letter_value = input("Enter a character: ")
number_letter = ord(letter_value)
print("The ASCII code for {} is {}".format(letter_value, number_letter))
number_value = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
while number_value < LOWER or number_value > UPPER:
    number_value = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))
character_number = chr(number_value)
print("The character for {} is {}".format(number_value, character_number))
for x in range(33, 127, 1):
    calc_character = chr(x)
    if x<=99:
        print("{} {:>6}".format(x, calc_character))
    else:
        print("{}{:>6}".format(x, calc_character))