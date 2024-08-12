import subprocess, sys
from functions import clear

clear()
subprocess.run([sys.executable, '-m', 'pip', 'install', 'pip', '--quiet', '-U'])
print("[OK] pip has been updated")
subprocess.run([sys.executable, '-m', 'pip', 'install', 'rich', '--quiet', '-U'])
print("[OK] rich has been installed & updated")
subprocess.run([sys.executable, '-m', 'pip', 'install', 'playsound', '--quiet', '-U'])
print("[OK] playsound has been installed & updated")
print("Setup complete. You can play the game now.")