from prac06.Guitar import Guitar


def main():
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = get_float("Year: ")
        cost = get_float("Cost: ")
        guitar_add = Guitar(name, year, cost)
        guitars.append(guitar_add)
        print(f"{guitar_add} added.")
        name = input("Name: ")
    print("These are my guitars")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() is True else ""
        print(f"Guitar {i}: {guitar.name} ({guitar.year}), worth $ {guitar.cost} {vintage_string}")


def get_float(prompt):
    return float(input(prompt))


main()
