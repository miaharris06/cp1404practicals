"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    score = float(input("Enter score: "))

    while 0 < score < 100:
        if score >= 50:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        else:
            print("Bad")
        score = float(input("Enter score: "))
    print("Invalid score")
