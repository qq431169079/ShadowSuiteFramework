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
    print("Importing 'os' module...")
    import os
    print("Importing 'sys' module...")
    import sys
    print("Importing 'traceback' module...")
    import traceback
    print("Importing 'error' module...")
    from core import error
    print("Importing 'misc' module...")
    from core import misc
    print("Importing 'update' module...")
    from core import update
    print("Importing 'version' module...")
    from core import version
    print("Importing 'module_manager' module...")
    from core import module_manager
    print("Importing 'suggest' module...")
    from core import suggest
    print("Importing 'logger' module...")
    from core import logger
    print("Importing 'joke' module...")
    from core import joke
    print("Importing 'quote' module...")
    from core import quote
    print("Finished Importing modules...\n")
    misc.programFunctions().pause(False)

except ImportError:
    # This function is called if a module was missing.
    cr = '\033[31m'
    cw = '\033[0m'
    print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue... Please make sure that required modules are installed and running properly!" + cw)
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    sys.exit(2)

def main():
    logger.log(0, 'Shadow Suite Linux Edition launched.', 'logfile.txt')
    print()
    print(misc.logo) # Prints logo
    print("\n")
    print(misc.brief_license) # Prints a brief information about the license.
    print("\n")
    print(quote.quote())
    print("\n")
    print("[i] If you need help, type 'help'...")
    print("\n")
    if __name__ != '__main__':
        # If the program is not running independently, then a message will be shown, while
        # still allowing the user to use it.
        logger.log(0, 'Shadow Suite running as module...', 'logfile.txt')
        print(misc.module_mode)

    # This while loop enables the user to enter commands inside shadow suite without
    # needing to run the program everytime a command is entered.
    while True:
        try:
            # If os.geteuid() is equal to 0, then a terminal with # will be shown.
            # Otherwise, $ will be shown.
            if os.geteuid() != 0:
                logger.log(0, 'Running as normal user.', 'logfile.txt')
                menu_input = input("[" + misc.cb + misc.fb + misc.fi + "ShadowSuite.py" + misc.fr + misc.cw + "] $: ")
            else:
                logger.log(0, 'Running as root.', 'logfile.txt')
                menu_input = input("[" + misc.cb + misc.fb + misc.fi + "ShadowSuite.py" + misc.fr + misc.cw + "] #: ")

            menu_input.lower()

            if menu_input == "help":
                logger.log(0, 'User needs help.', 'logfile.txt')
                print(misc.cc + misc.fb + misc.fi + "\nHELP\n" + misc.fr)
                print(misc.cw + "help              :: prints this help menu.")
                print("license           :: opens the license file via less command.")
                print("info              :: prints a brief information about Shadow Suite.")
                print("prog update       :: update Shadow Suite.")
                print("deps update       :: update dependency files.")
                print("full update       :: update Shadow Suite and install dependencies.")
                print("changelog         :: shows the changelog from the previous updates.")
                print("module            :: enter module shell. type \'module\' then \'help\'for details.")
                print("suggest           :: suggests a tool based on your critera.")
                print("clear             :: clears the screen.")
                print("\n")
                print("restart           :: restart Shadow Suite.")
                print("quit              :: quit Shadow Suite.")
                print("exit              :: same as \'quit\' command.\n")

            elif menu_input == "license":
                print("Opening \'LICENSE\' file via less command ...")
                logger.log(0, 'User opens license via less command...', 'logfile.txt')
                os.system("less extras/shadowsuitelicense")

            elif menu_input == "info":
                logger.log(0, 'Users looks at the info.', 'logfile.txt')
                print()
                print("The current version number of this program is: " + version.vnumber)
                print()
                print("The current version type of this program is: " + version.vtype)
                print()
                print("The current version codename of this program is: " + version.vcodename)
                print()
                print("To automatically update, type \'full update\' on this terminal.\n")
                print("To manually update, go to \'https://www.github.com/Sh4d0w-T34m/ShadowSuiteLE\' and clone the repository.")

            elif menu_input == "prog update":
                print(misc.cgr + "Fetching Shadow Suite from Shadow Team's repository..." + misc.cw)
                logger.log(0, 'User performs a program update...', 'logfile.txt')
                update.prog_update()

            elif menu_input == "deps update":
                print(misc.cgr + "Downloading and installing dependencies..." + misc.cw)
                logger.log(0, 'User performs a dependency update...', 'logfile.txt')
                update.deps_update()

            elif menu_input == "full update":
                print(misc.cgr + "Do you really want to perform a full update (y/n)?" + misc.cw)
                full_updateinput = input(" > ")
                if full_updateinput == "y" or full_updateinput == "Y":
                    logger.log(0, 'User performs a full update...', 'logfile.txt')
                    update.full_update()

                elif full_updateinput == "n" or full_updateinput == "N":
                    print(misc.cr + "Full update cancelled by user..." + misc.cw)

                else:
                    print(error.error0001)

            elif menu_input == "changelog":
                logger.log(0, 'User opens changelog.', 'logfile.txt')
                version.changelog()

            elif menu_input == "module":
                # Runs the module_manager.py module.
                logger.log(0, 'User enters module_manager shell...', 'logfile.txt')
                module_manager.shell()

            elif menu_input == "suggest":
                criteria = input("Enter keywords separated by comma (dns, wireless, cracking) > ")
                suggest.api(criteria)

            elif menu_input == "clear":
                misc.programFunctions().clrscrn()

            elif menu_input == "back":
                logger.log(2, 'ERROR 0004: Back can\'t be used in the main module', 'logfile.txt')
                print(error.error0004)

            elif menu_input == "restart":
                logger.log(0, 'User restarted Shadow Suite...', 'logfile.txt')
                os.system("clear")
                misc.programFunctions().program_restart()

            elif menu_input == "quit":
                print(joke.joke())
                print("Quitting Shadow Suite...\n")
                logger.log(0, 'User quits Shadow Suite...', 'logfile.txt')
                sys.exit()

            elif menu_input == "exit":
                print(joke.joke())
                print("Quitting Shadow Suite...\n")
                logger.log(0, 'User exits Shadow Suite...', 'logfile.txt')
                sys.exit()

            else:
                logger.log(2, 'ERROR 0001: Invalid Input', 'logfile.txt')
                print(error.error0001)

        except KeyboardInterrupt:
            logger.log(1, 'CTRL+C Detected...', 'logfile.txt')
            print(error.error0002)
            sys.exit()

        except ImportError:
            # This function is called if a module was missing.
            cr = '\033[31m'
            cw = '\033[0m'
            print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue..." + cw)
            print("==================== TRACEBACK ====================")
            traceback.print_exc()
            print("===================================================")
            logger.log(2, 'ImportError catched.', 'logfile.txt')
            sys.exit()

        except SystemExit:
            logger.log(2, 'SystemExit catched.', 'logfile.txt')
            sys.exit(0)

        except:
            print(error.warning0003)
            quit = misc.programFunctions().error_except()
            if quit == True:
                sys.exit(0)

            elif quit == False:
                pass

            else:
                ValueError_msg = "ValueError: quit variable must be a boolean (True or False)."
                print(ValueError_msg)
                logger.log(0, ValueError_msg, 'logfile.txt')
                sys.exit(0)

# Starts the program
if __name__ == "__main__":
    # Check python version first before main() function execution
    req_py_version = (3, 6, 4)
    cur_py_version = sys.version_info
    logger.log(0, 'User has python version ' + '.', 'logfile.txt')
    if cur_py_version < req_py_version:
        PythonVersionError_msg = 'PythonVersionError: Python 3.6.4 or greater is recommended. Now Quitting...'
        print(PythonVersionError_msg)
        logger.log(0, PythonVersionError_msg, 'logfile.txt')
        sys.exit(2)

    else:
        misc.programFunctions().clrscrn()
        main()
