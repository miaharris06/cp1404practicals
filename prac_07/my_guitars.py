from prac_07.guitar import Guitar

guitars = []


def main():
    add_new_guitar()
    process_file()
    display_guitars()


def add_new_guitar():
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")
        guitars.append(Guitar(name, year, cost))


def display_guitars():
    for guitar in guitars:
        print(guitar)


def process_file():
    with open("guitars.csv", "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], parts[1], parts[2])
            guitars.append(guitar)
            guitars.sort()


main()
