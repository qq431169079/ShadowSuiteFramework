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
from core import exceptions

############### ERRORS AND WARNINGS ###############

# All errors are in form of functions in a class.
# They all have the @property decorator except for errors 0011 and 0020.
# Those exceptions are normal functions, and needs parameters.

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
# ERROR 0011: Python version error (***IS A NORMAL FUNCTION!***)
# ERROR 0012: Invalid configuration file
# ERROR 0013: Wrong username or password
# ERROR 0014: Max login attempts reached.
# ERROR 0015: Path not found
# ERROR 0016: Not a valid SSF module.
# ERROR 0017: There was a problem parsing the module/package.
# ERROR 0018: Cannot uninstall the specified module.
# ERROR 0019: No notes saved.
# ERROR 0020: Unknown Fatal Error (Like WARNING 0003, but fatal) Used with Exception. (***IS A NORMAL FUNCTION!***)
# ERROR 0021: Cannot get version number from repository!
# ERROR 0022: Invalid Parameter Passed!

# WARNING 0001: Feature under dev
# WARNING 0002: Feature not implemented message
# WARNING 0003: An unknown error occured when processing your command.
# WARNING 0004: The last session of Shadow Suite Framework has failed to quit properly.
# WARNING 0005: Shadow Suite Framework will !work unless you define a custom config file
# WARNING 0006: Stopping all active services

    ##################################################################################
    #                                                                                #
    #                               ERROR FUNCTIONS                                  #
    #                                                                                #
    ##################################################################################

# This function prints the "Invalid Input message.
class errorCodes:

    def __init__(self):
        pass

    @property
    def ERROR0001(self):
        return(misc.CR + "ERROR 0001: Invalid Input! Please check your command." + misc.CW)
    @property
    def ERROR0002(self):
        return(misc.CR + "ERROR 0002: Keyboard interrupt detected..." + misc.CW)

    @property
    def ERROR0003(self):
        return(misc.CR + "ERROR 0003: 'exit' and 'quit' cannot be used inside a module; use 'back' instead..." + misc.CW)

    @property
    def ERROR0004(self):
        return(misc.CR + "ERROR 0004: 'back' cannot be used in the main module; use 'quit' or 'exit' instead..." + misc.CW)
    
    @property
    def ERROR0005(self):
        message = """ERROR 0005: {} requires root permissions!
        Please run as root first before proceeding...
        Search for 'Android Rooting' if you are using SSF on Android Systems,
        or 'Linux Root User' if you are using SSF on Linux Systems.
    
        If you are using SSF on Windows, search for 'Windows Administrator'
        for more information."""

        return(misc.CR + message.format("This operation") + misc.END)
            
    @property
    def ERROR0006(self):
        return(misc.CR + "ERROR 0006: No module with that name was found." + misc.CW)
        
    @property
    def ERROR0007(self):
        return(misc.CR + "ERROR 0007: An error occured while updating Shadow Suite Framework." + misc.CW)
        
    @property
    def ERROR0008(self):
        message = "ERROR 0008: A module is missing!\nPlease re-install/re-download {} to continue..."
        
        return(misc.CR + message.format("the missing module(s)") + misc.END)

    @property
    def ERROR0009(self):
        return(misc.CR + "ERROR 0009: The update package was not found! Maybe corrupted?" + misc.CW)

    @property
    def ERROR0010(self):
        return(misc.CR + "ERROR 0010: Cannot connect! Is it really up? Or the problem is ours? Please check." + misc.CW)

    def ERROR0011(self, pyver=''):
        message = "ERROR 0011: Python {0} or later is needed to run Shadow Suite Framework."
        if not pyver:
            raise exceptions.InvalidParameterError("The 'pyver' parameter is needed!")

        else:
            return(misc.CR + message.format(pyver) + misc.END)
            
    @property
    def ERROR0012(self):
        return(misc.CR + "ERROR 0012: Invalid configuration file!" + misc.CW)
        
    @property
    def ERROR0013(self):
        return(misc.CR + "ERROR 0013: Wrong username or password!" + misc.CW)
        
    @property
    def ERROR0014(self):
        return(misc.CR + "ERROR 0014: Max login attempts reached!" + misc.CW)
        
    @property
    def ERROR0015(self):
        message = "ERROR 0015: Path {} not found."

        return(misc.CR + message.format('') + misc.END)

    @property
    def ERROR0016(self):
        message = "ERROR 0016: {} a valid SSF module!"
        
        return(misc.CR + message.format('Not') + misc.CW)
                    
    @property
    def ERROR0017(self):
        message = "ERROR 0017: There was a problem parsing {}..."
        
        return(misc.CR + message.format('the package') + misc.END)

    @property
    def ERROR0018(self):
        message = "ERROR 0018: Cannot uninstall {}!"
        
        return(misc.CR + message.format("the specified package") + misc.END)

    @property
    def ERROR0019(self):
        return(misc.CR + "ERROR 0019: No notes saved!" + misc.CW)

    def ERROR0020(self, error_desc=''):
        if not error_desc:
            raise exceptions.InvalidParameterError("The 'error_desc' parameter is needed!")
        else:
            return(misc.CR + "ERROR 0020: A fatal error occured: {0}".format(error_desc) + misc.END)

    @property
    def ERROR0021(self):
        return(misc.CR + "ERROR 0021: Cannot get version number from repository! Please check for updates manually." + misc.END)

    @property
    def ERROR0022(self):
        return(misc.CR + "ERROR 0022: Invalid parameter has been passed!" + misc.END)

class warningCodes:
    
    def __init__(self):
        pass

    @property
    def WARNING0001(self):
        return(misc.CY + "WARNING 0001: This feature was still under development, it may contain bugs." + misc.CW)

    @property
    def WARNING0002(self):
        return(misc.CY + "WARNING 0002: Feature not yet implemented, cannot proceed..." + misc.CW)

    @property
    def WARNING0003(self):
        return(misc.CY + "WARNING 0003: An unknown error occured when processing your command." + misc.CW)

    @property
    def WARNING0004(self):
        return(misc.CY + "WARNING 0004: The last session of Shadow Suite Framework has failed to quit properly." + misc.CW)

    @property
    def WARNING0005(self):
        return(misc.CY + "WARNING 0005: Shadow Suite Framework will not work unless you define a custom configuration file!" + misc.CW)

    @property
    def WARNING0006(self):
        return(misc.CY + "WARNING 0006: Stopping all active services..." + misc.CW)
