from functions import *
from saveloader import *
from rich import print as rprint
from rich import box
from rich.table import Table
from rich.panel import Panel
from time import sleep as wait
import random

try: LANG = load("save.json", "lang", "settings")
except Exception: 
    find_save() 
    LANG = load("save.json", "lang", "settings")

#* The Game
def game(system_name : str, system_level: int, system_choice_index : int):
    clear()

    # Variables
    progressbar = list(range(20))
    curr_level = system_level
    pro_level = load_os(system_name, "pro_level")
    systems = ("PB95", "PB95+")
    unlock_level = load_os(systems[1], "unlock_level")
    bar_counter = 0
    can_input = True
    lives = load("save.json", "lives", "save")
    green_segment_catch = False
    perfectionist = False

    while True:
        # win or lose
        if lives == 0:
            print(load("lang.json", "game-4", LANG))
            lives = 3
            edit("save.json", "lives", lives)
            edit("save.json", system_name, curr_level-1, "save")
            from menus import menu
            menu(system_name, system_level)
        elif bar_counter >= 20 or green_segment_catch: # user wins
            # check perfectionist
            perfectionist = True
            for i in progressbar:
                if i == "y":
                    perfectionist = False
            if perfectionist:
                print(load("lang.json", "game-8", LANG))
            if not perfectionist:
                print(load("lang.json", "game-5", LANG))

            # get lives
            if perfectionist and lives < 3:
                lives += 1
                edit("save.json", "lives", lives)

            # edit variables to default
            curr_level += 1
            progressbar = list(range(20))
            bar_counter = 0
            can_input = True
            green_segment_catch = False
            perfectionist = False

            # labels (pro only for now)
            if curr_level == pro_level:
                print(load("lang.json", "label-1", LANG))
                edit_os("label", "Professional", systems[system_choice_index])

            # get pb95+
            if curr_level == unlock_level:
                if system_name == "PB95":
                    print(f"{load('lang.json', 'game-9', load('save.json', 'lang'))} {load_os(systems[1], "name")}")
                    edit_os("unlocked", True, load_os(systems[1], "short_name"))

            wait(2)
            edit("save.json", system_name, curr_level, "save")

        # popup
        popup_show = random.randint(0,7)
        if popup_show == 4:
            popup_spawn(progressbar)

        clear()
        print(f"{load("lang.json", "game-6", LANG)} {curr_level}")
        print(f"{load("lang.json", "game-7", LANG)} {lives}\n")
            
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

        if can_input:
            colored_progressbar = []
            for i in progressbar:
                if i == "b":
                    colored_progressbar.append("[blue]█[/blue]")
                elif i == "y":
                    colored_progressbar.append("[yellow]█[/yellow]")

        rprint("\n"+load("lang.json", "game-1", LANG), Panel("".join(colored_progressbar), box.ROUNDED, width=24))
        print(load("lang.json", "game-2", LANG))
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
            print(load("lang.json", "game-3", LANG))
            wait(2)
            from menus import menu
            menu(system_name, curr_level, system_choice_index)
            break
        elif choice_bar.lower() == "p":
            from menus import paused_menu
            paused_menu(system_name, system_level)
            break
        else:
            can_input = False

            
def popup_spawn(progressbar):
    while True:
        clear()
        colored_progressbar = []

        rprint(Panel(f"{load("lang.json", "popup", LANG)}\n       [OK]", box=box.ROUNDED, width=22))

        for i in progressbar:
            if i == "b":
                colored_progressbar.append("[blue]█[/blue]")
            elif i == "y":
                colored_progressbar.append("[yellow]█[/yellow]")
        rprint("\n"+load("lang.json", "game-1", LANG), Panel("".join(colored_progressbar), box.ROUNDED, width=24))

        popup_input = input("> ")
        if popup_input.lower() == "ok":
            break
