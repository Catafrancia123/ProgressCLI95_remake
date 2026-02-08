import os
import sys as system

def style_text(text: str, style: str = "normal", title: bool = False, justify: str = "left"):
    if justify == "center" and title == True:
        horizontal_line = "-" * 80
        lines = text.split("\n")
        centered_lines = [line.center(80) for line in lines]
        result = "\n".join(centered_lines)
        if result.endswith("\nNone"):
            result = result[:-5]
        return f"{horizontal_line}\n{result}\n{horizontal_line}"
    elif justify == "left":
        return text
    elif style == "bold":
        return f"\033[1m{text}\033[0m"
    elif style == "italic":
        return f"\033[3m{text}\033[0m]"
    elif style == "underline":
        return f"\033[4m{text}\033[0m"

def clear():
    if system.platform.startswith(('win32')):
        os.system('cls')
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')