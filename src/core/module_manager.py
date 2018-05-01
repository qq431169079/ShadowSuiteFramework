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

def shell(DEBUGGING, FAILSAFE, SESSION_ID):
    misc.debugging = DEBUGGING
    misc.failsafe = FAILSAFE
    while True:
        try:
            if os.geteuid() != 0:
                command = input(misc.CW + "[" + misc.CB + misc.FB + misc.FI + "Module_Manager.py" + misc.CW + misc.FR + "] $: ")
                
            else:
                command = input(misc.CW + "[" + misc.CB + misc.FB + misc.FI + "Module_Manager.py" + misc.CW + misc.FR + "] #: ")

            command = command.lower()
            if command == "help":
                print(misc.CC + misc.FB + misc.FI + "\nHELP\n" + misc.FR + misc.CW)
                print("help            :: prints this help menu.")
                print("list            :: list modules and frameworks.")
                print("use             :: use a module.")
                print("info            :: show module information.")
                print("manage          :: run module manager.")
                print("suggest         :: suggest an attack based on your criteria.")
                print("clear           :: clears the screen.")
                print("run             :: run a command from your terminal.")
                print("\n")
                print("back            :: back to Shadow Suite shell.")

            elif command == "list":
                list_module.list()

            elif command == "use":
                module_name = input(misc.CGR + "Enter the module name to use > " + misc.CW)
                logger.log(0, 'User uses ' + module_name + ' module.', 'logfile.txt', SESSION_ID)
                use_module.use(module_name)

            elif command == "info":
                miname = input(misc.CGR + "Enter the module name to view > " + misc.CW)
                logger.log(0, 'User finds ' + miname + ' module.', 'logfile.txt', SESSION_ID)
                find_module.find(miname)

            elif command == "manage":
                manage_module.manager(DEBUGGING, FAILSAFE, SESSION_ID)

            elif command == "suggest":
                criteria = input("Enter keywords separated by comma (dns, wireless, cracking) > ")
                suggest.api(criteria)



            elif command == "run":
                command_to_run = input(r"Command to run > ")
                logger.log(3, 'User run the command: ' + command_to_run, 'logfile.txt', SESSION_ID)
                os.system(command_to_run)

            elif command == "quit":
                print(error.ERROR0003)

            elif command == "exit":
                print(error.ERROR0003)

            elif command == "back":
                print("[i] Going back to Shadow Suite shell...")
                break
                
            else:
                logger.log(2, 'User entered an unknown command.', 'logfile.txt', SESSION_ID)
                print(error.ERROR0001)

        except KeyboardInterrupt:
            logger.log(1, 'CTRL+C detected...', 'logfile.txt')
            print(error.ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt', SESSION_ID)
            sys.exit(2)
