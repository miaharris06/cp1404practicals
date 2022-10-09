import random

MIN_VALUE = 1
MAX_VALUE = 45
NUMBERS_PER_LINE = 6

number_of_quickpicks = int(input("How many quick picks? "))
for i in range(number_of_quickpicks):
    random_numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        while number not in random_numbers:
            random_numbers.append(number)
    random_numbers.sort()
    print(" ".join(f"{number:2}" for number in random_numbers))
