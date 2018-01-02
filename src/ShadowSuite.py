#!/bin/python                                                                                                                                                                       # Shadow Suite :: Ethical Hacking Toolkit                                                 # Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>                           #                                                                                         # This program is free software: you can redistribute it and/or modify                    # it under the terms of the GNU General Public License as published by                    # the Free Software Foundation, either version 3 of the License, or                       # (at your option) any later version.                                                     #                                                                                         # This program is distributed in the hope that it will be useful,                         # but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                           # GNU General Public License for more details.
#                                                                                         # You should have received a copy of the GNU General Public License                       # along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import sys
import core.error
import core.misc
import core.update
import core.version
import core.module_manager

loop = True

os.system("clear")
core.misc.prn_logo()
print("\n")
core.misc.prn_brief_license()
print("\n")
print("[i] If you need help, type 'help'...")
print("\n")
if __name__ != '__main__':
    core.misc.module_mode()

while loop:
    try:
        menu_input = input("[" + core.misc.cb + core.misc.fb + core.misc.fi + "ShadowSuite.py" + core.misc.fr + core.misc.cw + "] $: ")

        if menu_input == "help":
            print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr)
            print(core.misc.cw + "help            :: prints this help menu.")
            print("license         :: opens the license file via less command.")
            print("full update     :: update Shadow Suite and install dependencies.")
            print("module          :: enter module shell. type \'module\' then \'help\'for details.")
            print("\n")
            print("quit            :: quit Shadow Suite.")
            print("exit            :: same as \'quit\' command.\n")

        elif menu_input == "license":
            print("Opening \'LICENSE\' file via less command ...")
            os.system("less LICENSE")

        elif menu_input == "full update":
            print(core.misc.cgr + "Do you really want to perform a full update (y/n)?" + core.misc.cw)
            full_updateinput = input(" > ")
            if full_updateinput == "y":
                core.update.full_update()

            elif full_updateinput == "Y":
                core.update.full_update()

            elif full_updateinput == "n":
                print(core.misc.cr + "Full update cancelled by user..." + core.misc.cw)

            elif full_updateinput == "N":
                print(core.misc.cr + "Full update cancelled by user..." + core.misc.cw)

            else:
                core.error.error0001()

        elif menu_input == "module":
            core.module_manager.shell()

        elif menu_input == "module help":
            core.module_manager.shell()

        elif menu_input == "quit":
            print("Quitting Shadow Suite...\n")
            sys.exit(0)

        elif menu_input == "exit":
            print("Quitting Shadow Suite...\n")
            sys.exit(0)

        else:
            core.error.error0001()

    except KeyboardInterrupt:
        core.error.error0002()
