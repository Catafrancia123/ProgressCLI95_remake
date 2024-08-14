from rich import print as rprint
from rich import box
from rich.table import Table
from rich.panel import Panel
from functions import clear

def test1():
    same = 0
    counter = 5000

    for i in range(1000):
        counter += 1
        
        find = list(map(str, str(counter)))
        thousand_digit = int(find[0])
        result = int(find[1]) + int(find[2]) + int(find[3])

        if result == thousand_digit:
            same += 1

    print(same)

def test2():
    clear()
    text = ":) Annoying Popup!"
    rprint(Panel(f"{text}\n       [OK]", box=box.ROUNDED, width=22))

test2()