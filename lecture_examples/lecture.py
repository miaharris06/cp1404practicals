total = 0
line_number = 0
error_line_numbers = []
filename = input("File: ")
in_file = open(filename)
for line_number, line in enumerate(in_file, 1):
    try:
        total += float(line)
    except ValueError:
        error_line_numbers.append(line_number)
print(total)
print(f"The following lines have errors:", end=" ")
print(", ".join([str(number) for number in error_line_numbers]))
