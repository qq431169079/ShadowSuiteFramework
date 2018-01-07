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
import core.error
import core.hakku

def use(framework_name):
    
    print("searching for framework named \'" + framework_name + "\' in root directory...")

    if framework_name == "hakku":
        print("Framework found!")
        # DEV 0001: This must use the API module not the OS module!
        # TIP: Use the algorithm of calling the module in use_module.py
        core.hakku.integrator()

    else:
        core.error.error0007()
