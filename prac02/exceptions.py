"""
Q1) when a letter or symbol is entered instead of a number
Q2) when the denominator is set to 0
Q3) Yes
"""



try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

finished = False
result = 0
while not finished:
    try:
        result = int(input("Integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
