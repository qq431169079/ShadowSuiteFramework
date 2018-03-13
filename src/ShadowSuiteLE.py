#!/bin/env python
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

# Import Python and Core modules to run properly
try:
    import os
    import sys
    import core.error
    import core.misc
    import core.update
    import core.version
    import core.module_manager
    import core.suggest
    import core.logger as logger
    import core.joke
    import core.quote

except ImportError:
    # This function is called if a module was missing.
    cr = '\033[31m'
    cw = '\033[0m'
    print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue... Please make sure that required modules are installed and running properly!" + cw)
    sys.exit(2)

def main():
    logger.log(0, 'Shadow Suite launched...', 'logfile.txt')
    print("\n\n\n\n\n") # Creates five blank lines / new lines / line breaks / whatever you wanna call it.
    core.misc.prn_logo() # Prints logo
    print("\n")
    core.misc.prn_brief_license() # Prints a brief information about the license.
    print("\n")
    core.quote.quote()
    print("\n")
    print("[i] If you need help, type 'help'...")
    print("\n")
    if __name__ != '__main__':
        # If the program is not running independently, then a message will be shown, while
        # still allowing the user to use it.
        logger.log(0, 'Shadow Suite running as module...', 'logfile.txt')
        core.misc.module_mode()

    # This while loop enables the user to enter commands inside shadow suite without
    # needing to run the program everytime a command is entered.
    while True:
        try:
            # If os.geteuid() is equal to 0, then a terminal with # will be shown.
            # Otherwise, $ will be shown.
            if os.geteuid() != 0:
                logger.log(0, 'Running as normal user...', 'logfile.txt')
                menu_input = input("[" + core.misc.cb + core.misc.fb + core.misc.fi + "ShadowSuite.py" + core.misc.fr + core.misc.cw + "] $: ")
            else:
                logger.log(0, 'Running as root...', 'logfile.txt')
                menu_input = input("[" + core.misc.cb + core.misc.fb + core.misc.fi + "ShadowSuite.py" + core.misc.fr + core.misc.cw + "] #: ")

            menu_input.lower()

            if menu_input == "help":
                print(core.misc.cc + core.misc.fb + core.misc.fi + "\nHELP\n" + core.misc.fr)
                print(core.misc.cw + "help              :: prints this help menu.")
                print("license           :: opens the license file via less command.")
                print("info              :: prints a brief information about Shadow Suite.")
                print("prog update       :: update Shadow Suite.")
                print("deps update       :: update dependency files.")
                print("full update       :: update Shadow Suite and install dependencies.")
                print("changelog         :: shows the changelog from the previous three updates.")
                print("module            :: enter module shell. type \'module\' then \'help\'for details.")
                print("suggest           :: suggest a tool based on your critera.")
                print("clear             :: clears the screen.")
                print("\n")
                print("restart           :: restart Shadow Suite.")
                print("quit              :: quit Shadow Suite.")
                print("exit              :: same as \'quit\' command.\n")

            elif menu_input == "license":
                print("Opening \'LICENSE\' file via less command ...")
                os.system("less extras/shadowsuitelicense")

            elif menu_input == "info":
                print()
                print("The current version number of this program is: " + core.version.vnumber)
                print()
                print("The current version type of this program is: " + core.version.vtype)
                print()
                print("The current version codename of this program is: " + core.version.vcodename)
                print()
                print("To automatically update, type \'full update\' on this terminal.\n")
                print("To manually update, go to \'https://www.github.com/Sh4d0w-T34m/ShadowSuiteLE\' and clone the repository.")

            elif menu_input == "prog update":
                print(core.misc.cgr + "Fetching Shadow Suite from Shadow Team's repository..." + core.misc.cw)
                logger.log(0, 'User performs a program update...', 'logfile.txt')
                core.update.prog_update()

            elif menu_input == "deps update":
                print(core.misc.cgr + "Downloading and installing dependencies..." + core.misc.cw)
                logger.log(0, 'User performs a dependency update...', 'logfile.txt')
                core.update.deps_update()

            elif menu_input == "full update":
                print(core.misc.cgr + "Do you really want to perform a full update (y/n)?" + core.misc.cw)
                full_updateinput = input(" > ")
                if full_updateinput == "y" or full_updateinput == "Y":
                    logger.log(0, 'User performs a full update...', 'logfile.txt')
                    core.update.full_update()

                elif full_updateinput == "n" or full_updateinput == "N":
                    print(core.misc.cr + "Full update cancelled by user..." + core.misc.cw)

                else:
                    core.error.error0001()

            elif menu_input == "changelog":
                core.version.changelog()

            elif menu_input == "module":
                # Runs the module_manager.py module.
                logger.log(0, 'User enters module_manager shell...', 'logfile.txt')
                core.module_manager.shell()

            elif menu_input == "suggest":
                criteria = input("Enter keywords separated by comma (dns, wireless, cracking) > ")
                core.suggest.api(criteria)

            elif menu_input == "clear":
                os.system("clear")

            elif menu_input == "back":
                logger.log(2, 'ERROR 0004: Back can\'t be used in the main module', 'logfile.txt')
                core.error.error0004()

            elif menu_input == "restart":
                logger.log(0, 'User restarted Shadow Suite...', 'logfile.txt')
                os.system("clear")
                core.misc.program_restart()

            elif menu_input == "quit":
                core.joke.joke()
                print("Quitting Shadow Suite...\n")
                logger.log(0, 'User quits Shadow Suite...', 'logfile.txt')
                sys.exit(0)

            elif menu_input == "exit":
                core.joke.joke()
                print("Quitting Shadow Suite...\n")
                logger.log(0, 'User exits Shadow Suite...', 'logfile.txt')
                sys.exit(0)

            else:
                logger.log(2, 'ERROR 0001: Invalid Input', 'logfile.txt')
                core.error.error0001()

        except KeyboardInterrupt:
            logger.log(1, 'CTRL+C Detected...', 'logfile.txt')
            core.error.error0002()

        except ImportError:
            # This function is called if a module was missing.
            cr = '\033[31m'
            cw = '\033[0m'
            print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue..." + cw)
            sys.exit(2)

# Starts the program
if __name__ == "__main__":
    # Check python version first before main() function execution
    req_py_version = (3, 6, 4)
    cur_py_version = sys.version_info
    if cur_py_version < req_py_version:
        print('ERROR: Python 3.6.4 or greater is recommended. Now Quitting...')
        sys.exit()

    else:
        main()
