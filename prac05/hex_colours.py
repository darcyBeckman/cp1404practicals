COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4",
           "azure": "#f0ffff", "beige": "#f5f5dc", "black": "#000000", "blanchedalmond": "#ffebcd",
           "blueviolet": "#8a2be2"}
print(COLOURS)
colour_name = input("Colour name: ").lower()
while colour_name != "":
    if colour_name in COLOURS:
        print(f"{colour_name} hex is {COLOURS[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Colour name: ").lower()