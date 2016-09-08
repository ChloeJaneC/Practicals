"""
Do from Scratch Exercise 1
CJ
"""
import random

QUICK_LENGTH = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    picks = []
    number_picks = int(input("How many quick picks? "))
    for i in range(1, number_picks + 1):
        rand_pick = []
        for x in range(QUICK_LENGTH):
            random_number = random.randrange(MINIMUM, MAXIMUM)
            rand_pick.append(random_number)
        picks.append(sorted(rand_pick))
    print(picks)


main()
