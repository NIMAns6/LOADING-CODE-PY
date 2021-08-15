#Resorses
import time
from tqdm.notebook import tqdm
from tqdm import tqdm,trange,gui
from colorama import init,Fore
import sys
from os import system
import shutil

#loading page-Simple

for _ in tqdm(range(100),

        desc="Loading...",unit='kB',
        ascii=' ▁▂▄▅▆▇█',ncols=75,miniters=0):
    time.sleep(0.1)
columns = shutil.get_terminal_size().columns
print("Loading Done!".center(columns))

#loading page-Pro
columns = shutil.get_terminal_size().columns
init(autoreset=True)
def do_something ():
    time.sleep(0.04)
def do_another_something():
    time.sleep(0.09)
color_bars = ["\033[1;31;40m"]
for color in color_bars:
    for i in trange(100,unit='FILE',leave=False, position=1, file=sys.stdout,ascii='☆★',miniters=10,ncols=332, desc='\033[1;31;40m'+'System Loading...'.center(columns),bar_format='{l_bar}%s{bar}%s{r_bar}' % (color, Fore.RESET)):
        do_something()
    for j in trange(100,file=sys.stdout, miniters=2, leave=False, unit='FILE', desc='\033[1;32;40m'+'Program Loading...',ascii=' ▀▄▄▄▀▄▄▀█', ncols=70,bar_format='{l_bar}%s{bar}%s{r_bar}' % (color, Fore.RESET)):
        do_another_something()
color_bars = ["\033[1;33;40m"]
for color in color_bars:
    for i in trange(int(2e6), 
                    unit='FILE',desc='\033[1;33;40m'+' Cheak For Updates...'.center(columns),ascii=' ░░▒▒▓▓█'.center(columns),leave=True ,ncols=148,bar_format="{l_bar}%s{bar}%s{r_bar}" % (color, Fore.RESET)):  
        pass
    time.sleep(2)
columns = shutil.get_terminal_size().columns
print("\033[1;36;40m" + " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Loading Done!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(columns))
print("\033[1;36;40m" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| CyberPyscho |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~".center(columns))


tqdm.write("TY")
time.sleep (2)
system('cls')
