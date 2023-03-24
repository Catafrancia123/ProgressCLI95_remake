import sys
import os
from clear import clear
from saveloader import editSettingsFile

def langset():
    finished = False
    while not finished:
        clear()

        # import lang directory and put listing into variable
        sys.path.insert(0, './lang/')
        langDir = os.listdir('./lang/')

        # clean the old array and append cleaned data into new array
        langArray = []
        for x in langDir:
            if x == "__pycache__":
                continue
            else:
                x = x.replace('.py', '')
                langArray.append(x)

        # generate language list and wait for input
        for x in langArray:
            globals()[x] = __import__(x)
            xobj = eval(x).language()
            print('[{0}] {1}\n'.format(x, xobj.pleaseSelect))
        global langCode
        langCode = input('> ')

        # check if language code exists and return it if true.
        if langCode in langArray:
            editSettingsFile("lang", langCode)
            return langCode
            finished = True