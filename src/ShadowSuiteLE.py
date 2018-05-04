#!/bin/env python3
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
    logger.log(5, "SystemExit raised with error code 8.", 'logfile.txt')
    sys.exit(8)

def main():
    logger.log(0, 'Shadow Suite Linux Edition launched.', 'logfile.txt', SESSION_ID)
    PLATFORM = misc.programFunctions().get_platform()
    print()
    print(misc.LOGO) # Prints logo
    print("\n")
    print("[i] Running on " + PLATFORM + " platform.")
    print("\n")
    print(misc.BRIEF_LICENSE) # Prints a brief information about the license.
    print("\n")
    print(quote.quote())
    print("\n")
    print("[i] If you need help, type 'help'...")
    print("\n")
    if __name__ != '__main__':
        # If the program is not running independently, then a message will be shown, while
        # still allowing the user to use it.
        logger.log(3, 'Shadow Suite running as module...', 'logfile.txt', SESSION_ID)
        print(misc.MODULE_MODE_INFO)

    if misc.debugging == True:
        # If the program has been executed with an argument -d or --debug, show this info
        print("[i] Debugging mode is on")
        logger.log(3, 'Shadow Suite Debugging is on', 'logfile.txt', SESSION_ID)

    if misc.failsafe == True:
        # If the program has been executed with an argument -f or --failsafe, show this
        print("[i] Failsafe mode is on")
        logger.log(3, 'Shadow Suite Failsafe is on', 'logfile.txt', SESSION_ID)

    # This while loop enables the user to enter commands inside shadow suite without
    # needing to run the program everytime a command is entered.
    while True:
        try:
            # If os.geteuid() is equal to 0, then a terminal with # will be shown.
            # Otherwise, $ will be shown.
            if os.geteuid() != 0:
                logger.log(0, 'Running as normal user.', 'logfile.txt', SESSION_ID)
                menu_input = input("[" + misc.CB + misc.FB + misc.FI + "ShadowSuite.py" + misc.FR + misc.CW + "] $: ")

            else:
                logger.log(0, 'Running as root.', 'logfile.txt', SESSION_ID)
                menu_input = input("[" + misc.CB + misc.FB + misc.FI + "ShadowSuite.py" + misc.FR + misc.CW + "] #: ")

            menu_input.lower()
            if menu_input in ["help"]:
                logger.log(0, 'User needs help.', 'logfile.txt', SESSION_ID)
                print(misc.CC + misc.FB + misc.FI + "\nHELP\n" + misc.FR)
                print(misc.CW + "help              :: prints this help menu.")
                print("show [OPTION]     :: Shows the license/info/changelog.")
                print("update [OPTION]   :: update program/dependencies/all.")
                print("module            :: enter module shell. type \'module\' then \'help\'for details.")
                print("suggest           :: suggests a tool based on your critera.")
                print("clear             :: clears the screen.")
                print("run               :: run a command from your terminal.")
                print("\n")
                print("restart           :: restart Shadow Suite.")
                print("quit              :: quit Shadow Suite.")
                print("exit              :: same as \'quit\' command.\n")

            elif menu_input.startswith("show"):
                show_o = menu_input.split(" ")
                try:
                    if show_o[1] in ["license", "copying", "copyright"]:
                        if misc.failsafe == True:
                            print("[FAILSAFE] license not available")
                            continue

                        logger.log(0, 'User opens license via less command...', 'logfile.txt', SESSION_ID)
                        os.system("less extras/shadowsuitelicense")

                    elif show_o[1] in ["info", "information", "status", "stats"]:
                        logger.log(0, 'Users looks at the info.', 'logfile.txt', SESSION_ID)
                        print()
                        if misc.debugging == True:
                            print("Debugging: ON")

                        else:
                            print("Debugging: OFF")

                        if misc.failsafe == True:
                            print("Failsafe: ON")

                        else:
                            print("Failsafe: OFF")

                        print("Session ID: " + str(SESSION_ID))
                        print()
                        print("Current version number:   " + version.VNUMBER)
                        print("Current version type:     " + version.VTYPE)
                        print("Current version codename: " + version.VCODENAME)
                        print()
                        print("[i] To automatically update, type \'full update\' on this terminal.")
                        print("[i] To manually update, go to \'https://www.github.com/Sh4d0w-T34m/ShadowSuiteLE\' and clone the repository.")

                    elif show_o[1] == "changelog":
                        if misc.failsafe == True:
                            print("[FAILSAFE] changelog not available")

                        else:
                            logger.log(0, 'User opens changelog.', 'logfile.txt', SESSION_ID)
                            version.changelog()

                    else:
                        print()
                        print("Usage: show [OPTION]")
                        print()
                        print("license  copying  copyright         -    Shows the full license via less command.")
                        print("info  information  status  stats    -    Shows the current information of Shadow Suite.")
                        print("changelog                           -    Shows the changelog via less command.")
                        print()

                except IndexError:
                    print()
                    print("Usage: show [OPTION]")
                    print()
                    print("license  copying  copyright         -    Shows the full license via less command.")
                    print("info  information  status  stats    -    Shows the current information of Shadow Suite.")
                    print("changelog                           -    Shows the changelog via less command.")
                    print()

            elif menu_input.startswith("update"):
                update_o = menu_input.split(" ")
                try:
                    if update_o[1] in ["prog", "program"]:
                        if misc.failsafe == True:
                            print("[FAILSAFE] prog update not available")

                        else:
                            print(misc.CGR + "Fetching Shadow Suite LE from Shadow Team's repository..." + misc.CW)
                            logger.log(0, 'User performs a program update...', 'logfile.txt', SESSION_ID)
                            update.prog_update(misc.debugging)

                    elif update_o[1] in ["deps", "dependencies", "dependency"]:
                        if misc.failsafe == True:
                            print("[FAILSAFE] deps update not available")

                        else:
                            print(misc.CGR + "Downloading and installing dependencies..." + misc.CW)
                            logger.log(0, 'User performs a dependency update...', 'logfile.txt', SESSION_ID)
                            update.deps_update()

                    elif update_o[1] in ["full", "all"]:
                        if misc.failsafe == True:
                            print("[FAILSAFE] full update not available")

                        else:
                            print(misc.CGR + "Do you really want to perform a full update (y/n)?" + misc.CW)
                            full_updateinput = input(" > ")
                            if full_updateinput == "y" or full_updateinput == "Y":
                                logger.log(0, 'User performs a full update...', 'logfile.txt', SESSION_ID)
                                update.full_update(DEBUGGING)

                            elif full_updateinput == "n" or full_updateinput == "N":
                                print(misc.CR + "Full update cancelled by user..." + misc.CW)

                            else:
                                print(error.ERROR0001)

                    else:
                        print()
                        print("[i] Usage: update [OPTION]")
                        print()
                        print("prog  program                     -    Update Shadow Suite from GitHub.")
                        print("deps  dependencies  dependency    -    Update/install dependencies.")
                        print("full  all                         -    Update both Shadow Suite and dependencies.")
                        print()

                except IndexError:
                    print()
                    print("[i] Usage: update [OPTION]")
                    print()
                    print("prog  program                     -    Update Shadow Suite from GitHub.")
                    print("deps  dependencies  dependency    -    Update/install dependencies.")
                    print("full  all                         -    Update both Shadow Suite and dependencies.")
                    print()

            elif menu_input in ["module"]:
                # Runs the module_manager.py module.
                logger.log(0, 'User enters module_manager shell...', 'logfile.txt', SESSION_ID)
                module_manager.shell(misc.debugging, misc.failsafe, SESSION_ID)

            elif menu_input in ["suggest"]:
                if misc.failsafe == True:
                    print("[FAILSAFE] suggest command not available")
                    continue

                criteria = input("Enter keywords (dns, wireless, cracking) > ")
                logger.log(0, 'User want a suggestion with the criteria ' + criteria + '.', 'logfile.txt', SESSION_ID)
                suggest.api(criteria)

            elif menu_input in ["clear", "clr", "cls", "clrscrn"]:
                if misc.failsafe == True:
                    print("[FAILSAFE] clear not available")
                    continue

                misc.programFunctions().clrscrn()

            elif menu_input in ["run"]:
                if misc.failsafe == True:
                    print("[FAILSAFE] run not available")
                    continue

                command = input(r"Command to run > ")
                logger.log(3, 'User run the command: CODE[' + command + ']', 'logfile.txt', SESSION_ID)
                os.system(command)

            elif menu_input in ["back"]:
                logger.log(2, "ERROR 0004: Back cannot be used in the main module", 'logfile.txt', SESSION_ID)
                print(error.ERROR0004)

            elif menu_input in ["restart"]:
                logger.log(0, 'User restarted Shadow Suite...', 'logfile.txt', SESSION_ID)
                misc.programFunctions().clrscrn()
                misc.programFunctions().program_restart()

            elif menu_input in ["quit", "exit"]:
                print(joke.joke())
                print("Quitting Shadow Suite...\n")
                logger.log(0, 'User quits Shadow Suite...', 'logfile.txt', SESSION_ID)
                logger.log(0, "SystemExit raised with error code 0.", 'logfile.txt', SESSION_ID)
                sys.exit(0)

            else:
                logger.log(2, 'ERROR 0001: Invalid Input', 'logfile.txt', SESSION_ID)
                print(error.ERROR0001)

        except KeyboardInterrupt:
            logger.log(1, 'CTRL+C Detected...', 'logfile.txt', SESSION_ID)
            print(error.ERROR0002)
            logger.log(1, "SystemExit raise with error code 2.", 'logfile.txt', SESSION_ID)
            sys.exit(2)

        except ImportError:
            # This function is called if a module was missing.
            cr = '\033[31m'
            cw = '\033[0m'
            print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue..." + cw)
            print("==================== TRACEBACK ====================")
            traceback.print_exc()
            print("===================================================")
            logger.log(5, 'ImportError catched.', 'logfile.txt', SESSION_ID)
            logger.log(5, "SystemExit raised with error code 8.", 'logfile.txt', SESSION_ID)
            sys.exit(8)

        except SystemExit:
            logger.log(1, 'SystemExit catched.', 'logfile.txt', SESSION_ID)
            try:
                if misc.debugging == True:
                    print("[DEBUG] Deleting session file...")

                open('.last_session_exit_fail.log', 'r').read() # Try to read the file
                open('.last_session_exit_fail.log', 'r').close() # Close the file
                if PLATFORM == 'windows' or PLATFORM == 'nt':
                    os.system("del .last_session_exit_fail.log")

                else:
                    os.system('rm .last_session_exit_fail.log') # Delete the file

            except:
                if misc.debugging == True:
                    print("[DEBUG] Session file doesn't exist, now quitting...")

                pass # If file doesn't exist, do nothing. just exit

            sys.exit()

        except:
            print(error.WARNING0003)
            print()
            print("==================== TRACEBACK ====================")
            traceback.print_exc()
            print("===================================================")
            print()
            quit = misc.programFunctions().error_except()
            if quit == True:
                logger.log(0, "SystemExit raised with error code 0.", 'logfile.txt', SESSION_ID)
                sys.exit(0)

            elif quit == False:
                pass

            else:
                ValueError_msg = "ValueError: quit variable must be a boolean (True or False)."
                print(ValueError_msg)
                logger.log(0, ValueError_msg, 'logfile.txt', SESSION_ID)
                sys.exit(0)

