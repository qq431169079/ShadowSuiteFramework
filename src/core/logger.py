# Made by Shadow Team
# Encoding=UTF-8

import os

def log(TYPE=3, MSG="", LOGFILE="logfile.txt"):
    TYPE = int(TYPE)
    line = '============================================================================='

    boundary = os.system('echo ' + line + " >> " + LOGFILE)
    date = os.system("date >> " + LOGFILE)

    # 0 == Normal message
    # 1 == Warning message
    # 2 == Error message

    if TYPE == 0:
        ICO = '[INF]: '

    elif TYPE == 1:
        ICO = '[WRN]: '

    elif TYPE == 2:
        ICO = '[ERR]: '

    else:
        ICO = '[UNK]: '

    boundary
    date
    message = os.system('echo ' + ICO + MSG + " >> " + LOGFILE)
    boundary
