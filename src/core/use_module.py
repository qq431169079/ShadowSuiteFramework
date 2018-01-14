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

def use(module_name):
    
    print("searching for module named \'" + module_name + "\' in modules directory...")

    if module_name == "dnsmap":
        print("Module found!")
        import modules.dnsmap
        modules.dnsmap.main()

    elif module_name == "nwrap":
        print("Module found!")
        import modules.nwrap
        modules.nwrap.main()

    elif module_name == "red hawk":
        print("Module found!")
        import modules.red_hawk
        modules.red_hawk.main()

    elif module_name == "automater":
        print("Module found!")
        import modules.automater
        modules.automater.main()

    elif module_name == "dnsenum":
        print("Module found!")
        import modules.dnsenum
        modules.dnsenum.main()

    elif module_name == "dnsrecon":
        print("Module found!")
        import modules.dnsrecon
        modules.dnsrecon.main()

    elif module_name == "metagoofil":
        print("Module found!")
        import modules.metagoofil
        modules.metagoofil.main()

    elif module_name == "the harvester":
        print("Module found!")
        import modules.theharvester
        modules.theharvester.main()

    # Put the code below... Careful with the indentation! match indents of the codes
    # above to avoid errors!

    elif module_name == "sample":
        print("Module found!")
        import modules.sample
        modules.sample.main()

    # Hey! don't modify this thing below!
    else:
        core.error.error0006()