# Starts the program
if __name__ == "__main__":
    # Check python version first before main() function execution
    req_py_version = (3, 6, 0)
    cur_py_version = sys.version_info
    str_py_version = str(sys.version_info)
    str_py_version = str_py_version.replace('sys.version_info(', '')
    str_py_version = str_py_version.replace(')', '')
    logger.log(3, 'User has python version ' + str_py_version +'.', 'logfile.txt')
    req_py_version_str = "v"
    for ver_nums in req_py_version:
        req_py_version_str = req_py_version_str + str(ver_nums) + '.'

    if cur_py_version < req_py_version:
        PythonVersionError_msg = error.ERROR0011
        PythonVersionError_msg = PythonVersionError_msg.format(req_py_version_str)
        print(PythonVersionError_msg)
        logger.log(0, PythonVersionError_msg, 'logfile.txt')
        logger.log(2, "SystemExit raised with error code 11.", 'logfile.txt')
        sys.exit(11)

    else:
        pass

    SESSION_ID = misc.programFunctions().generate_session_id()
    logger.log(3, "Generated Session ID: " + str(SESSION_ID))
    
    # Check for arguments, if any.
    NO_WARN = False
    argv = sys.argv
    sys.argv = sys.argv
    for args in sys.argv:
        arg = args.lower()

        try:
            if '-d' == arg or '--debug' == arg:
                misc.debugging = True

            if '-h' == arg or '--help' == arg:
                misc.programFunctions().clrscrn()
                print(sys.argv[0] + "\t--\t" + version.BOTH)
                print()
                print("Basic Usage:")
                print(sys.argv[0] + " [-h/--help] || [SWITCHES]")
                print()
                print("-h    --help         Show this help menu.")
                print()
                print("Troubleshooting Switches:")
                print("-d           --debug            Run Shadow Suite in debug mode; Shows logging information.")
                print("-f           --failsafe         Run Shadow Suite in failsafe mode.")
                print()
                print("Compatibility Switches:")
                print("-w           --no-warn          Disable last session exit fail warning.")
                print()
                print("Customization Switches:")
                print("-c [FILE]    --config=[FILE]    Define a custom configuration file.")
                print()
                sys.exit(0)

            # DEV0001: Wrong meaning of Failsafe :P
            if '-f' == arg or '--failsafe' == arg:
                misc.failsafe = True
                print("[i] Failsafe mode is not available this time! Sorry, dude.")
                sys.exit(0)

            if '-w' == arg or '--no-warn' == arg:
                NO_WARN = True

        except IndexError:
            pass

    # Parse configuration file (WIP)
    try:
        iterator_config = 0
        while iterator_config <= len(sys.argv):
            if sys.argv[iterator_config] == '-c':
                iterator_config += 1
                config_file = sys.argv[iterator_config]
                if os.path.exists(config_file):
                    break

                else:
                    print("[i] Invalid configuration file!")
                    sys.exit(1)

            else:
                iterator_config += 1

    except IndexError:
        pass

    try:
        iterator_config = 0
        while iterator_config <= len(sys.argv):
            if '--config=' in sys.argv[iterator_config]:
                config_filf = sys.argv[iterator_config]
                config_filf = config_filf.split("=")
                config_file = config_filf[1]
                if os.path.exists(config_file):
                    break
                
                else:
                    print("[i] Invalid configuration file!")
                    sys.exit(1)
                
            else:
                iterator_config += 1

    except IndexError:
        pass

    #

    # Checks if last session failed to exit properly
    if NO_WARN == False:
        try:
            open('.last_session_exit_fail.log', 'r').read() # Try to read the file
            open('.last_session_exit_fail.log', 'r').close() # Close the file
            print(error.WARNING0004)
            instance_warn = str(input(misc.CY + misc.FB + misc.FI + "Do you still want to run anyway? (y/n) > " + misc.FR + misc.CW))
            instance_warn = instance_warn.lower()
            if instance_warn == 'y':
                misc.programFunctions().clrscrn()
                main()

            else:
                sys.exit(0)
    
        except FileNotFoundError:
            open('.last_session_exit_fail.log', 'w').write('')
            open('.last_session_exit_fail.log', 'w').close() # Close the file
            misc.programFunctions().clrscrn()
            main()

    else:
        misc.programFunctions().clrscrn()
        main()
