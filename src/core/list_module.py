#!/bin/python
# Coding=UTF-8
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
import core.misc
import core.error

def list():

    cw = '\033[0m'                       #  white  (normal)
    cb = '\033[34m'                      #  blue   (highlights)

    cg = '\033[32m'                      #  green  (Stable)
    cy = '\033[33m'                      #  yellow (Experimental)
    cr = '\033[31m'                      #  red    (Unstable)
    nyi = "\t[i] Not yet Implemented!!!"   # Not yet Implemented
    cp = '\033[35m'                      #  purple (Custom Module)
    
    # Font types
    fr = '\033[0m'                       #  regular
    fb = '\033[1m'                       #  bold
    fi = '\033[3m'                       #  italic

    print(cg + "===Shadow Suite Modules and Frameworks===\n\n" + cb)
    print(cw + "[i] The stability of the tools is color-coded:" + cw)
    print(cg + "\tStable" + cw)
    print(cy + "\tExperimental" + cw)
    print(cr + "\tUnstable" + cw)
    print(cp + "\tCustom Module\n\n" + cw)
    # DEV0002: Add new modules here, self-explanatory.
    print(cb + "\t==01-Informarion Gathering==\n" + cw)
    print(cg + "\t\tAutomater" + cw)
    print(cg + "\t\tDNSEnum" + cw)
    print(cg + "\t\tDNSMap" + cw)
    print(cg + "\t\tDNSrecon" + cw)
    print(cg + "\t\tLANScan" + cw)
    print(cg + "\t\tMetagoofil" + cw)
    print(cg + "\t\tNwrap" + cw)
    print(cg + "\t\tRed Hawk" + cw)
    print(cg + "\t\tThe Harvester" + cw)
    print()
    print(cb + "\t==02-Vulnerability Analysis==\n" + cw)
    print(cb + "\t\t==Cisco Tools==\n" + cw)
    print(cg + "\t\t\tCisco Auditing Tool" + cw)
    print(cg + "\t\t\tCisco Global Exploiter" + cw)
    print()
    print(cb + "\t\t==Fuzzing Tools==\n" + cw)
    print(cg + "\t\t\tAngry Fuzzer" + cw)
    print(cy + "\t\t\tDotDotPwn" + cw)
    print()
    print(cb + "\t\t==Stress Testing==\n" + cw)
    print(cg + "\t\t\tfl00d" + cw)
    print(cr + "\t\t\tSlowloris" + cw)
    print()
    print(cb + "\t\t==VoIP Tools==\n" + cw)
    print(nyi)
    print()
    print(cb + "\t==Integrated Frameworks==\n" + cw)
    print(cg + "\t\tHakku Framework" + cw)
    print()
    print(cb + "\t==Custom Modules==\n" + cw)
    # If you are adding a custom module, duplicate the code below:
    # print(core.misc.cp + "[MODULE NAME]")
    print(cp + "\t\tsample" + cw)
