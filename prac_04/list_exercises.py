# numbers = []
# total = 0
# for i in range(5):
#     number = int(input("Number: "))
#     numbers.append(number)
#     total += float(number)
# average = total / len(numbers)
# print("The first number is", numbers[0])
# print("The last number is", numbers[-1])
# print("The smallest number is", min(numbers))
# print("The largest number is", max(numbers))
# print(f"The average of the numbers is {average}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Username: ")
if username in usernames:
    print("Access granted :)")
else:
    print("Access denied :(")
