from functions import *
from saveloader import *
from rich import print as rprint
from rich import box
from rich.table import Table
from rich.panel import Panel
from time import sleep as wait
import random

def load_tables(system_name : str):
    # Make it accessible anywhere
    global menutable1, begintable1, begintable2

    # Main Menu 1 (no bin, achivements, calendar)
    menutable1 = Table(title=load_os(system_name, "name"), box=box.ROUNDED)
    menutable1.add_column(load("lang.json", "main-collumn", load("save.json", "lang")))
    
    menutable1.add_row(f"1. {load("lang.json", "main-row-1", load("save.json", "lang"))}")
    menutable1.add_row(f"2. {load("lang.json", "main-row-2", load("save.json", "lang"))}")

    # Begin Menu 1 (no load game)
    begintable1 = Table(title=load("lang.json", "main-row-2", load("save.json", "lang")), box=box.ROUNDED)
    begintable1.add_column(load("lang.json", "main-collumn", load("save.json", "lang")))
    
    begintable1.add_row(f"1. {load("lang.json", "begin-row-1", load("save.json", "lang"))}")
    begintable1.add_row(f"2. {load("lang.json", "begin-row-3", load("save.json", "lang"))}")
    begintable1.add_row(f"3. {load("lang.json", "begin-row-4", load("save.json", "lang"))}")
    begintable1.add_row(f"4. {load("lang.json", "begin-row-5", load("save.json", "lang"))}")
    begintable1.add_row(f"5. {load("lang.json", "begin-row-6", load("save.json", "lang"))}")

    # Begin Menu 2 (has load game)
    begintable2 = Table(title=load("lang.json", "main-row-2", load("save.json", "lang")), box=box.ROUNDED)
    begintable2.add_column(load("lang.json", "main-collumn", load("save.json", "lang")))
    
    begintable2.add_row(f"1. {load("lang.json", "begin-row-2", load("save.json", "lang"))}")
    begintable2.add_row(f"2. {load("lang.json", "begin-row-1", load("save.json", "lang"))}")
    begintable2.add_row(f"3. {load("lang.json", "begin-row-3", load("save.json", "lang"))}")
    begintable2.add_row(f"4. {load("lang.json", "begin-row-4", load("save.json", "lang"))}")
    begintable2.add_row(f"5. {load("lang.json", "begin-row-5", load("save.json", "lang"))}")
    begintable2.add_row(f"6. {load("lang.json", "begin-row-6", load("save.json", "lang"))}")

def menu(system_name : str, system_level: int, load_table : bool = False):
    if load_table == True:
        load_tables(system_name)
    clear()
    rprint(menutable1)
    choice = input("\n> ")

    while True:
        if choice == "1":
            print("nope")
        elif choice == "2":
            clear()
            if system_level == 0:
                rprint(begintable1)
                choicebm = input("\n> ")
                if choicebm == "1":
                    game(system_name, system_level)
                    break
                elif choicebm == "4":
                    shutdown()
                elif choicebm == "5":
                    restart()    
            elif system_level >= 1:
                rprint(begintable2)
                choicebm = input("\n> ")
                if choicebm == "2":
                    print(f"{load("lang.json", "delete-1", load("save.json", "lang"))} (Y/N)")
                    choice_delete = input("> ")
                    if choice_delete.lower() == "y":
                        choice_sure = input(f"{load("lang.json", "delete-2", load("save.json", "lang"))} ")
                        if choice_sure.lower() == load("lang.json", "delete-prompt", load("save.json", "lang")):
                            edit("save.json", system_name, 0, "save")
                            print(load("lang.json", "delete-3", load("save.json", "lang")))
                elif choicebm == "1":
                    game(system_name, system_level)
                    break
                elif choicebm == "5":
                    shutdown()
                elif choicebm == "6":
                    restart()
            elif system_level < 0: 
                edit("save.json", load_os(system_name, "short_name"), 0, "save")

# shutdown wgaming
def shutdown():
    clear()
    print(load("lang.json", "wait", load("save.json", "lang")))
    wait(3)
    find_save(True)
    rprint(f"[bold yellow]{load("lang.json", "close-game", load("save.json", "lang"))}[/bold yellow]")
    wait(2)
    quit()

def restart():
    clear()
    print(load("lang.json", "wait", load("save.json", "lang")))
    wait(3)
    from boot import boot
    boot()
            
