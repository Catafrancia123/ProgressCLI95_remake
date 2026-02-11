"""
Version: v0.4.1-dev2
New Features: 
    - Documentation for saveloader functions
    - Added the change language option in settings
    - Fixed several bugs
"""
from functions import *
from menus import menu
from rich import print as rprint
from time import sleep as wait
from playsound3 import playsound

# Version and Important stuff
VERSION = "v0.4.1-dev2"
BUILD_DATE = "09-02-2026"
SYSTEMS = ("PB95", "PB95+")
LANGS = ("en")
SYSTEMS_INT = tuple(range(len(SYSTEMS)+1))

try: LANG = load("save.json", "lang", "settings")
except Exception: find_save()

def boot():
    check_lives = load("save.json", "lives", "save")
    LANG = load("save.json", "lang", "settings")
    if check_lives > 3 or LANG not in LANGS:
        clear()
        print(load("lang.json", "error-save-modified", LANG))
        exit()


    clear()
    has_audio = load("save.json", "has_audio", "settings")
    if has_audio: playsound("sounds/beep.wav")
    while True:
        clear()
        print(load("lang.json", "sparrow", LANG)) # yes
        print(load("lang.json", "version", LANG).format(VERSION, BUILD_DATE))
        rprint(f"[bright_red]- {load("lang.json", "beta-warning", LANG)} -[bright_red]\n")
            
        counter = 1
        for i in SYSTEMS:
            unlockeds = load_os(i, "unlocked")
            global_label = load_os(i, "label")

            if unlockeds:
                rprint(f"[#cccccc]{counter}. {load_os(i, "name")}[/#cccccc] {global_label}")
            elif not unlockeds:
                rprint(f"[#cccccc]{counter}[/#cccccc]. [bright_red]{load_os(i, "name")} ({load('lang.json', 'not-unlocked', LANG)})[/bright_red]")

            counter += 1

        choice = input(f"\n{load('lang.json', 'select-system', LANG)} ")

        if choice == "credits":
            credits_pbcli()
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(SYSTEMS):
            choice_index = int(choice) - 1 
            unlocked = load_os(SYSTEMS[choice_index], "unlocked")
            label = load_os(SYSTEMS[choice_index], "label")
            label = "" if label == "None" else label

            if unlocked:
                clear()
                print(f"{load('lang.json', 'loading', LANG)} {load_os(SYSTEMS[choice_index], 'name')} {label}\n{load('lang.json', 'wait', LANG)}")
                wait(3)
                menu(load_os(SYSTEMS[choice_index], "short_name"), load("save.json", SYSTEMS[choice_index], "save"), choice_index, True)
                break
            elif not unlocked:
                print(load("lang.json", "system-not-unlocked-input", LANG))
                wait(3)
        else:
            print(load("lang.json", "system-not-unlocked-input", LANG)) 
            wait(2)

def credits_pbcli():
    LANG = load("save.json", "lang", "settings")
    clear()
    rprint(load("lang.json", "credits-1", LANG))
    rprint("[#0000FF]Catamapp[/#0000FF] - Main Developer")
    rprint("[light_green]kernelpanic[/light_green] - Contributor\n")
    rprint(load("lang.json", "credits-2", LANG))
    rprint("[#0000FF]Catamapp[/#0000FF] - (en) English")
    rprint("[light_green]kernelpanic[/light_green] - (ru) Russian\n")

    input(load("lang.json", "continue", LANG))
    boot()
    

if __name__ == "__main__":
    boot()