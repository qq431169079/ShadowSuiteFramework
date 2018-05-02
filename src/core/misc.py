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
import random

from core import version
from core import logger

if sys.platform == 'linux' or sys.platform == 'darwin':
    # Colors with meanings
    CW = '\033[0m'     #  white     (normal)
    CR = '\033[31m'    #  red       (errors)
    CG = '\033[32m'    #  green     (main color)
    CY = '\033[33m'    #  yellow    (warnings)
    CB = '\033[34m'    #  blue      (highlights)
    CGR = '\033[37m'   #  gray      (questions)

    # Misc colors
    CP = '\033[35m'    #  purple
    CC = '\033[36m'    #  cyan

    # Font types
    FR = '\033[0m'     #  regular
    FB = '\033[1m'     #  bold
    FI = '\033[3m'     #  italic

else:
    # No color support on windows operating systems.
    CW = ''
    CR = ''
    CG = ''
    CY = ''
    CB = ''
    CGR = ''

    CP = ''
    CC = ''

    FR = ''
    FB = ''
    FI = ''

# Shadow Suite's logo and a brief description.
LOGO = CG + """  ___|  |               |                  ___|       _) |
\\___ \\  __ \\   _` |  _` |  _ \\\\ \\  \\   / \\___ \\  |   | | __|  _ \\
      | | | | (   | (   | (   |\\ \\  \\ /        | |   | | |    __/
_____/ _| |_|\\__,_|\\__,_|\\___/  \\_/\\_/   _____/ \\__,_|_|\\__|\\___|""" + "\n                    Linux Edition\n                Ethical Hacking Toolkit\n\n" + '\n' + version.BOTH + CW

# brief description of the license.
BRIEF_LICENSE = CG + r"""This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'license' for details.""" + CW

# ShadowSuite is running as module.
MODULE_MODE_INFO = CY + "[i] Running as module...\n" + CW

# Debugging and Failsafe modes
debugging = False # Default value
failsafe = False # Default value

class programFunctions:
    COPYRIGHT = "Copyright(C) 2017-2018 by Shadow Team"

    def program_restart(self):
        try:
            open('.last_session_exit_fail.log', 'r').read() # Try to read the file
            open('.last_session_exit_fail.log', 'r').close() # Close the file
            IS_WINDOWS = self.is_windows()
            if IS_WINDOWS == False:
                os.system('rm .last_session_exit_fail.log') # Delete the file

            else:
                os.system("del .last_session_exit_fail.log") # Delete the file

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

            elif platform == 'windows' or platform == 'nt':
                os.system('cls')

            else:
                os.system('clear')
                # DEV0001: Thinking of new generic clrscrn...
                """
                loop = 0
                while loop != 100:
                    print()
                    loop += 1
                """

        except KeyboardInterrupt:
            print(error.ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def pause(self, silent=False):
        try:
            """
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
            """

            if silent == True:
                input()

            else:
                input("Press return/enter to continue...")

        except KeyboardInterrupt:
            print(error.ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def error_except(self):
        try:
            loop = True
            while loop == True:
                quit = None
                ask = input(CB + FB + FI + 'Do you want to keep Shadow Suite running? (y/n)> ' + CW + FR)
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
            print(error.ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def get_platform(self):
        result = sys.platform
        return result

    def cli_color_support(self):
        PLATFORM = self.get_platform()
        if PLATFORM == 'linux':
            return True

        elif PLATFORM == 'windows':
            return False

        else:
            # Just to be sure that we will not mess up everything.
            return False

    def is_windows(self):
        PLATFORM = self.get_platform()
        if PLATFORM == 'windows':
            return True

        else:
            return False

    def generate_session_id(self):
        session = random.randint(111111, 999999)
        return session
