"""
Intermediate Exercise 2
CJ
"""

def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_username = str(input("Please enter your username: "))
    if user_username in usernames:
        print("Access Granted")
    else:
        print("Access Denied")

main()