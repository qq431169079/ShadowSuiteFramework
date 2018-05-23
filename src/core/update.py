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
from core import error
from core import fullupdate
import subprocess

def full_update(global_variables, DEBUGGING):
    process = "4"

    print(misc.FB + misc.FI + misc.CB + "Performing a full update..." + misc.FR + misc.CW)
    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    if sys.platform == 'windows' or sys.platform == 'nt':
        print("[i] Can't install binaries on Windows. Please install them manually.")

    else:
        subprocess.call(["bash", "instdeps.bash"]) # DEV0001: Need a new algorithm!

    print(misc.CB + "Updating Shadow Suite... (2/" + process + ")\n" + misc.CW)
    fullupdate.update(global_variables, DEBUGGING)

    print(misc.CB + "Installing python modules... (3/" + process + ")\n" + misc.CW)
    subprocess.call("pip", "install", "-r", "python_requirements") # DEV001: Also needs a new algorithm! I'm sure people are sick using this! >:(

    print(misc.CB + "Installing perl modules... (4/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize") # DEV0001: Also this!

    print(misc.FB + misc.FI + misc.CB + "Performing a full update... Done!" + misc.FR + misc.CW)

def deps_update(global_variables):
    process = "3"

    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    if sys.platform == 'windows' or sys.platform == 'nt':
        print("[i] Can't install binaries on Windows. Please install them manually.")
    
    else:
        subprocess.call(["bash", "instdeps.bash"])

    print(misc.CB + "Installing python modules... (2/" + process + ")\n" + misc.CW)
    os.system("pip install -r python_requirements")

    print(misc.CB + "Installing perl modules... (3/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize")
    print(misc.FB + misc.FI + misc.CB + "Performing a dependency update... Done!" + misc.FR + misc.CW)
    
def prog_update(global_variables, DEBUGGING):
    fullupdate.update(global_variables, DEBUGGING)
