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
import core.error
import core.misc
import core.update
import core.version
import core.module_manager
# DEV 0001: The integrator() function must use this Hakku API not the bash script!
# import hakku_API

def integrator():
    print("[i] Running Hakku...")
    os.system("bash hakku_integrator")
