from saveloader import *
from functions import *
from player import main_menu
from rich import print as rprint
from time import sleep as wait

# Version and Important stuff
version = "0.3.1"
build_date = "30/7/2024"
systems = ["95", "95+"]
systems_int = tuple(range(1+1))

def boot():
    find_save()
    while True:
        clear()
        print(load("lang.json", "sparrow", "en"))
        print(load("lang.json", "version", "en"))
        rprint(f"[bright_red]- {load("lang.json", "beta-warning", "en")} -[bright_red]\n")

        counter = 1
        for i in systems: 
            print(f"{counter}.", load_os(i, "name"))
            counter += 1

        try:
            choice = int(input(f"\n{load("lang.json", "select-system", "en")} "))
            if choice in systems_int:
                main_menu(load_os("95", "short_name"), load("save.json", "PB95", "save"))
                break
            else: 
                print(load("lang.json", "system-not-unlocked-exist", "en"))
                wait(2)
        except ValueError:
            print(load("lang.json", "not-valid-input", "en"))
            wait(2)
        

boot()