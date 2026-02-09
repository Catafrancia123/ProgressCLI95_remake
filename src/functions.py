import json, os
import sys as system

#* Saveloader stuff
LANGS = ("en",)
oses = "oses.json"
save = "save.json"

def find_save(quiet : bool = False):
    save_found = False
    current_directory_files = os.listdir("./")  # List all files in the current directory

    if save in current_directory_files:  # Check if 'save.json' exists in the current directory
        save_found = True

    if not save_found:
        if not quiet:
            print("Save not found, Creating save...")
        save_template = {
            "save": {
                "PB95": 0,
                "PB95+": 0,
                "lives": 3,
            },
            "settings": {
                "lang": "en",
            }
        }

        with open("save.json", "w") as outfile:
            json.dump(save_template, outfile)
        print("Save created.")
        select_language()
    else:
        if not quiet:
            print("Save Found, Continuing game...")

def load_os(os_name : str, to_load : str):
    with open(oses, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    return load["os"][f"system_{os_name}"][to_load]

def load(path : str, to_load : str, index : str = "none") -> any:
    """"
    Loads data and returns it.

    Args:
        path (str): Path to the JSON file.
        to_load (str): Key to load from the JSON file.
        index (str, optional): The index within the JSON file. Defaults to "none".

    Returns:
        any: The data
    """

    with open(path, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    if index == "none":
        return load[to_load]
    return load[index][to_load]

def edit(path : str, to_change : str, value, index : str = "none") -> None:
    """"
    Loads data and returns it.

    Args:
        path (str): Path to the JSON file.
        to_load (str): Key to load from the JSON file.
        value: The new value to set.
        index (str, optional): The index within the JSON file. Defaults to "none".
    """

    with open(path, mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    if index != "none":
        data[index][to_change] = value
    else:
        data[to_change] = value

    with open(path, "w") as outfile:
        json.dump(data, outfile)

def edit_os(to_change : str, value, os_name : str):
    with open(oses, mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    data["os"][f"system_{os_name}"][to_change] = value
    with open(oses, "w") as outfile:
        json.dump(data, outfile, indent=3)

#* Other Functions

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

def select_language(startup: bool = True) -> None:
    clear()

    for i in LANGS:
        print(load("lang.json", "select-language", i))

    lang_choice = input("\n> ")
    if lang_choice in LANGS:
        edit("save.json", "lang", lang_choice, "settings")
    else:
        print("Invalid language code. Defaulting to English.")
        edit("save.json", "lang", "en", "settings")
        
    if not startup:
        print("Please restart the game to apply language changes.")
        exit()