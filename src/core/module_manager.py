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
from core import find_module
from core import list_module
from core import use_module
from core import manage_module
from core import suggest
from core import logger

def shell():
    while True:
        try:
            if os.geteuid() != 0:
                command = input(misc.cw + "[" + misc.cb + misc.fb + misc.fi + "Module_Manager.py" + misc.cw + misc.fr + "] $: ")
                
            else:
                command = input(misc.cw + "[" + misc.cb + misc.fb + misc.fi + "Module_Manager.py" + misc.cw + misc.fr + "] #: ")

            command = command.lower()
            
            if command == "help":
                print(misc.cc + misc.fb + misc.fi + "\nHELP\n" + misc.fr + misc.cw)
                print("help            :: prints this help menu.")
                print("list            :: list modules and frameworks.")
                print("use             :: use a module.")
                print("info            :: show module information.")
                print("manage          :: run module manager.")
                print("suggest         :: suggest an attack based on your criteria.")
                print("clear           :: clears the screen.")
                print("\n")
                print("back            :: back to Shadow Suite shell.")

            elif command == "list":
                list_module.list()

            elif command == "use":
                module_name = input(misc.cgr + "Enter the module name to use > " + misc.cw)
                logger.log(0, 'User uses ' + module_name + ' module.', 'logfile.txt')
                use_module.use(module_name)

            elif command == "info":
                miname = input(misc.cgr + "Enter the module name to view > " + misc.cw)
                logger.log(0, 'User finds ' + miname + ' module.', 'logfile.txt')
                find_module.find(miname)

            elif command == "manage":
                manage_module.manager()

            elif command == "suggest":
                criteria = input("Enter keywords separated by comma (dns, wireless, cracking) > ")
                suggest.api(criteria)

            elif command == "clear":
                os.system("clear")

            elif command == "quit":
                print(error.error0003)

            elif command == "exit":
                print(error.error0003)

            elif command == "back":
                print("[i] Going back to Shadow Suite shell...")
                break
                
            else:
                logger.log(2, 'User entered an unknown command.', 'logfile.txt')
                print(error.error0001)

        except KeyboardInterrupt:
            logger.log(1, 'CTRL+C detected...', 'logfile.txt')
            print(error.error0002)
            sys.exit(1)
