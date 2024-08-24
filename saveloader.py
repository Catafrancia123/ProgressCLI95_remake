import json, os

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
            "lang": "en",
            "save": {
                "PB95" : 0,
                "PB95+" : 0,
            },
            "lives": 3
        }

        with open("save.json", "w") as outfile:
            json.dump(save_template, outfile)
    else:
        if not quiet:
            print("Save Found, Continuing game...")

def load_os(os_name : str, to_load : str):
    with open(oses, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    return load["os"][f"system_{os_name}"][to_load]

def load(path : str, to_load : str, library : str = "none"):
    with open(path, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    if library == "none":
        return load[to_load]
    return load[library][to_load]

def edit(path : str, to_change : str, value, library : str = "none"):
    with open(path, mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    if library != "none":
        data[library][to_change] = value
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