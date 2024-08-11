import json, os

oses = "oses.json"
save = "save.json"

def find_save():
    save_found = False
    for root, dirs, files in os.walk("./"):
        if save in files:
            save_found = True

    if save_found == False:
        print("Save not found, Creating save...")
        save_template = {
            "lang": "en",
            "save": {
                "PB95": 0
            }
        }

        with open("save.json", "w") as outfile:
            json.dump(save_template, outfile)
    else:
        print("Save Found, Continuing game...")

def load_os(os_name : str, to_load : str):
    with open(oses, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    return load["os"][f"system_PB{os_name}"][to_load]

def load(path : str, to_load : str, libary : str = "none"):
    with open(path, mode="r", encoding="utf-8") as read_file:
        load = json.load(read_file)
    return load[libary][to_load]