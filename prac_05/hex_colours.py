NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "alice blue": "#f0f8ff",
                "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00",
                "amethyst": "	#9966cc", "antique white": "#faebd7", "antique white1": "#ffefdb",
                "antique white2": "#eedfcc"}

colour_name = input("Colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Colour name: ").lower()
