try:  # 'use ctrl + alt + l' to format the file (like when you copy it from a PDF)
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:  # Q1 ValueError occurs when you enter a str
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # Q2 ZeroDivisionError will occur when the denominator is 0 as it results in an unknown
    print("Cannot divide by zero!") # Q3 Yes the program would have to check to ensure the denominator was not 0
