"""
Intermediate Exercise 1
CJ
"""

def main():
    numbers = []
    for x in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    print(("The first number is: {}".format(numbers[0])))
    print(("The lst number is: {}".format(numbers[-1])))
    print(("The smallest number is: {}".format(min(numbers))))
    print(("The biggest number is: {}".format(max(numbers))))
    print(("The average of the numbers are: {}".format(sum(numbers)/len(numbers))))

main()