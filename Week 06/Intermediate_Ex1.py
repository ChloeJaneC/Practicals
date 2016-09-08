"""
Intermediate Exercise 1
CJ
"""
COLOUR_NAMES = {"AQUAMARINE2": "#7fffd4", "AZURE1": "#f0ffff", "CADETBLUE1": "#5f9ea0", "CHARTREUSE2": "#76ee00",
                "CORNFLOWERBLUE": "#6495ed", "CORNSILK1": "#fff8dc", "DARKORCHID": "#9932cc",
                "DARKSEAGREEN1": "#c1ffc1", "DARKSLATEBLUE": "483d8b", "GREY15": "#262626"}


def main():
    print(COLOUR_NAMES)

    colour = input("Enter a colour name: ").upper()
    while colour != "":
        if colour in COLOUR_NAMES:
            print(colour, "is", COLOUR_NAMES[colour])
        else:
            print("Invalid colour choice")
        colour = input("Enter a colour name: ").upper()


main()
