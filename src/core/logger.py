# Made by Shadow Team
# Encoding=UTF-8

import os
from core import misc

def log(TYPE=9999, MSG="Logger called.", LOGFILE="logfile.txt"):
    TYPE = int(TYPE)
    line = '=' * 50

    boundary = os.system('echo ' + line + " >> " + LOGFILE)
    date = os.system("date >> " + LOGFILE)

    ### Basic types ###
    # 0 == Normal message
    # 1 == Warning message
    # 2 == Error message

    ### Extended Types ###
    # 3 == Important message
    # 4 == Serious warning message
    # 5 == Fatal error message

    if TYPE == 0:
        ICO = '[INF]: '

    elif TYPE == 1:
        ICO = '[WRN]: '

    elif TYPE == 2:
        ICO = '[ERR]: '

    elif TYPE == 3:
        ICO = '[***INF***]: '

    elif TYPE == 4:
        ICO = '[***WRN***]: '

    elif TYPE == 5:
        ICO = '[***ERR***]: '

    else:
        ICO = '[**UNK**]: '

    boundary
    date
    message = os.system('echo ' + ICO + MSG + " >> " + LOGFILE)
    boundary
    if misc.debugging == True:
        print("[DEBUG] Operation logged: " + ICO + MSG)
