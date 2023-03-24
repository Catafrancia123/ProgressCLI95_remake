import os
import sys as system

def clear():
    if system.platform.startswith(('win32')):
        os.system('cls')
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')

