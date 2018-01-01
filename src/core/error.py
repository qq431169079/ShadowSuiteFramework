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

def error0001():
    # This function prints the "Invalid Input message.
    print(core.misc.cr + "ERROR 0001: Invalid Input! Please check your command.\n[i] TIP: commands are case-sensitive!" + core.misc.cw)

def warning0001():
    # This function is called if ShadowSuite.py is renamed.
    print(core.misc.cy + "WARNING 0001: Shadow Suite has been renamed!" + core.misc.cw)

def warning0002():
    # This function should be called if a feature is not yet implemented.
    print(core.misc.cy + "WARNING 0002: Feature not yet implemented, cannot proceed..." + core.misc.cw)
