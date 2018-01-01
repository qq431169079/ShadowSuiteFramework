#!/bin/python

# Shadow Suite :: Ethical Hacking Toolkit
# Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>
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

# =====ERROR CODES=====
#
# In 
# ERROR 0001: Invalid input! Please check your command.

# =====WARNING CODES=====
#
# WARNING 0001: Shadow Suite has been renamed!

# Colors with meanings
cw = '\033[0m'     #  white (normal)
cr = '\033[31m'    #  red   (errors)
cg = '\033[32m'    #  green (some highlights)
cy = '\033[33m'    #  yellow (warnings)

# Misc colors
cb = '\033[34m'    #  blue
cp = '\033[35m'    #  purple
cc = '\033[36m'    #  cyan
cgr = '\033[37m'   #  gray

# Font types
fr = '\033[0m'     #  regular
fb = '\033[1m'     #  bold
fi = '\033[3m'     #  italic

# Function to print the logo.
def prn_logo():
    # This function prints Shadow Suite's logo and a brief description.
    print(cg + "  ___|  |               |                  ___|       _) |")
    print("\\___ \\  __ \\   _` |  _` |  _ \\\\ \\  \\   / \\___ \\  |   | | __|  _ \\")
    print("      | | | | (   | (   | (   |\\ \\  \\ /        | |   | | |    __/")
    print("_____/ _| |_|\\__,_|\\__,_|\\___/  \\_/\\_/   _____/ \\__,_|_|\\__|\\___|")
    print("\nEthical Hacking Toolkit\n\n" + cw)

def prn_brief_license():
    # This function prints a brief description of the license.
    print(cg + "This program comes with ABSOLUTELY NO WARRANTY.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; type 'license' for details." + cw)

def error0001():
    # This function prints the "Invalid Input message.
    print(cr + "ERROR 0001: Invalid Input! Please check your command." + cw)

def warning0001():
    # This function is called if ShadowSuite.py is renamed.
    print(cy + "WARNING 0001: Shadow Suite has been renamed!" + cw)

def module_mode():
    # This function is called if ShadowSuite is running as module.
    print(cy + "[i] Running as module..." + cw)
