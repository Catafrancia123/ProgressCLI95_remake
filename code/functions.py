def bold_text(text : str):
    print("\033[1m"+text+"\033[0m")

def center_text(text : str, width : int):
    horizontal_line = "-" * width
    lines = text.split("\n")
    centered_lines = [line.center(width) for line in lines]
    result = "\n".join(centered_lines)
    if result.endswith("\nNone"):
        result = result[:-5]
    return f"{horizontal_line}\n{result}\n{horizontal_line}"

def print_paragraph(name : str):
    if name == "023":
        print(bold_text("ProgressCLI95 0.2.3 Updates!")+"""

            Were happy to introduce you the new features of the game!

            - More languages

            - Fixed some bugs

            - Added the credits Section

            Thanks for enjoying our game!""")