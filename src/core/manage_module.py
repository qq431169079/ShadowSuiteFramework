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
import core.misc
import core.error

def manager():
    loop = True
    
    while loop == True:
        try:
            command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module Manager" + core.misc.cw + core.misc.fr + "] $: ")

            if command == "help":
                print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr + core.misc.cw)
                print("generate new :: generate a new module template.")
                print("\n")
                print("back         :: back to Module_Manager.py shell.")

            elif command == "generate new":
                print("Extracting template...")
                os.system("cp $PWD/modules/temp.py $PWD/output/")
                os.system("echo You can now open the template located on: $PWD/output/temp.py")

            elif command == "quit":
                core.error.error0003()

            elif command == "exit":
                core.error.error0003()

            elif command == "back":
                print("[i] Going back to Module_Manager.py shell...")
                break

            else:
                core.error.error0001()

        except KeyboardInterrupt:
            core.error.error0002()
