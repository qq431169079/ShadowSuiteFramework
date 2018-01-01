#!/bin/python

import os
import sys
import core.error
import core.misc
import core.update

loop = True

os.system("clear")
core.misc.prn_logo()
core.misc.prn_brief_license()
print("\n")
if __name__ != '__main__':
    core.misc.module_mode()

while loop:
    try:
        menu_input = input("[" + core.misc.cb + core.misc.fb + core.misc.fi + "ShadowSuite.py" + core.misc.fr + core.misc.cw + "] $: ")

        if menu_input == "help":
            print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr)
            print(core.misc.cw + "help        :: prints this help menu.")
            print("license     :: opens the license file via less command.")
            print("full update :: update Shadow Suite and install dependencies.")
            print("\n")
            print("quit        :: quit Shadow Suite.\n")

        elif menu_input == "license":
            print("Opening \'LICENSE\' file via less command ...")
            os.system("less LICENSE")

        elif menu_input == "full update":
            print(core.misc.cy + "Do you really want to perform a full update (y/n)?" + core.misc.cw)
            full_updateinput = input(" > ")
            if full_updateinput == "y":
                core.update.full_update()

            elif full_updateinput == "Y":
                core.update.full_update()

            else:
                print(core.misc.cy + "Full update cancelled by user..." + core.misc.cw)

        elif menu_input == "quit":
            print("Quitting Shadow Suite...\n")
            sys.exit(0)

        else:
            core.misc.error0001()

    except KeyboardInterrupt:
        print("Forcing Shadow Suite to quit...\n")
        sys.exit(0)
