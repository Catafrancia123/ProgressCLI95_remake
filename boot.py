from saveloader import *
from functions import *
from player import menu
from rich import print as rprint
from time import sleep as wait
from playsound3 import playsound

# Version and Important stuff
systems = ("PB95", "PB95+")
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
            unlockeds = load_os(i, "unlocked")
            global_label = load_os(i, "label")
            if global_label == "None":
                global_label = ""

            if unlockeds:
                rprint(f"[#cccccc]{counter}. {load_os(i, "name")}[/#cccccc] {global_label}")
            elif not unlockeds:
                rprint(f"[#cccccc]{counter}[/#cccccc]. [bright_red]{load_os(i, "name")} ({load('lang.json', 'not-unlocked', load('save.json', 'lang'))})[/bright_red]")

            counter += 1

        choice = input(f"\n{load('lang.json', 'select-system', load('save.json', 'lang'))} ")

        if choice == "credits":
            credits_pbcli()
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(systems):
            choice_index = int(choice) - 1 
            unlocked = load_os(systems[choice_index], "unlocked")
            label = load_os(systems[choice_index], "label")
            label = "" if label == "None" else label

            if unlocked:
                clear()
                print(f"{load('lang.json', 'loading', load('save.json', 'lang'))} {load_os(systems[choice_index], 'name')} {label}\n{load('lang.json', 'wait', load('save.json', 'lang'))}")
                wait(3)
                menu(load_os(systems[choice_index], "short_name"), load("save.json", systems[choice_index], "save"), choice_index, True)
                break
            elif not unlocked:
                print(load("lang.json", "system-not-unlocked-input", load("save.json", "lang")))
                wait(3)
        else:
            print(load("lang.json", "system-not-unlocked-input", load("save.json", "lang"))) 
            wait(2)

def credits_pbcli():
    clear()
    rprint(load("lang.json", "credits-1", load("save.json", "lang")))
    rprint("[#0000FF]Catamapp[/#0000FF] - Main Developer")
    rprint("[light_green]kernelpanic[/light_green] - Contributor\n")
    rprint(load("lang.json", "credits-2", load("save.json", "lang")))
    rprint("[#0000FF]Catamapp[/#0000FF] - (en) English")
    rprint("[light_green]kernelpanic[/light_green] - (ru) Russian\n")

    input(load("lang.json", "continue", load("save.json", "lang")))
    boot()
    

boot()