from prac08.SilverServiceTaxi import SilverServiceTaxi
from prac08.taxi import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "limo", 2), SilverServiceTaxi(200, "Hummer", 4)]
    bill = 0
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = get_menu_choice(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = int(input("Choose taxi: "))
        if choice == "d":
            try:
                distance = int(input("Drive how far? "))
                taxis[current_taxi].drive(distance)
                print(f"Your {taxis[current_taxi].name} trip will cost you ${taxis[current_taxi].get_fare():.2f}")
                bill += taxis[current_taxi].get_fare()
            except TypeError:
                print("Choose a taxi first")
        print(f"Bill to date: {bill:.2f}")
        print(MENU)
        choice = get_menu_choice(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)


def get_menu_choice(prompt):
    choice = input(prompt)
    while choice not in "qcd":
        print("Invalid Option")
        choice = input(prompt)
    return choice


def display_taxis(lst):
    for item in lst:
        print(f"{lst.index(item)} - {item}")


main()
