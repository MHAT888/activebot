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
print("𝐴𝐶𝑇𝐼𝑉𝐸 𝐵𝑂𝑇 𝐷𝐸𝑉𝐸𝐿𝑂𝑃𝐸𝐷 𝐵𝑌 𝐿𝑂𝑅𝐷 𝐴𝑁𝐷 𝐸𝐷𝐼𝑇𝐸𝐷 𝐵𝑌 𝑀𝐻𝐴𝑇 𝑀𝐿𝑀𝐿𝑀")
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
