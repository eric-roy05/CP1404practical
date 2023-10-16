# def main():
#     numbers = []
#
#     for i in range(5):
#         number = int(input("Number: "))
#         numbers.append(number)
#
#     print("The first number is", numbers[0])
#     print("The last number is", numbers[-1])
#     print("The smallest number is", min(numbers))
#     print("The largest number is", max(numbers))
#     print("The average of the numbers is", sum(numbers) / len(numbers))
#
# main()

# List of users
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask user for username
user_input = input("Enter your username: ")

# Check if username is in list
if user_input in usernames:
    print("Access granted")
else:
    print("Access denied")
