"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

MENU = "\n(R)esult \n(S)tars \n(Q)uit"


def main():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            print(determine_result(score))
        elif choice == "S":
            for i in range(score):
                print("*", end="")
        print(MENU)
        choice = input(">>> ").upper()



def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
