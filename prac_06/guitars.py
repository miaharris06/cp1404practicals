from prac_06.guitar import Guitar
guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")
    guitars.append(Guitar(name, year, cost))

print("These are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = ""
    if guitar.is_vintage():
        vintage_string = " (vintage) "
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
