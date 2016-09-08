"""
Do-from-scratch Exercise 1
CJ
"""

sentence = str(input("Please enter a string: "))
words = sentence.split(" ")
my_dict = {}
for word in words:
    if word in my_dict:
        my_dict[word] += 1
    else:
        my_dict[word] = 1

for word in my_dict:
    print(word, ":", my_dict[word])
