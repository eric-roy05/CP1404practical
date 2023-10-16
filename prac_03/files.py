# # Open file
# with open("name.txt", "r") as file:
#     # Read  name from  file
#     stored_name = file.read()
#
# # Print the formatted output
# print(f"Your name is {stored_name}")
#
#
# # Ask  user for their name
# user_name = input("Enter your name: ")
#
# # Open  file "name.txt"
# with open("name.txt", "w") as file:
#     # Add user's name to the file
#     file.write(user_name)
#
# Open file
# with open("numbers.txt", "r") as file:
#     # Read  first two numbers from file
#     first_number = int(file.readline())
#     second_number = int(file.readline())
#
# # Add the two numbers together
# result = first_number + second_number
#
# print(result)

# Open file
with open("numbers.txt", "r") as file:
    # Make total zero
    total = 0

    for line in file:
        total += int(line)

print("The total for all numbers in the file is:", total)
