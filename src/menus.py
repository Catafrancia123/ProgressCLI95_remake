from functions import *
from saveloader import *
from player import game
from rich import print as rprint
from rich import box
from rich.table import Table
from time import sleep as wait

#! Tables for the menu
try: LANG = load("save.json", "lang", "settings")
except Exception: 
    find_save() 
    LANG = load("save.json", "lang", "settings")

def load_tables(system_name : str):
    #! Make it accessible anywhere
    global menutable1, begintable1, begintable2, begintable3, settingstable

    #* Main Menu 1 (no bin, achivements, calendar)
    menutable1 = Table(title=load_os(system_name, "name"), box=box.ROUNDED)
    menutable1.add_column(load("lang.json", "main-collumn", LANG))
    
    menutable1.add_row(f"1. {load("lang.json", "main-row-1", LANG)}")
    menutable1.add_row(f"2. {load("lang.json", "main-row-2", LANG)}")

    #* Begin Menu 1 (no load game)
    begintable1 = Table(title=load("lang.json", "main-row-2", LANG), box=box.ROUNDED)
    begintable1.add_column(load("lang.json", "main-collumn", LANG))
    
    begintable1.add_row(f"1. {load("lang.json", "begin-row-1", LANG)}")
    begintable1.add_row(f"2. {load("lang.json", "begin-row-3", LANG)}")
    begintable1.add_row(f"3. {load("lang.json", "begin-row-4", LANG)}")
    begintable1.add_row(f"4. {load("lang.json", "begin-row-5", LANG)}")
    begintable1.add_row(f"5. {load("lang.json", "begin-row-6", LANG)}")

    #* Begin Menu 2 (has load game)
    begintable2 = Table(title=load("lang.json", "main-row-2", LANG), box=box.ROUNDED)
    begintable2.add_column(load("lang.json", "main-collumn", LANG))
    
    begintable2.add_row(f"1. {load("lang.json", "begin-row-2", LANG)}")
    begintable2.add_row(f"2. {load("lang.json", "begin-row-1", LANG)}")
    begintable2.add_row(f"3. {load("lang.json", "begin-row-3", LANG)}")
    begintable2.add_row(f"4. {load("lang.json", "begin-row-4", LANG)}")
    begintable2.add_row(f"5. {load("lang.json", "begin-row-5", LANG)}")
    begintable2.add_row(f"6. {load("lang.json", "begin-row-6", LANG)}")

    #* Begin Menu 3 (pause game)
    begintable3 = Table(title=load("lang.json", "main-row-3", LANG), box=box.ROUNDED)
    begintable3.add_column(load("lang.json", "main-collumn", LANG))
    begintable3.add_row(f"1. {load("lang.json", "begin-row-8", LANG)}")
    begintable3.add_row(f"2. {load("lang.json", "begin-row-7", LANG)}")
    begintable3.add_row(f"3. {load("lang.json", "begin-row-5", LANG)}")
    begintable3.add_row(f"4. {load("lang.json", "begin-row-6", LANG)}")

    #* Settings Menu
    settingstable = Table(title=load("lang.json", "main-row-4", LANG), box=box.ROUNDED)
    settingstable.add_column(load("lang.json", "main-collumn", LANG))
    settingstable.add_row(f"1. {load("lang.json", "settings-row-1", LANG)}")
    settingstable.add_row(f"2. {load("lang.json", "settings-row-2", LANG)}")
    settingstable.add_row(f"3. {load("lang.json", "main-row-5", LANG)}")

