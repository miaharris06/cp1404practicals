# Program 1
name = input("Name: ")
with open("name.txt", "w") as out_file:
    print(name, file= out_file)

#Program 2
with open("name.txt") as in_file:
    name = in_file.read()
    print(f"Your name is {name}")

#Program 3
with open("numbers.txt") as in_file:
    first_line = in_file.readline()
    second_line = in_file.readline()
    total = float(first_line) + float(second_line)
    print(total)

#Program 3
total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        total += float(line)
    print(total)
