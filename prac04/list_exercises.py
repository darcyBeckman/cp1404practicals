NUMBER_OF_NUMBERS = 5
numbers = []
for i in range(NUMBER_OF_NUMBERS):
    numbers.append(int(input("Numbers: ")))
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers)}")
print()
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_username = input("Username: ")
if user_username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
