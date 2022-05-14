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
import random
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
\033[1;97m [\033[1;94m✯\033[1;91m] \033[1;92mTOOL NAME : USER AGENT MAKER
\033[1;97m [\033[1;94m✯\033[1;91m] \033[1;92mNOTE : OPERA USER AGENTS ONLY
\033[1;90m═══════════════════════════════════════════════════════════
    """
    
x = UserAgent(family='opera')
b1 =x.random()
b2 = x.random()
b3 = x.random()
b4 = x.random()
b5 = x.random()

#randomly printing any 5 useragent
os.system("clear")
print(logo)
print("\033[92;1m[+] USER AGENT SAVED IN -> o-ua.txt")
print("\033[92;1m")
print(b1)
print("")
print(b2)
print("")
print(b3)
print("")
print(b4)
print("")
print(b5)

open("o-ua.txt","a").write(b1+'\n')
open("o-ua.txt","a").write(b2+'\n')
open("o-ua.txt","a").write(b3+'\n')
open("o-ua.txt","a").write(b4+'\n')
open("o-ua.txt","a").write(b5+'\n')




