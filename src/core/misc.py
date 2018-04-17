#!/bin/python
# Coding=UTF-8
# Shadow Suite Linux Edition :: Ethical Hacking Toolkit
# Copyright (C) 2017-2018  Shadow Team <Public.ShadowTeam@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import sys
from core import version
from core import logger

# Colors with meanings
cw = '\033[0m'     #  white     (normal)
cr = '\033[31m'    #  red       (errors)
cg = '\033[32m'    #  green     (main color)
cy = '\033[33m'    #  yellow    (warnings)
cb = '\033[34m'    #  blue      (highlights)
cgr = '\033[37m'   #  gray      (questions)

# Misc colors
cp = '\033[35m'    #  purple
cc = '\033[36m'    #  cyan

# Font types
fr = '\033[0m'     #  regular
fb = '\033[1m'     #  bold
fi = '\033[3m'     #  italic

# Shadow Suite's logo and a brief description.
logo = cg + """  ___|  |               |                  ___|       _) |
\\___ \\  __ \\   _` |  _` |  _ \\\\ \\  \\   / \\___ \\  |   | | __|  _ \\
      | | | | (   | (   | (   |\\ \\  \\ /        | |   | | |    __/
_____/ _| |_|\\__,_|\\__,_|\\___/  \\_/\\_/   _____/ \\__,_|_|\\__|\\___|""" + "\n                    Linux Edition\n                Ethical Hacking Toolkit\n\n" + '\n' + version.both + cw

# brief description of the license.
brief_license = cg + r"""This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'license' for details.""" + cw

# ShadowSuite is running as module.
module_mode_info = cy + "[i] Running as module...\n" + cw

# Debugging and Failsafe modes
debugging = False # Default value
failsafe = False # Default value

class programFunctions():
    copyright = "Copyright(C) 2017-2018 by Shadow Team"

    def program_restart(self):
        try:
            open('.last_session_exit_fail.log', 'r').read() # Try to read the file
            open('.last_session_exit_fail.log', 'r').close() # Close the file
            os.system('rm .last_session_exit_fail.log') # Delete the file

        except:
            pass # If file doesn't exist, do nothing, just restart.

        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

    def clrscrn(self):
        try:
            platform = sys.platform
            if platform == 'linux':
                os.system('clear')

            elif platform == 'windows':
                os.system('cls')

            else:
                os.system('clear')

        except KeyboardInterrupt:
            print(error.error0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def pause(self, silent=False):
        try:
            platform = sys.platform
            if platform == 'linux':
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')

            elif platform == 'windows':
                if silent is False:
                    os.system('pause')

                else:
                    os.sysem('pause > nul')

            else:
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')

        except KeyboardInterrupt:
            print(error.error0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def error_except(self):
        try:
            loop = True
            while loop == True:
                quit = None
                ask = input(cb + fb + fi + 'Do you want to keep Shadow Suite running? (y/n)> ' + cw + fr)
                ask = ask.lower()
                if ask == 'y':
                    loop = False
                    quit = False

                elif ask == 'n':
                    loop = False
                    quit = True

                else:
                    loop = True

            return quit

        except KeyboardInterrupt:
            print(error.error0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)
