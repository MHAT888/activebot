import os
try:
    import aminolib
except ModuleNotFoundError:
    os.system("pip install aminolib")

try:
    import aminofix
except ModuleNotFoundError:
    os.system("pip install aminofix")

try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")

try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")

os.system("clear")

import aminofix
import aminolib as lib
from colorama import *
import pyfiglet

print(Fore.RED + Style.BRIGHT)
print("π΄πΆππΌππΈ π΅ππ π·πΈππΈπΏπππΈπ· π΅π πΏπππ· π΄ππ· πΈπ·πΌππΈπ· π΅π ππ»π΄π ππΏππΏπ")
print("")
print(pyfiglet.figlet_format("active", font="sblood"))

c=lib.Client()
e=input ("Email : ")
p=input ("Password : ")
c.login(e, p)
print("")
print("Logged...")

comId='232923843'
for i in range(5):
 c.send_active(comId)
 print(i+1)
