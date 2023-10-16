COLOUR_CODES = {
    "AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4", "Azure": "#f0ffff",
    "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000", "BlanchedAlmond": "#ffebcd", "Blue": "#0000ff"}


def main():
    """
    Function interacts with users and selects colours
    """
    colour_name = input("Enter a colour name (or blank to stop): ").strip().upper()

    while colour_name != "":
        if colour_name:
            colour_code = lookup_colour_code(colour_name)
            if colour_code:
                print(f"The hexadecimal code for {colour_name} is {colour_code}")
            else:
                print("Invalid colour name. Please enter a valid colour name.")

        colour_name = input("Enter a colour name (or blank to stop): ").strip()


def lookup_colour_code(colour_name):
    """
    Look up the hexadecimal colour code for a given colour name.
    """
    try:
        return COLOUR_CODES[colour_name.upper()]
    except KeyError:
        return None


main()
