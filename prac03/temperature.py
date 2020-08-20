"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_fahrenheit(celsius)
            display_result(fahrenheit, "F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_celsius(fahrenheit)
            display_result(celsius, "C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def display_result(result, unit):
    print(f"Result: {result:.2f} {unit}")


def convert_fahrenheit_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
