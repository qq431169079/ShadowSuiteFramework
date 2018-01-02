#!/bin/python                                                                                                                                                                       # Shadow Suite :: Ethical Hacking Toolkit                                                 # Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>                           #                                                                                         # This program is free software: you can redistribute it and/or modify                    # it under the terms of the GNU General Public License as published by                    # the Free Software Foundation, either version 3 of the License, or                       # (at your option) any later version.                                                     #                                                                                         # This program is distributed in the hope that it will be useful,                         # but WITHOUT ANY WARRANTY; without even the implied warranty of                          # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                           # GNU General Public License for more details.                                            #                                                                                         # You should have received a copy of the GNU General Public License                       # along with this program.  If not, see <http://www.gnu.org/licenses/>

import core.misc
import core.error
import core.search_module
import core.use_module

def shell():
    loop = True

    while loop == True:
        try:
            command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module_Manager.py" + core.misc.cw + core.misc.fr + "] $: ")
            
            if command == "help":
                print("help            :: prints this help menu.")
                print("search          :: search installed module/s.")
                print("use             :: use installed module.")
                print("manage          :: run module manager.")
                print("\n")
                print("back            :: back to Shadow Suite shell.")

            elif command == "search":
                query = input(core.misc.cgr + "Enter the module name to search > " + core.misc.cw)
                core.search_module.search(query)

            elif command == "use":
                module_name = input(core.misc.cgr + "Enter the module name to use > " + core.misc.cw)
                core.use_module.use(module_name)

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
