#!/usr/bin/env python3
# Coding=UTF-8
# Shadow Suite Framework :: Ethical Hacking Toolkit and Framework
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

############### ERRORS AND WARNINGS ###############

# ERROR 0001: Invalid Input message
# ERROR 0002: CTRL+C Detection
# ERROR 0003: Exit and Quit can't be used inside a module
# ERROR 0004: Back can't be used in the main module
# ERROR 0005: Requires root permission
# ERROR 0006: No module with that filename found
# ERROR 0007: An error occured while updating Shadow Suite Framework.
# ERROR 0008: A module was missing message
# ERROR 0009: Update package not found
# ERROR 0010: Connection Error
# ERROR 0011: Python version error (Needs string formatting)
# ERROR 0012: Invalid configuration file
# ERROR 0013: Wrong username or password
# ERROR 0014: Max login attempts reached.
# ERROR 0015: Path not found
# ERROR 0016: Not a valid SSF module.
# ERROR 0017: There was a problem parsing the module/package.
# ERROR 0018: Cannot uninstall the specified module.

# WARNING 0001: Feature under dev
# WARNING 0002: Feature not implemented message
# WARNING 0003: An unknown error occured when processing your command.
# WARNING 0004: The last session of Shadow Suite Framework has failed to quit properly.
# WARNING 0005: Shadow Suite Framework will !work unless you define a custom config file

    ##################################################################################
    #                                                                                #
    #                               ERROR FUNCTIONS                                  #
    #                                                                                #
    ##################################################################################

# This function prints the "Invalid Input message.
ERROR0001 = misc.CR + "ERROR 0001: Invalid Input! Please check your command." + misc.CW

# This function prints this message if CTRL+C is detected.
ERROR0002 = misc.CR + "ERROR 0002: Keyboard interrupt detected..." + misc.CW

# This function prints this message if 'quit' or 'exit' command is entered when inside a module.
ERROR0003 = misc.CR + "ERROR 0003: 'exit' and 'quit' cannot be used inside a module; use 'back' instead..." + misc.CW

# This function is called only in ShadowSuite.py
ERROR0004 = misc.CR + "ERROR 0004: 'back' cannot be used in the main module; use 'quit' or 'exit' instead..." + misc.CW

# This function is called if user device has no superuser permission but is running a module that needs root.
ERROR0005 = misc.CR + "ERROR 0005: This operation requires root permissions!\n\nPlease run as root first before proceeding. Search for \'Android Rooting\' if you are using\nShadow Suite Framework on Android, or \'Linux Root User\' if you are running on Linux for details.\nIf you are using Windows Operating System, try to run as Administrator..." + misc.CW

# This function is called if no modules were found in the modules directory.
ERROR0006 = misc.CR + "ERROR 0006: No module with that name was found." + misc.CW

# Error while updating Shadow Suite Framework
ERROR0007 = misc.CR + "ERROR 0007: An error occured while updating Shadow Suite Framework." + misc.CW

# This function is called if a module was missing
ERROR0008 = "ERROR 0008: A module is missing!\nPlease re-install/re-download the missing module/s to continue..."

# This is called if the update package is not found.
ERROR0009 = misc.CR + "ERROR 0009: The update package was not found! Maybe corrupted?" + misc.CW

# This is called if we need internet but there is no internet connection.
ERROR0010 = misc.CR + "ERROR 0010: Cannot connect! Is it really up? Or the problem is ours? Please check." + misc.CW

# This is called if python version of user doesn't meet the required version.
ERROR0011 = "ERROR 0011: Python {0} or later is needed to run Shadow Suite Framework."

# This is called if the configuration file is invalid.
ERROR0012 = misc.CR + "ERROR 0012: Invalid configuration file!" + misc.CW

# This is called if the username or password is wrong.
ERROR0013 = misc.CR + "ERROR 0013: Wrong username or password!" + misc.CW

# This is called if max attempts of login fail reached.
ERROR0014 = misc.CR + "ERROR 0014: Max login attempts reached!" + misc.CW

# This is called if path is not found.
ERROR0015 = misc.CR + "ERROR 0015: Path not found." + misc.CW

# This is called if the module user is trying to install is not a python script.
ERROR0016 = misc.CR + "ERROR 0016: Not a valid SSF module!" + misc.CW

# This is called if the module user is trying to install has encountered an error.
ERROR0017 = misc.CR + "ERROR 0017: There was a problem Parsing the pakcage..." + misc.CW

# This is called if the module to uninstall can't be removed.
ERROR0018 = misc.CR + "ERROR 0018: Cannot uninstall the specified package!" + misc.CW

    ##################################################################################
    #                                                                                #
    #                              WARNING FUNCTIONS                                 #
    #                                                                                #
    ##################################################################################

# This function is called when feature was still under development.
WARNING0001 = misc.CY + "WARNING 0001: This feature was still under development, it may contain bugs." + misc.CW

# This function should be called if a feature is not yet implemented.
WARNING0002 = misc.CY + "WARNING 0002: Feature not yet implemented, cannot proceed..." + misc.CW

# This function is called when an error occured when processing your command.
WARNING0003 = misc.CY + "WARNING 0003: An unknown error occured when processing your command." + misc.CW

# This is called if another instance of Shadow Suite is currently running...
WARNING0004 = misc.CY + "WARNING 0004: The last session of Shadow Suite Framework has failed to quit properly." + misc.CW

WARNING0005 = misc.CY + "WARNING 0005: Shadow Suite Framework will not work unless you define a custom configuration file!" + misc.CW
