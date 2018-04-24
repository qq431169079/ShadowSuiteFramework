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
from core import use_module
from core import logger

def generate_new(cmn):
    # This is used to generate a custom module from a template via API.
    logger.log(0, 'User generated a new module named ' + cmn, 'logfile.txt')
    if misc.failsafe == True:
        print("[FAILSAFE] called logger... (Press enter key to continue)")
        misc.programFunctions().pause(True)

    cmn = cmn.lower()
    if misc.failsafe == True:
        print("[FAILSAFE] lower-cased cmn variable's value. (Press enter key to continue)")
        misc.programFunctions().pause(True)

    cmn = cmn.strip()
    if misc.failsafe == True:
        print("[FAILSAFE] stripped value of cmn variable. (Press enter key to continue)")
        misc.programFunctions().pause(True)

    cmn = cmn.replace(' ', '')
    if misc.failsafe == True:
        print("[FAILSAFE] replaced ' ' with '' in cmn variable. (Press enter key to continue)")
        misc.programFunctions().pause(True)

    IS_WINDOWS = misc.is_windows()
    if IS_WINDOWS == False:
        os.system("cp $PWD/core/temp.py $PWD/output/")

    else:
        os.system("xcopy core/temp.py output/")

    if misc.failsafe == True:
        print("[FAILSAFE] copied core/temp.py to output/temp.py. (Press enter key to continue)")
        misc.programFunctions().pause(True)

    if IS_WINDOWS == False:
        os.system("mv $PWD/output/temp.py $PWD/output/" + cmn + ".py")

    else:
        os.system("ren output/temp.py output/" + cmn + ".py")

    if misc.failsafe == True:
        print("[FAILSAFE] renamed output/temp.py to output/$cmn.py. (Press enter key to continue)")
        misc.programFunctions().pause(True)

    print("You can now open the template located on: output/" + cmn + ".py")

def manager():
    while True:
        try:
            if os.geteuid() != 0:
                command = input(misc.CW + "[" + misc.CB + misc.FB + misc.FI + "Manage_Module.py" + misc.CW + misc.FR + "] $: ")

            else:
                command = input(misc.CW + "[" + misc.CB + misc.FB + misc.FI + "Manage_Module.py" + misc.CW + misc.FR + "] #: ")

            command = command.lower()

            if command == "help":
                print(misc.CC + misc.FB + misc.FI + "\nHELP\n" + misc.FR + misc.CW)
                print("generate     :: generate a new module template.")
                print("clear        :: clears the screen.")
                print("run          :: run a command from your terminal.")
                print("\n")
                print("back         :: back to Module_Manager.py shell.")

            elif command == "generate":
                cmn = input("Enter the name of your custom module > ")
                print("Extracting template...")
                generate_new(cmn)

            elif command == "clear":
                misc.programFunctions().clrscrn()

            elif command == "run":
                command_to_run = input(r"Command to run > ")
                logger.log(3, 'User run the command: CODE[' + command_to_run + ']', 'logfile.txt')
                os.system(command_to_run)

            elif command == "quit":
                print(error.ERROR0003)

            elif command == "exit":
                print(error.ERROR0003)

            elif command == "back":
                print("[i] Going back to Module_Manager.py shell...")
                logger.log(0, 'User exits module manager...', 'logfile.txt')
                break

            else:
                logger.log(0, 'User entered an unknown command.', 'logfile.txt')
                print(error.ERROR0001)

        except KeyboardInterrupt:
            logger.log(0, 'CTRL+C detected...', 'logfile.txt')
            print(error.ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)