def game(system_name : str, system_level: int):
    clear()

    # Variables
    progressbar = list(range(20))
    curr_level = system_level
    bar_counter = 0
    can_input = True
    lives = load("save.json", "lives")
    green_segment_catch = False
    perfectionist = False

    while True:
        if lives == 0:
            print(load("lang.json", "game-4", load("save.json", "lang")))
            lives = 3
            edit("save.json", "lives", lives)
            menu(system_name, system_level)
        elif bar_counter == 20 or green_segment_catch == True:
            perfectionist == True
            for i in progressbar:
                if i == "y":
                    perfectionist == False
            print(load("lang.json", "game-8", load("save.json", "lang")))
            if perfectionist == False:
                print(load("lang.json", "game-5", load("save.json", "lang")))
            wait(2)
            curr_level += 1
            progressbar = list(range(20))
            bar_counter = 0
            can_input = True
            green_segment_catch = False
            edit("save.json", system_name, curr_level, "save")
            if perfectionist == True:
                lives += 1
                edit("save.json", "lives", lives)

        # popup
        popup_show = random.randint(0,7)
        if popup_show == 6:
            popup_spawn()

        clear()
        print(f"{load("lang.json", "game-6", load("save.json", "lang"))} {curr_level}")
        print(f"{load("lang.json", "game-7", load("save.json", "lang"))} {lives}\n")
            
        # green segment
        seg = random.randint(0, 5)
        green_seg = random.randint(0, 250)
        if green_seg == 95:
            seg = 6
            rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")
        
        if seg != 6:
            if seg == 0:
                rprint("[blue]╔══╗\n║  ║\n║  ║\n╚══╝[/blue]")
            elif seg == 1:
                rprint("[bright_red]╔══╗\n║!!║\n║!!║\n╚══╝[/bright_red]")
            elif seg == 2:
                rprint("[bright_magenta]╔══╗\n║--║\n║--║\n╚══╝[/bright_magenta]")
            elif seg == 3:
                rprint("[bright_yellow]╔══╗\n║~~║\n║~~║\n╚══╝[/bright_yellow]")
            elif seg == 4:
                rprint("[bright_black]╔══╗\n║..║\n║..║\n╚══╝[/bright_black]")
            elif seg == 5:
                rprint("[bright_cyan]╔══╗\n║**║\n║**║\n╚══╝[/bright_cyan]")

        if can_input == True:
            colored_progressbar = []
            for i in progressbar:
                if i == "b":
                    colored_progressbar.append("[blue]█[/blue]")
                elif i == "y":
                    colored_progressbar.append("[yellow]█[/yellow]")

        rprint("\n"+load("lang.json", "game-1", load("save.json", "lang")), Panel("".join(colored_progressbar), box.ROUNDED, width=24))
        print(load("lang.json", "game-2", load("save.json", "lang")))
        choice_bar = input("> ")
        if choice_bar.lower() == "c":
            can_input = True
            if seg == 0:
                progressbar[bar_counter] = "b"
                bar_counter += 1
            elif seg == 1:
                lives -= 1
                edit("save.json", "lives", lives)
                progressbar = list(range(20))
                bar_counter = 0
            elif seg == 2:
                bar_counter -= 1
                if bar_counter < 0:
                    bar_counter = 0
                progressbar[bar_counter] = bar_counter
            elif seg == 3:
                progressbar[bar_counter] = "y"
                bar_counter += 1
            elif seg == 5:
                decider = random.randint(0,1)
                if decider == 0:
                    times = 2
                elif decider == 1:
                    times = 3

                if bar_counter > 20-times:
                    times -= 1

                for i in range(times):
                    progressbar[bar_counter] = "b"
                    bar_counter += 1

                          
            elif seg == 6:
                green_segment_catch = True   
        elif choice_bar.lower() == "q":
            print(load("lang.json", "game-3", load("save.json", "lang")))
            wait(2)
            menu(system_name, curr_level)
            break
        else:
            can_input = False
            
def popup_spawn():
    while True:
        clear()
        rprint(Panel(f"{load("lang.json", "popup", load("save.json", "lang"))}\n       [OK]", box=box.ROUNDED, width=22))
        popup_input = input("> ")
        if popup_input.lower() == "ok":
            break
