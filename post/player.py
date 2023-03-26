from clear import clear
from rich import print as rprint
from rich.table import Table
from rich.text import Text
from time import sleep
from functions import *
import random
from saveloader import editSystemSave, editSettingsFile, addSystemSave, loadSettingsSave, addSetting
from checkbadge import calculateBadge

def startup(system, systemlevel, systempro, systembadge, systemlogo, systemunlock, systemunlocklevel):
    langobj = loadSettingsSave("lang")
    globals()[langobj] = __import__(langobj)
    global lang
    lang = eval(langobj).language()

    global unlock
    global unlocklevel

    unlock = systemunlock
    unlocklevel = systemunlocklevel

    clear()
    print('P r o g r e s s b a r ', systemlogo)
    print(systembadge)
    print(lang.loading)
    sleep(5)

    generateTables(systemlogo)
    systemLogo = systemlogo.replace(" ", "")
    if systemLogo == "95":
        mainMenu(system, systemlevel, systempro, systemlogo, False)
    else:
        mainMenu(system, systemlevel, systempro, systemlogo, True)

def generateTables(systemlogo):
    global bm1table
    global bm2table
    global bm3table
    global instable
    global updatetable1
    global aptable
    global sett
    global begintui1
    global begintui2

    systemLogo = systemlogo.replace(" ", "")

    # begin menu table with no load game
    bm1table = Table()
    bm1table.add_column(lang.bm1)
    bm1table.add_row("1."+lang.bm2)
    bm1table.add_row("2."+lang.bm6)
    bm1table.add_row("3."+lang.bm4)
    bm1table.add_row("4."+lang.bm5)
    bm1table.add_row("5."+lang.bm8)

    # begin menu table with load game
    bm2table = Table()
    bm2table.add_column(lang.bm1)
    bm2table.add_row("1."+lang.bm3)
    bm2table.add_row("2."+lang.bm2)
    bm2table.add_row("3."+lang.bm6)
    bm2table.add_row("4."+lang.bm4)
    bm2table.add_row("5."+lang.bm5)
    bm2table.add_row("6."+lang.bm8)

    # paused begin menu
    bm3table = Table()
    bm3table.add_column(lang.bm1)
    bm3table.add_row("1."+lang.bm7)
    bm3table.add_row("2."+lang.bm2)
    bm3table.add_row("3."+lang.bm4)
    bm3table.add_row("4."+lang.bm5)
    bm3table.add_row("5."+lang.bm8)

    # annoying popup
    aptable = Table()
    aptable.show_header = False
    aptable.add_column("Annoying popup!")
    aptable.add_row(lang.annoyingPopup)
    aptable.add_row("       [OK]", style="bold bright_black")

    # instructions table
    instable = Table(title=lang.instable1, show_header=True, header_style="bold")
    instable.add_column(lang.instable2, no_wrap=True)
    instable.add_column(lang.instable3, no_wrap=True)
    instable.add_row(lang.instable4a, lang.instable4b)
    instable.add_row(lang.instable4c, lang.instable4d)
    instable.add_row(lang.instable5a, lang.instable5b)
    instable.add_row(lang.instable6a, lang.instable6b)
    instable.add_row(lang.instable7a, lang.instable7b)
    instable.add_row(lang.instable8a, lang.instable8b)
    instable.add_row(lang.instable9a, lang.instable9b)


    #settings table
    sett = Table()
    sett.add_column(lang.sett1)
    sett.add_row("1."+lang.sett2)
    sett.add_row("2."+lang.sett3)

    #begin menu tui without mail (95)
    begintui1 = Table(title="Progressbar "+systemLogo)
    begintui1.add_column(lang.mm1)
    begintui1.add_row(lang.mm2+ " - M")
    begintui1.add_row(lang.mm3+ " - B")
    begintui1.add_row(lang.mm4+ " - A")
    begintui1.add_row(lang.mm5+ " - C")
    begintui1.add_row(lang.mm7+ " - S")

    #begin menu tui with mail
    begintui2 = Table(title="Progressbar "+systemLogo)
    begintui2.add_column(lang.mm1)
    begintui2.add_row(lang.mm2+ " - M")
    begintui2.add_row(lang.mm3+ " - B")
    begintui2.add_row(lang.mm4+ " - A")
    begintui2.add_row(lang.mm5+ " - C")
    begintui2.add_row(lang.mm6+ " - X")
    begintui2.add_row(lang.mm7+ " - S")
 
