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
systems_int = tuple(range(2+1))

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
            print(f"{counter}.", load_os(f"PB{i}", "name"))
            counter += 1

        try:
            choice = int(input(f"\n{load("lang.json", "select-system", load("save.json", "lang"))} "))
            if choice in systems_int:
                clear()
                print(load("lang.json", "wait", load("save.json", "lang")))
                wait(2)
                menu(load_os(f"PB{systems[choice-1]}", "short_name"), load("save.json", f"PB{systems[choice-1]}", "save"), True)
                break
            else: 
                print(load("lang.json", "system-not-unlocked-exist", load("save.json", "lang"))) 
                wait(2)
        except ValueError or EOFError:
            print(load("lang.json", "not-valid-input", load("save.json", "lang")))
            wait(2) 

boot()