W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'

import os
try:
    import my_fake_useragent
except ImportError:
    print('\n [✓] installing pip wait !...\n')
    os.system('pip install my_fake_useragent')
from my_fake_useragent import UserAgent
import os
import sys
import time
import requests
import random
import platform
import base64
import marshal
import zlib
os.system("clear")
logo = """
          \033[91;1m########  ######## ##     ## #### ##       
          \033[92;1m##     ## ##       ##     ##  ##  ##       
          \033[93;1m##     ## ##       ##     ##  ##  ##       
          \033[94;1m##     ## ######   ##     ##  ##  ##       
          \033[95;1m##     ## ##        ##   ##   ##  ##       
          \033[96;1m##     ## ##         ## ##    ##  ##       
          \033[97;1m########  ########    ###    #### ########      
    \033[93;1m    ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬     
   \033[1;91m    ========={ \033[1;92mAUTHER 🔥 👿DAD OF DEVIL👿\033[1;91m }=========                                  
\033[1;90m═══════════════════════════════════════════════════════════
\033[1;94m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : Dad Of Devil  
\033[1;95m [\033[1;94m✯\033[1;91m] \033[1;92mFB GROUP : FB TRICKS AND FRIEND ZONE ( DEEPAK X JONTY)
\033[1;93m [\033[1;94m✯\033[1;91m] \033[1;92mTOOL : USER-AGENTS
\033[1;97m [\033[1;94m✯\033[1;91m] \033[1;92mNOTE : USER-AGENT FOR YOUR COMMANDS
\033[1;90m═══════════════════════════════════════════════════════════
    """


def dod():
    os.system("clear")
print(logo)
print(' \033[1;97m[1] : Chrome User Agents[5 UA IN ONE CLICK] \033[0m')
print(' \033[1;97m[2] : FireFox User Agents[5 UA IN ONE CLICK] \033[0m')
print(' \033[1;97m[3] : Safari User Agents[5 UA IN ONE CLICK] \033[0m')
print(' \033[1;97m[4] : Opera User Agents[5 UA IN ONE CLICK] \033[0m')
print("")
__DOD = input(" [✓] C H O O S E : ")
if __DOD in ["", " "]:
	Main()
elif __DOD in ["1", "01"]:
    print('\n [✓] wait !...\n')
    os.system('python 1.py')
elif __DOD in ["2", "02"]:
    print('\n [✓] wait !...\n')
    os.system('python 2.py')
elif __DOD in ["3", "03"]:
    print('\n [✓] wait !...\n')
    os.system('python 3.py')
elif __DOD in ["4", "4"]:
    print('\n [✓] wait !...\n')
    os.system('python 4.py')
else:
	exit()
