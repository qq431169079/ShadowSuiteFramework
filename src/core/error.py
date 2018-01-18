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

import os
import sys
import core.misc

# ERROR 0001: Invalid Input message
# ERROR 0002: CTRL-C Detection
# ERROR 0003: Exit and Quit can't be used inside a module
# ERROR 0004: Back can't be used in the main module
# ERROR 0005: Requires root permission
# ERROR 0006: No module with that filename found
# ERROR 0007: No framework with that filename found
# ERROR 0008: A module was missing message

# WARNING 0001: 
# WARNING 0002: Feature not implemented message

    ##################################################################################
    #                                                                                #
    #                               ERROR FUNCTIONS                                  #
    #                                                                                #
    ##################################################################################

def error0001():
    # This function prints the "Invalid Input message.
    print(core.misc.cr + "ERROR 0001: Invalid Input! Please check your command.\n[i] TIP: commands are case-sensitive!\n[i] Type 'help' for commands and their descriptions." + core.misc.cw)

def error0002():
    # This function prints this message if CTRL+C is detected.
    print(core.misc.cr + "ERROR 0002: Forcing Shadow Suite to quit..." + core.misc.cw)
    sys.exit(1)

def error0003():
    # This function prints this message if 'quit' or 'exit' command is entered when inside a module.
    print(core.misc.cr + "ERROR 0003: 'exit' and 'quit' cannot be used inside a module; use 'back' instead..." + core.misc.cw)

def error0004():
    # This function is called only in ShadowSuite.py
    print(core.misc.cr + "ERROR 0004: 'back' cannot be used in the main module; use 'quit' or 'exit' instead..." + core.misc.cw)

def error0005():
    # This function is called if user device has no superuser permission but is running a
    # module that needs root.
    print(core.misc.cr + "ERROR 0005: This operation requires root permissions!\n\nPlease run as root first before proceeding. Search for \'Android Rooting\' if you are using\nShadow Suite on Android, or \'Linux Root User\' if you are running on Linux for details.\nIf you are using Windows Operating System, try to run as Administrator..." + core.misc.cw)

def error0006():
    # This function is called if no modules were found in the modules directory.
    print(core.misc.cr + "ERROR 0006: No modules with that name was found.")

def error0007():
    # This function is called if no frameworks were found in the modules directory.
    print(core.misc.cr + "ERROR 0007: No frameworks with that name was found.")

def error0008():
    # This function is called if a module was missing.
    cr = '\033[31m'
    cw = '\033[0m'

    print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download the missing module to continue..." + cw)

    ##################################################################################
    #                                                                                #
    #                              WARNING FUNCTIONS                                 #
    #                                                                                #
    ##################################################################################

def warning0001():
    # This function is vacant
    print(core.misc.cy + "WARNING 0001: " + core.misc.cw)

def warning0002():
    # This function should be called if a feature is not yet implemented.
    print(core.misc.cy + "WARNING 0002: Feature not yet implemented, cannot proceed..." + core.misc.cw)
