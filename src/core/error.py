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
from core import misc

# ERROR 0001: Invalid Input message
# ERROR 0002: CTRL+C Detection
# ERROR 0003: Exit and Quit can't be used inside a module
# ERROR 0004: Back can't be used in the main module
# ERROR 0005: Requires root permission
# ERROR 0006: No module with that filename found
# ERROR 0007: An error occured while updating Shadow Suite.
# ERROR 0008: A module was missing message
# ERROR 0009: Update package not found
# ERROR 0010: Connection Error

# WARNING 0001: Feature under dev
# WARNING 0002: Feature not implemented message

    ##################################################################################
    #                                                                                #
    #                               ERROR FUNCTIONS                                  #
    #                                                                                #
    ##################################################################################

# This function prints the "Invalid Input message.
error0001 = misc.cr + "ERROR 0001: Invalid Input! Please check your command.\n[i] TIP: commands are case-sensitive!\n[i] Type 'help' for commands and their descriptions." + misc.cw

# This function prints this message if CTRL+C is detected.
error0002 = misc.cr + "ERROR 0002: Forcing Shadow Suite to quit..." + misc.cw

# This function prints this message if 'quit' or 'exit' command is entered when inside a module.
error0003 = misc.cr + "ERROR 0003: 'exit' and 'quit' cannot be used inside a module; use 'back' instead..." + misc.cw

# This function is called only in ShadowSuite.py
error0004 = misc.cr + "ERROR 0004: 'back' cannot be used in the main module; use 'quit' or 'exit' instead..." + misc.cw

# This function is called if user device has no superuser permission but is running a module that needs root.
error0005 = misc.cr + "ERROR 0005: This operation requires root permissions!\n\nPlease run as root first before proceeding. Search for \'Android Rooting\' if you are using\nShadow Suite LE on Android, or \'Linux Root User\' if you are running on Linux for details.\nIf you are using Windows Operating System, try to run as Administrator..." + misc.cw

# This function is called if no modules were found in the modules directory.
error0006 = misc.cr + "ERROR 0006: No module with that name was found." + misc.cw

# Vacant
error0007 = misc.cr + "ERROR 0007: An error occured while updating Shadow Suite." + misc.cw

# This function is called if a module was missing
error0008 = "ERROR 0008: A module is missing!\nPlease re-install/re-download the missing module to continue..."

# This is called if the update package is not found.
error0009 = "ERROR 0009: The update package was not found! Maybe corrupted?"

# This is called if we need internet but there is no internet connection.
error0010 = "ERROR 0010: Cannot connect! Is it really up? Or the problem is ours? Please check."

    ##################################################################################
    #                                                                                #
    #                              WARNING FUNCTIONS                                 #
    #                                                                                #
    ##################################################################################

# This function is vacant
warning0001 = misc.cy + "WARNING 0001: This feature was still under development, it may contain bugs." + misc.cw

# This function should be called if a feature is not yet implemented.
warning0002 = misc.cy + "WARNING 0002: Feature not yet implemented, cannot proceed..." + misc.cw