def screenDownFun():
    # checks if you have orange segments in your bar
    if progressbar2 > 0:
        print(lang.bar, end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
            elif segment == "Orange":
                rprint("[bright_yellow][][/bright_yellow]", end='')
        print(lang.barProgress1.format(progressbar, progressbar2))
    else:
        print(lang.bar, end='')
        for segment in bar2:
            if segment == "Blue":
                rprint("[blue][][/blue]", end='')
        print(lang.barProgress2.format(progressbar))

def settings(systemname, systemlevel, systempro):
    clear()
    rprint(sett)
    choise = input("> ")
    if choise == "1":
        clear()
        print(lang.doYouWant)
        rprint(lang.bar, " [blue][][][][][][][][][][][][][][][][][][][][/blue]")
        print(lang.popupSetting)
        choice = input("> ")
        if choice == "Y" or choice =="y":
            editSettingsFile("barwhenpopup", "True")
            settings(systemname, systemlevel, systempro)
        elif choice == "N" or choice == "n":
            editSettingsFile("barwhenpopup", "False")
            settings(systemname, systemlevel, systempro)
        else:
            settings(systemname, systemlevel, systempro)
    elif choise == "2":
        mainMenu(systemname, systemlevel, systempro)
    else:
        settings(systemname, systemlevel, systempro)

# shutdown woohoo
def shutdown():
    clear()
    print(lang.wait)
    sleep(3)
    rprint(lang.closeCMD)
    sleep(2)
    quit()

def restart():
    clear()
    print(lang.wait)
    sleep(3)
    from boot import boot
    boot()

def instructions(systemname, systemlevel, systempro, systemlogo):
    clear()
    print(style_text(lang.bm8, justify="center", title=True))
    print(style_text(lang.ins1, style="bold"))
    print(lang.ins2+"\n")
    rprint(instable)
    print("\n"+lang.ins3)
    print(lang.con1)
    input()
    mainMenu(systemname, systemlevel, systempro, systemlogo)

def binpet(systemname, systemlevel, systempro, systemlogo):
    try:
        visits = loadSettingsSave("binvisits")
        if visits == 0:
            addSetting("binvisits", 0)
            print_paragraph("bin-figure-normal")
            mood = 50
        else:
            visits += 1
            editSettingsFile("binvisits", visits)
            if mood > 40 and mood < 60:
                print_paragraph("bin-figure-normal")
            elif mood > 0 and mood < 40:
                print_paragraph("bin-figure-sad")
            elif mood > 60 and mood < 100:
                print_paragraph("bin-figure-happy")
    except UnboundLocalError:
        print(lang.error)
        print(lang.con2)
        input()
        mainMenu(systemname, systemlevel, systempro, systemlogo)

# Begin menu normally
def mainMenu(systemname, systemlevel, systempro, systemlogo,  mail : bool = "nothing"):
    clear()
    systemLogo = systemlogo.replace(" ", "")
    if mail == "nothing" and systemLogo == "95":
        mail = False
    elif mail == "nothing":
        mail = True 
    
    if mail == False:
        rprint(begintui1)
        choisce = input("> ")
        if choisce.lower() == "s":
            clear()
            if systemlevel > 1:
                print(bm2table)
            else:
                rprint(bm1table)
            choice = input("> ")
            if choice == "1":
                if systemlevel > 1:
                    startGame(systemname, systemlevel, systempro, systemlogo, systemlevel)
                else:
                    editSystemSave(systemname, 1)
                    startGame(systemname, 1, systempro, systemlogo, systemlevel)
            elif choice == "2":
                if systemlevel > 1:
                    editSystemSave(systemname, 1)
                    startGame(systemname, 1, systempro, systemlogo, systemlevel)
                else:
                    settings(systemname, systemlevel, systempro)
            elif choice == "3":
                if systemlevel > 1:
                    settings(systemname, systemlevel, systempro)
                else:
                    restart()
            elif choice == "4":
                if systemlevel > 1:
                    restart()
                else:
                    shutdown()
            elif choice == "5":
                if systemlevel > 1:
                    shutdown()
                else:
                    instructions(systemname, systemlevel, systempro)
            elif choice == "6":
                if systemlevel > 1:
                    instructions(systemname, systemlevel, systempro)
            else:
                mainMenu(systemname, systemlevel, systempro, systemlogo)
        elif choisce.lower() == "b":
            binpet(systemname, systemlevel, systempro)
        else:
            print(lang.comingsoon)
            sleep(3)
            mainMenu(systemname, systemlevel, systempro, systemlogo)    
    elif mail == True:
        rprint(begintui2)
        choisce = input("> ")
        if choisce.lower() == "s":
            clear()
            if systemlevel > 1:
                print(bm2table)
            else:
                rprint(bm1table)
            choice = input("> ")
            if choice == "1":
                if systemlevel > 1:
                    startGame(systemname, systemlevel, systempro, systemlogo, systemlevel)
                else:
                    editSystemSave(systemname, 1)
                    startGame(systemname, 1, systempro, systemlogo, systemlevel)
            elif choice == "2":
                if systemlevel > 1:
                    editSystemSave(systemname, 1)
                    startGame(systemname, 1, systempro, systemlogo, systemlevel)
                else:
                    settings(systemname, systemlevel, systempro)
            elif choice == "3":
                if systemlevel > 1:
                    settings(systemname, systemlevel, systempro)
                else:
                    restart()
            elif choice == "4":
                if systemlevel > 1:
                    restart()
                else:
                    shutdown()
            elif choice == "5":
                if systemlevel > 1:
                    shutdown()
                else:
                    instructions(systemname, systemlevel, systempro)
            elif choice == "6":
                if systemlevel > 1:
                    instructions(systemname, systemlevel, systempro)
            else:
                mainMenu(systemname, systemlevel, systempro, systemlogo)
        elif choisce.lower() == "b":
            binpet(systemname, systemlevel, systempro)
        else:
            print(lang.comingsoon)
            sleep(3)
            mainMenu(systemname, systemlevel, systempro, systemlogo) 

# Begin menu during gameplay
def pauseBeginMenu(systemName, systemlevel, systemPro, systemlogo):
    clear()
    rprint(bm3table)
    choice = input()
    if choice == "1":
        return
    elif choice == "2":
        editSystemSave(systemName, 1)
        startGame(systemName, 1, systemPro, systemlogo, systemlevel, systemlevel)
    elif choice == "3":
        restart()
    elif choice == "4":
        shutdown()
    elif choice == "5":
        instructions(systemName, systemlevel, systemPro, systemlogo)
    else:
        pauseBeginMenu(systemName, systemlevel, systemPro, systemlogo)

# original code by Setapdede, but i refined it a bit.
def spawnPopup(startLevel, systemLabel):
    clear()
    print('Level', startLevel)
    if systemLevel > 0:
        print('<', systemLabel, '>')
    rprint(aptable)
    popupinput = input()
    if popupinput.lower() == "ok":
	    clear()
    elif popupinput == "Ok":
        clear()
    else:
        spawnPopup(startLevel, systemLabel)

def startGame(systemName, startLevel, proLevel, systemlogo, systemlevel):
    global progressbar # total progressbar progress
    global progressbar2 # total orange segments in progressbar
    global lives
    global score
    global bar # array that contains segments for the progressbar
    global bar2 # contents in bar that are used to calculate pink segments
    global bardisplay # bar[] contents are displayed on screen
    global segments # used in conjunction with bardisplay
    global systemLabel # current system label
    global systemLevel # current system level (used with systemLabel)

    # setting global variables
    progressbar = 0
    progressbar2 = 0
    lives = 3
    score = 0
    bar = []
    bar2 = []
    bardisplay = ""
    segments = ""

    systemLabel = calculateBadge(startLevel, proLevel)
    if systemLabel == "What?":
        systemLabel = 8
    elif systemLabel == "Do you even touch grass yet??":
        systemLevel = 7
    elif systemLabel == "Grandmaster":
        systemLevel = 6
    elif systemLabel == "Grand":
        systemLevel = 5
    elif systemLabel == "Adept":
        systemLevel = 4
    elif systemLabel == "Master":
        systemLevel = 3
    elif systemLabel == "Expert":
        systemLevel = 2
    elif systemLabel == "Pro":
        systemLevel = 1
    else:
        systemLevel = 0

    while True:
        # clears the screen for next segment
        clear()

        # checks if lives are 0, breaks if true
        if lives == 0:
            rprint(lang.outOfLives)
            if startLevel == 1:
                rprint(lang.noLevelTaken)
            else:
                startLevel -= 1
                rprint(lang.negateLevel)
                editSystemSave(systemName, startLevel)
            lives = 3
            sleep(3)
            clear()

        popupshow = random.randint(0, 6)
        if popupshow == 6:
            spawnPopup(startLevel, systemLabel)

        print(lang.level, startLevel)
        if systemLevel > 0:
            print('<', systemLabel, '>')

        # randomly chooses a segment and loads art
        seg = random.randint(0, 5)
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

        # green segment check
        greenseg = random.randint(0, 250)
        if greenseg == 95:
            clear()
            print('Level', startLevel)
            if systemLevel > 0:
                print('<', systemLabel, '>')
            seg = 6
            rprint("[bright_green]╔══╗\n║$$║\n║$$║\n╚══╝[/bright_green]")

        # checks if you have 1 life left
        if lives == 1:
            rprint(lang.oneLifeLeft)
        else:
            print(lang.livesLeft.format(lives))

        screenDownFun()

        # catches the currently displayed segment
        catch = input(lang.pressInstructions)

        # calculates which segment you caught and does stuff
        if seg == 0 and catch == "c":
            progressbar = progressbar + 5
            bar2.append("Blue")
            score += 5
        elif seg == 1 and catch == "c":
            bar = []
            bar2 = []
            bardisplay = ""
            lives = lives - 1
            progressbar = 0
            progressbar2 = 0
            score -= 1
        elif seg == 2 and catch == "c":
            if progressbar == 0:
                continue
            if bar2[-1] == "Orange":
                progressbar2 = progressbar2 - 5
                progressbar = progressbar - 5
                bar2.pop(-1)
                score += 5
            else:
                progressbar = progressbar - 5
                bar2.pop(-1)
                score + score - 5
        elif seg == 3 and catch == "c":
            progressbar = progressbar + 5
            progressbar2 = progressbar2 + 5
            bar2.append("Orange")
        elif seg == 4 and catch == "c":
            continue
        elif seg == 5 and catch == "c":
            bonus = random.randint(0, 1)
            if bonus == 0:
                progressbar = progressbar + 10
                bar2.append("Blue")
                bar2.append("Blue")
                score += 10
            else:
                progressbar = progressbar + 15
                bar2.append("Blue")
                bar2.append("Blue")
                bar2.append("Blue")
                score += 15
        elif seg == 6 and catch == "c":
            progressbar = 100
            progressbar2 = 0
            score += 100

        if catch == "q":
            print(lang.gameOver)
            sleep(3)
            mainMenu(systemName, startLevel, proLevel, systemlogo)

        if catch == "beginmenu" or catch.lower() == "bm":
            pauseBeginMenu(systemName, systemlevel, proLevel, systemlogo)

        # if you have 100% on your progressbar, the game will end.
        if progressbar >= 100:

            # bonuses
            if progressbar2 > 0:
                print(lang.gameBravo)
            elif progressbar >= 100 and progressbar2 == 0:
                print(lang.gamePerfect)
            elif progressbar > 100:
                print(lang.gameOuterSpace)

            if progressbar == 50 and progressbar2 == 50:
                print (lang.gameYinAndYang)

            if progressbar == 0 and progressbar2 == 100:
                print (lang.gameNonconformist)

            # increment level count
            startLevel += 1
            editSystemSave(systemName, startLevel)

            # system unlock check section
            if unlocklevel == False:
                print()
            elif startLevel == unlocklevel:
                rprint(lang.newSystem)
                addSystemSave(unlock)

            # check pro
            if startLevel == proLevel:
                print(lang.proCongrats)
                print(lang.proAcquired)
                systemLevel = 1
                systemLabel = "Pro"

            # label check section
            if startLevel == 100:
                print(lang.expertAcquired)
                systemLevel = 2
                systemLabel = "Expert"
            elif startLevel == 250:
                print(lang.masterAcquired)
                systemLevel = 3
                systemLabel = "Master"
            elif startLevel == 500:
                print(lang.adeptAcquired)
                systemLevel = 4
                systemLabel = "Adept"
            elif startLevel == 1000:
                print(lang.grandAcquired)
                systemLevel = 5
                systemLabel = "Grand"
            elif startLevel == 5000:
                print(lang.grandmaster)
                systemLabel = 6
                systemLabel = "Grandmaster"
            elif startLevel == 10000:
                print(lang.discordmod)
                systemLabel = 7
                systemLabel = "Completed"
            elif startLevel == 2147483647:
                print(lang.whatAcquired)
               

            # reset variables and await input
            bar2 = []
            bardisplay = ""
            segments = ""
            progressbar = 0
            progressbar2 = 0
            print(lang.con2)
            input()
        continue
