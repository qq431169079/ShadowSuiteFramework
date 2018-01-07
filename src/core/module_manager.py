#!/bin/python                                                                                                                                                                       # Shadow Suite :: Ethical Hacking Toolkit                                                 # Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>                           #                                                                                         # This program is free software: you can redistribute it and/or modify                    # it under the terms of the GNU General Public License as published by                    # the Free Software Foundation, either version 3 of the License, or                       # (at your option) any later version.                                                     #                                                                                         # This program is distributed in the hope that it will be useful,                         # but WITHOUT ANY WARRANTY; without even the implied warranty of                          # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                           # GNU General Public License for more details.                                            #                                                                                         # You should have received a copy of the GNU General Public License                       # along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import sys
import core.misc
import core.error
import core.find_module
import core.list_module
import core.use_module
import core.use_framework
import core.manage_module

def shell():
    while True:
        try:
            if os.geteuid() != 0:
                command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module_Manager.py" + core.misc.cw + core.misc.fr + "] $: ")
                
            else:
                command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module_Manager.py" + core.misc.cw + core.misc.fr + "] #: ")
            
            if command == "help":
                print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr + core.misc.cw)
                print("help            :: prints this help menu.")
                print("list            :: list modules and frameworks.")
                print("use module      :: use a module.")
                print("module info     :: show module information.")
                print("use framework   :: use a framework")
                print("manage          :: run module manager.")
                print("\n")
                print("back            :: back to Shadow Suite shell.")

            elif command == "list":
                core.list_module.list()

            elif command == "use module":
                module_name = input(core.misc.cgr + "Enter the module name to use > " + core.misc.cw)
                core.use_module.use(module_name)

            elif command == "module info":
                miname = input(core.misc.cgr + "Enter the module name to view > " + core.misc.cw)
                core.find_module.find(miname)

            elif command == "use framework":
                framework_name = input(core.misc.cgr + "Enter the framework name to use > " + core.misc.cw)
                core.use_framework.use(framework_name)

            elif command == "framework info":
                finame = input(core.misc.cgr + "Enter the framework name to view > " + core.misc.cw)
                core.error.warning0002()

            elif command == "manage":
                core.manage_module.manager()

            elif command == "quit":
                core.error.error0003()

            elif command == "exit":
                core.error.error0003()

            elif command == "back":
                print("[i] Going back to Shadow Suite shell...")
                break
                
            else:
                core.error.error0001()

        except KeyboardInterrupt:
            core.error.error0002()