#* MENUS
def menu(system_name : str, system_level: int, system_choice_index : int, load_table : bool = False):
    if load_table:
        load_tables(system_name)
    clear()
    rprint(menutable1)

    while True:
        choice = input("\n> ")
        if choice == "1":
            statistics(system_name, system_level)
        elif choice == "2":
            if system_level == 0:
                while True:
                    clear()
                    rprint(begintable1)
                    choicebm = input("\n> ")
                    if choicebm == "1":
                        game(system_name, system_level, system_choice_index)
                        break
                    elif choicebm == "2":
                        settings(system_name, system_level, system_choice_index)
                        break
                    elif choicebm == "4":
                        shutdown()
                        break
                    elif choicebm == "5":
                        restart()    
                        break
            elif system_level >= 1:
                while True:
                    clear()
                    rprint(begintable2)
                    choicebm = input("\n> ")
                    if choicebm == "2":
                        print(f"{load("lang.json", "delete-1", LANG)} (Y/N)")
                        choice_delete = input("> ")
                        if choice_delete.lower() == "y":
                            choice_sure = input(f"{load("lang.json", "delete-2", LANG)}: ")
                            if choice_sure.lower() == "delete":
                                edit("save.json", system_name, 0, "save")
                                print(load("lang.json", "delete-3", LANG))
                    elif choicebm == "1":
                        game(system_name, system_level, system_choice_index)
                        break
                    elif choicebm == "3":
                        settings(system_name, system_level, system_choice_index)
                        break
                    elif choicebm == "5":
                        shutdown()
                        break
                    elif choicebm == "6":
                        restart()
                        break
            elif system_level < 0: 
                edit("save.json", system_name, 0, "save")

def paused_menu(system_name : str, system_level: int):
    clear()
    rprint(begintable3)
    while True:
        choice = input("\n> ")
        if choice == "1":
            game(system_name, system_level)
            break
        elif choice == "2":
            print(load("lang.json", "game-3", LANG))
            wait(2)
            menu(system_name, system_level)
            break
        elif choice == "3":
            shutdown()
            break
        elif choice == "4":
            restart()
            break

#* STATISTICS
def statistics(system_name : str, system_level: int):
    clear()
    print(f"{load("lang.json", "main-row-1", LANG)}:\n")

    # Variables
    systems = ("PB95", "PB95+")
    systemslevels = {name: load("save.json", name, "save") for name in systems}
    allsystemslevels = sum(systemslevels.values())
    systems_unlocked = []
    for i in systems: systems_unlocked.append(i)

    print(f"{load("lang.json", "stats-1", LANG)} {allsystemslevels}")
    print(f"{load("lang.json", "stats-2", LANG)} {', '.join(systems_unlocked)}\n")
    input(load("lang.json", "continue", LANG))
    menu(system_name, system_level)

#* SETTINGS
def settings(system_name : str, system_level: int, system_choice_index: int):
    clear()
    rprint(settingstable)

    choice = input("\n> ")
    while True:
        if choice == "1":
            clear()
            if load("save.json", "bar_popup", "settings"):
                print(f"{load("lang.json", "settings-popup2", LANG)}")
            elif not load("save.json", "bar_popup", "settings"):
                print(f"{load("lang.json", "settings-popup", LANG)}")
            rprint(f"{load("lang.json", "game-1", LANG)}", "[blue]██████[/blue]")
            print(f"{load("lang.json", "settings-popup3", LANG)}")

            choice = input("> ")
            while True:
                if choice.lower() == "y":
                    edit("save.json", "bar_popup", True, "settings")
                    settings(system_name, system_level, system_choice_index)
                    break
                elif choice.lower() == "n":
                    edit("save.json", "bar_popup", False, "settings")
                    settings(system_name, system_level, system_choice_index)
                    break
        elif choice == "2":
            langobj = langset("player")
            globals()[langobj] = __import__(langobj)
            lang = eval(langobj).language()
        elif choice == "3":
            menu(system_name, system_level, system_choice_index)
            break


#* SHUTDOWN AND RESTART
def shutdown():
    clear()
    print(load("lang.json", "wait", LANG))
    wait(3)
    rprint(f"[bold yellow]{load("lang.json", "close-game", LANG)}[/bold yellow]")
    quit()

def restart():
    clear()
    print(load("lang.json", "wait", LANG))
    wait(3)
    from main import boot
    boot()