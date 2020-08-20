MIN_LENGTH = 4


def main():
    """Main program."""
    password = get_password("Password: ")
    print_hidden_password(password)


def print_hidden_password(password):
    print(len(password) * "*")


def get_password(prompt):
    password = input(prompt)
    while len(password) < MIN_LENGTH:
        print(f"Your password must be {MIN_LENGTH} characters long")
        password = input(prompt)
    return password


main()
