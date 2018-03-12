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
import core.misc
import core.error
import core.use_module
import core.logger as logger

def generate_new(cmn):
    # This is used to generate a custom module from a template via API.
    cmn = cmn.lower()
    cmn = cmn.strip()
    cmn = cmn.replace(' ', '')
    os.system("cp $PWD/core/temp.py $PWD/output/")
    os.system("mv $PWD/output/temp.py $PWD/output/" + cmn + ".py")
    os.system("echo You can now open the template located on: $PWD/output/" + cmn + ".py")

def manager():
    loop = True
    global core
    
    while loop == True:
        try:
            if os.geteuid() != 0:
                command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module Manager" + core.misc.cw + core.misc.fr + "] $: ")

            else:
                command = input(core.misc.cw + "[" + core.misc.cb + core.misc.fb + core.misc.fi + "Module Manager" + core.misc.cw + core.misc.fr + "] #: ")

            command = command.lower()

            if command == "help":
                print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr + core.misc.cw)
                print("generate new :: generate a new module template.")
                print("clear        :: clears the screen.")
                print("\n")
                print("back         :: back to Module_Manager.py shell.")

            elif command == "generate new":
                cmn = input("Enter the name of your custom module > ")
                print("Extracting template...")
                generate_new(cmn)

            elif command == "clear":
                os.system("clear")

            elif command == "quit":
                core.error.error0003()

            elif command == "exit":
                core.error.error0003()

            elif command == "back":
                print("[i] Going back to Module_Manager.py shell...")
                logger.log(0, 'User exits module manager...', 'logfile.txt')
                break

            else:
                logger.log(0, 'User entered an unknown command.', 'logfile.txt')
                core.error.error0001()

        except KeyboardInterrupt:
            logger.log(0, 'CTRL+C detected...', 'logfile.txt')
            core.error.error0002()
