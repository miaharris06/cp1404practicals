def main():
    MINIMUM_LENGTH = 5
    password = get_password(MINIMUM_LENGTH)
    print_astericks(password)


def print_astericks(password):
    for letter in password:
        print("*", end="")


def get_password(MINIMUM_LENGTH):
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error")
        password = input("Password: ")
    return password


main()