from saveloader import *
from functions import *
from player import menu
from rich import print as rprint
from time import sleep as wait
from playsound3 import playsound

# Version and Important stuff
version = "0.3.1"
build_date = "30/7/2024"
systems = ("95", "95+")
languages = ("en")
systems_int = tuple(range(2 + 1))


def boot():
    find_save()
    check_lives = load("save.json", "lives")
    check_lang = load("save.json", "lang")
    if check_lives > 3 or check_lang not in languages:
        clear()
        print(load("lang.json", "error-save-modified", load("save.json", "lang")))
        exit()

    clear()
    playsound("sounds/beep.wav")
    while True:
        clear()
        print(load("lang.json", "sparrow", load("save.json", "lang")))
        print(load("lang.json", "version", load("save.json", "lang")))
        rprint(f"[bright_red]- {load("lang.json", "beta-warning", load("save.json", "lang"))} -[bright_red]\n")

        counter = 1
        for i in systems:
            system_unlocked = load_os(f"PB{i}", "unlocked")
            global_label = load("save.json", f"PB{i}_label", "save")
            if global_label == "None":
                global_label = ""
            if system_unlocked == True:
                print(f"{counter}.", load_os(f"PB{i}", "name"), global_label)
            elif system_unlocked == False:
                print(f"{counter}.", load_os(f"PB{i}", "name"), global_label, "(not unlocked)")
            counter += 1

        try:
            choice = int(input(f"\n{load("lang.json", "select-system", load("save.json", "lang"))} "))
            label = load("save.json", f"PB{systems[choice-1]}_label", "save")
            if label == "None":
                label = ""

            if choice in systems_int:
                system = load("oses.json", f"system_PB{systems[choice-1]}", "os")
                clear()
                if system['unlocked'] == True:
                    print(f"{load("lang.json", "loading", load("save.json", "lang"))} {load_os(f"PB{systems[choice-1]}", "name")} {label}\n{load("lang.json", "wait", load("save.json", "lang"))}")
                    wait(3)
                    menu(load_os(f"PB{systems[choice-1]}", "short_name"), load("save.json", f"PB{systems[choice-1]}", "save"), True)
                elif system['unlocked'] == False:
                    print(load("lang.json", "system-not-unlocked-exist", load("save.json", "lang")))
                    wait(3)
                break
        except ValueError or EOFError:
            print(load("lang.json", "not-valid-input", load("save.json", "lang")))
            wait(2)


boot()