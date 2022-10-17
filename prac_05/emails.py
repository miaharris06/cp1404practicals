"""
Emails
Estimate: 45 min
Actual: 30mins
"""
NUMBERS = "0123456789"


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n) ")
        if choice.upper() != "Y" and choice != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    parts = email.split("@")[0]
    names = parts.split(".")
    name = " ".join(names).title()
    return name


main()
