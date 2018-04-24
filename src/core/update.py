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
from core import misc
from core import error
from core import fullupdate

def full_update():
    process = "4"

    print(misc.FB + misc.FI + misc.CB + "Performing a full update..." + misc.FR + misc.CW)
    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    os.system("bash instdeps.bash")
    print(misc.CB + "Updating Shadow Suite... (2/" + process + ")\n" + misc.CW)
    fullupdate.update()
    print(misc.CB + "Installing python modules... (3/" + process + ")\n" + misc.CW)
    os.system("pip install -r python_requirements")
    print(misc.CB + "Installing perl modules... (4/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize")
    print(misc.FB + misc.FI + misc.CB + "Performing a full update... Done!" + misc.FR + misc.CW)

def deps_update():
    process = "3"

    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    os.system("bash instdeps.bash")
    print(misc.CB + "Installing python modules... (2/" + process + ")\n" + misc.CW)
    os.system("pip install -r python_requirements")
    print(misc.CB + "Installing perl modules... (3/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize")
    print(misc.FB + misc.FI + misc.CB + "Performing a dependency update... Done!" + misc.FR + misc.CW)
    
def prog_update():
    process = "1"
    
    print(misc.CB + "Updating Shadow Suite... (1/" + process + ")\n" + misc.CW)
    fullupdate.check_for_updates()
    fullupdate.update()
