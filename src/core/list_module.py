#!/bin/python
# Shadow Suite :: Ethical Hacking Toolkit
# Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
## This program is distributed in the hope that it will be useful,                         # but WITHOUT ANY WARRANTY; without even the implied warranty of                          # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                           # GNU General Public License for more details.                                            #                                                                                         # You should have received a copy of the GNU General Public License                       # along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import core.misc
import core.error

def list():
    print(core.misc.cg + "===Shadow Suite Modules===\n\n" + core.misc.cb)
    print(core.misc.cw + "[i] The stability of the tools is color-coded:")
    print(core.misc.cg + "\tStable")
    print(core.misc.cy + "\tExperimental")
    print(core.misc.cr + "\tUnstable")
    print(core.misc.cgr + "\tNot yet implemented")
    print(core.misc.cp + "\tCustom Module\n\n")
    print(core.misc.cb + "\t==01-Informarion Gathering==\n" + core.misc.cw)
    print(core.misc.cg + "\t\tDNSMap")
    print(core.misc.cg + "\t\tNwrap")
    print(core.misc.cgr + "\t\tRed Hawk")
    print(core.misc.cgr + "\t\tAutomater")
    print(core.misc.cgr + "\t\tDNSenum")
    print(core.misc.cgr + "\t\tDNSrecon")
    print(core.misc.cgr + "\t\tMetagoofil")
    print(core.misc.cgr + "\t\tThe Harvester")
    print(core.misc.cb + "\t==Custom Modules==\n" + core.misc.cw)
    # If you are adding a custom module, duplicate the code below:
    # print(core.misc.cp + "[MODULE NAME]")
