def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        choice = input(f"Is your name {name.title()}? (Y/n) ").lower()
        if choice not in ("y", "yes", ""):
            name = input("Name: ")
        emails[name] = email
        email = input("Email: ")
    for email in emails:
        print(f"{email} ({emails[email]})")


def get_name(email):
    name = email.split("@")
    name = name[0].split(".")
    name = " ".join(name)
    return name


main()
