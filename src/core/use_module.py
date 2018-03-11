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
import sys
import core.misc
import core.error

def use(module_name):
    
    print("searching for module named \'" + module_name + "\' in modules directory...")

    module_name = module_name.lower()

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

    elif module_name == "lanscan":
        print("Module found!")
        import modules.lanscan
        modules.lanscan.main()

    elif module_name == "cat":
        print("Module found!")
        import modules.cat
        modules.cat.main()

    elif module_name == "cge":
        print("Module found!")
        import modules.cge
        modules.cge.main()

    elif module_name == "angryfuzzer":
        print("Module found!")
        import modules.angryfuzzer
        modules.angryfuzzer.main()

    elif module_name == "dotdotpwn":
        print("Module found!")
        import modules.dotdotpwn
        modules.dotdotpwn.main()

    elif module_name == "fl00d":
        print("Module found!")
        import modules.fl00d
        modules.fl00d.main()

    elif module_name == "slowloris":
        print("Module found!")
        import modules.slowloris
        modules.slowloris.main()

    elif module_name == "dtect":
        print("Module found!")
        import modules.dtect
        modules.dtect.main()

    elif module_name == "shellshocker":
        print("Module found!")
        import modules.shellshocker
        modules.shellshocker.main()

    elif module_name == "striker":
        print("Module found!")
        import modules.striker
        modules.striker.main()

    elif module_name == "dsss":
        print("Module found!")
        import modules.dsss
        modules.dsss.main()

    elif module_name == "sqlmap":
        print("Module found!")
        import modules.sqlmap
        modules.sqlmap.main()

    elif module_name == "hash identifier":
        print("Module found!")
        import modules.hashid
        modules.hashid.main()

    elif module_name == "shadow crack":
        print("Module found!")
        import modules.shadowcrack
        modules.shadowcrack.main()

    elif module_name == "black hydra":
        print("Module found!")
        import modules.blackhydra
        modules.blackhydra.main()

    elif module_name == "hash buster":
        print("Module found!")
        import modules.hashbuster
        modules.hashbuster.main()

    elif module_name == "cupp":
        print("Module found!")
        import modules.cupp
        modules.cupp.main()

    # Put the code below... Careful with the indentation! match indents of the codes
    # above to avoid errors!

    elif module_name == "sample":
        print("Module found!")
        import modules.sample
        modules.sample.main()

    # Hey! don't modify this thing below!
    else:
        core.error.error0006()
