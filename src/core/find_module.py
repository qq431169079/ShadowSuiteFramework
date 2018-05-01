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

def find(module_name):
    # DEV0001: Reconstruct this algorithm to automatically detect custom modules.
    print("searching for module named \'" + module_name + "\' in modules directory...\n\n\n")
    module_name = module_name.lower()
    
    # DEV0002: Add new tools here
    if module_name == "dnsmap":
        print("Module found!")
        import modules.dnsmap
        modules.dnsmap.module_info()

    elif module_name == "nwrap":
        print("Module found!")
        import modules.nwrap
        modules.nwrap.module_info()

    elif module_name == "red hawk":
        print("Module found!")
        import modules.red_hawk
        modules.red_hawk.module_info()

    elif module_name == "automater":
        print("Module found!")
        import modules.automater
        modules.automater.module_info()

    elif module_name == "dnsenum":
        print("Module found!")
        import modules.dnsenum
        modules.dnsenum.module_info()

    elif module_name == "dnsrecon":
        print("Module found!")
        import modules.dnsrecon
        modules.dnsrecon.module_info()

    elif module_name == "metagoofil":
        print("Module found!")
        import modules.metagoofil
        modules.metagoofil.module_info()

    elif module_name == "the harvester":
        print("Module found!")
        import modules.theharvester
        modules.theharvester.module_info()

    elif module_name == "lanscan":
        print("Module found!")
        import modules.lanscan
        modules.lanscan.module_info()

    elif module_name == "cat":
        print("Module found!")
        import modules.cat
        modules.cat.module_info()

    elif module_name == "cge":
        print("Module found!")
        import modules.cge
        modules.cge.module_info()

    elif module_name == "angryfuzzer":
        print("Module found!")
        import modules.angryfuzzer
        modules.angryfuzzer.module_info()
    
    elif module_name == "dotdotpwn":
        print("Module found!")
        import modules.dotdotpwn
        modules.dotdotpwn.module_info()

    elif module_name == "fl00d":
        print("Module found!")
        import modules.fl00d
        modules.fl00d.module_info()

    elif module_name == "slowloris":
        print("Module found!")
        import modules.slowloris
        modules.slowloris.module_info()

    elif module_name == "dtect":
        print("Module found!")
        import modules.dtect
        modules.dtect.module_info()

    elif module_name == "shellshocker":
        print("Module found!")
        import modules.shellshocker
        modules.shellshocker.module_info()

    elif module_name == "striker":
        print("Module found!")
        import modules.striker
        modules.striker.module_info()

    elif module_name == "dsss":
        print("Module found!")
        import modules.dsss
        modules.dsss.module_info()

    elif module_name == "sqlmap":
        print("Module found!")
        import modules.sqlmap
        modules.sqlmap.module_info()

    elif module_name == "hash identifier":
        print("Module found!")
        import modules.hashid
        modules.hashid.module_info()

    elif module_name == "shadow crack":
        print("Module found!")
        import modules.shadowcrack
        modules.shadowcrack.module_info()

    elif module_name == "black hydra":
        print("Module found!")
        import modules.blackhydra
        modules.blackhydra.module_info()

    elif module_name == "hash buster":
        print("Module found!")
        import modules.hashbuster
        modules.hashbuster.module_info()

    elif module_name == "cupp":
        print("Module found!")
        import modules.cupp
        modules.cupp.module_info()

    elif module_name == "les":
        print("Module found!")
        import modules.les
        modules.les.module_info()

    elif module_name == "routersploit":
        print("Module found!")
        import modules.routersploit
        modules.routersploit.module_info()

    elif module_name == "pipal":
        print("Module found!")
        import modules.pipal
        modules.pipal.module_info()

    elif module_name == "set":
        print("Module found!")
        import modules.set
        modules.set.module_info()

    elif module_name == "ipify":
        print("Module found!")
        import modules.ipify
        modules.ipify.module_info()

    elif module_name == "urlcrazy":
        print("Module found!")
        import modules.urlcrazy
        modules.urlcrazy.module_info()

    elif module_name == "weeman":
        print("Module found!")
        import modules.weeman
        modules.weeman.module_info()

    elif module_name == "ipcalc":
        print("Module found!")
        import modules.ipcalc
        modules.ipcalc.module_info()

    elif module_name == "deception":
        print("Module found!")
        import modules.deception
        modules.deception.module_info()

    elif module_name == "smt":
        print("Module found!")
        import modules.smt
        modules.smt.module_info()

    # Put the code below... Careful with the indentation! match indents of the codes
    # above to avoid errors!

    elif module_name == "sample":
        print("Module found!")
        import modules.sample
        modules.sample.module_info()

    # Hey! don't modify this thing below!
    else:
        print(error.ERROR0006)
