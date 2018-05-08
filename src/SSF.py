#!/usr/bin/env python3
# Coding=UTF-8
# Shadow Suite Framework :: Ethical Hacking Toolkit and Framework
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
    print("[i] Importing 'os' module...")
    import os
    print("[i] Importing 'sys' module...")
    import sys
    print("[i] Importing 'traceback' module...")
    import traceback
    print("[i] Importing 'getpass' module...")
    from getpass import getpass
    print("[i] Importing 'hashlib' module...")
    import hashlib
    print("[i] Importing 'time' module...")
    import time
    print("[i] Importing 'subprocess' module...")
    import subprocess
    print("[i] Importing 'importlib' module...")
    import importlib
    print("[i] Importing 'signal' module...")
    import signal

    print()
    print("[i] Importing 'error' module...")
    from core import error
    print("[i] Importing 'misc' module...")
    from core import misc
    print("[i] Importing 'multitasking' module...")
    from core import multitasking
    print("[i] Importing 'update' module...")
    from core import update
    print("[i] Importing 'version' module...")
    from core import version
    print("[i] Importing 'suggest' module...")
    from core import suggest
    print("[i] Importing 'logger' module...")
    from core import logger
    print("[i] Importing 'joke' module...")
    from core import joke
    print("[i] Importing 'quote' module...")
    from core import quote
    print("[i] Importing 'list_module' module...")
    from core import list_module
    print("[i] Importing 'API' module...")
    import API

    print()
    print("[i] Finished Importing modules...\n")
    misc.programFunctions().pause(False)

except ImportError:
    # This function is called if a module was missing.
    cr = '\033[31m'
    cw = '\033[0m'
    print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite Framework to continue... Please make sure that required modules are installed and running properly!" + cw)
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    logger.log(5, "SystemExit raised with error code 8.", 'logfile.txt')
    sys.exit(8)

def main():
    logger.log(0, 'Shadow Suite Linux Edition launched.', 'logfile.txt', SESSION_ID)
    # Global variables
    global config_file
    global __USERNAME__
    global __USERPASS__
    global __ROOTNAME__
    global __ROOTPASS__
    global __MODULE_PATH__
    global __OUTPUT_PATH__
    global USERLEVEL
    PLATFORM = misc.programFunctions().get_platform()
    print()
    print(misc.LOGO) # Prints logo
    print("\n")
    # Informs the user on what platform Shadow Suite is running.
    print("[i] Running on " + PLATFORM + " platform.")
    print("\n")
    print(misc.BRIEF_LICENSE) # Prints a brief information about the license.
    print("\n")
    print(quote.quote()) # Print a random quote or tip.
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

    # This while loop enables the user to enter commands inside shadow suite without
    # needing to run the program everytime a command is entered.
    while True:
        try:
            # If geteuid is equal to 0, then a terminal with # will be shown.
            # Otherwise, $ will be shown.
            if misc.programFunctions().geteuid() != 0:
                logger.log(0, 'Running as normal user.', 'logfile.txt', SESSION_ID)
                menu_input = input("[" + misc.CB + misc.FB + misc.FI + "SSF.py" + misc.FR + misc.CW + "] $: ")

            else:
                logger.log(0, 'Running as root.', 'logfile.txt', SESSION_ID)
                menu_input = input("[" + misc.CB + misc.FB + misc.FI + "SSF.py" + misc.FR + misc.CW + "] #: ")

            if menu_input.lower().startswith("help"):
                logger.log(0, 'User needs help.', 'logfile.txt', SESSION_ID)
                print(misc.CC + misc.FB + misc.FI + "\nHELP\n" + misc.FR)
                print(misc.CW)
                print("help                          :: prints this help menu.")
                print("show [OPTION]                 :: Shows the license/info/changelog.")
                print("update [OPTION]               :: update program/dependencies/all.")
                print("config [OPTION]               :: Configure Shadow Suite settings; Export settings.")
                print("module [OPTION]               :: manage modules.")
                print("suggest=[CRITERIA1,CRITERIA2] :: suggests a tool based on your critera.")
                print("clear                         :: clears the screen.")
                print("run || exec [COMMAND]         :: run a command from your terminal.")
                print("\n")
                print("restart                       :: restart Shadow Suite.")
                print("quit || exit                  :: quit Shadow Suite.")
                print()

            elif menu_input.lower().startswith("show"):
                show_o = menu_input.split(" ")
                try:
                    if show_o[1].lower() in ["license", "copying", "copyright"]:
                        logger.log(0, 'User opens license via less command...', 'logfile.txt', SESSION_ID)
                        if PLATFORM == 'windows' or PLATFORM == 'nt':
                            os.system("start extras/shadowsuitelicense")

                        else:
                            os.system("less extras/shadowsuitelicense")

                    elif show_o[1].lower() in ["info", "information", "status", "stats"]:
                        logger.log(0, 'Users looks at the info.', 'logfile.txt', SESSION_ID)
                        print()
                        if misc.debugging == True:
                            print("Debugging: ON")

                        else:
                            print("Debugging: OFF")

                        print()
                        print("Current User: " + current_user)
                        print("Session ID: " + str(SESSION_ID))
                        print()
                        print("Current version number:   " + version.VNUMBER)
                        print("Current version type:     " + version.VTYPE)
                        print("Current version codename: " + version.VCODENAME)
                        print()
                        print("[i] To automatically update, type \'full update\' on this terminal.")
                        print("[i] To manually update, go to \'https://www.github.com/Sh4d0w-T34m/ShadowSuiteLE\' and clone the repository.")

                    elif show_o[1].lower() == "changelog":
                        logger.log(0, 'User opens changelog.', 'logfile.txt', SESSION_ID)
                        version.changelog()

                    elif show_o[1].lower() == "config_files":
                        try:
                            available_config_files = os.listdir('data/')
                            acf_iterator = 0
                            for config_files in available_config_files:
                                if config_files == 'config.dat':
                                    continue

                                else:
                                    acf_iterator += 1
                                    print("[" + str(acf_iterator) + "] " + config_files)

                            del acf_iterator

                        except NotImplementedError:
                            print("[SYSTEM] functionality is unavailable")

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("Usage: show [OPTION]")
                    print()
                    print("license  copying  copyright         -    Shows the full license via less command.")
                    print("info  information  status  stats    -    Shows the current information of Shadow Suite.")
                    print("changelog                           -    Shows the changelog via less command.")
                    print("config_files                        -    Lists the configuration files available.")
                    print()

            elif menu_input.lower().startswith("update"):
                update_o = menu_input.split(" ")
                try:
                    if update_o[1].lower() in ["prog", "program"]:
                        print(misc.CGR + "Fetching Shadow Suite LE from Shadow Team's repository..." + misc.CW)
                        logger.log(0, 'User performs a program update...', 'logfile.txt', SESSION_ID)
                        update.prog_update(misc.debugging)

                    elif update_o[1].lower() in ["deps", "dependencies", "dependency"]:
                        print(misc.CGR + "Downloading and installing dependencies..." + misc.CW)
                        logger.log(0, 'User performs a dependency update...', 'logfile.txt', SESSION_ID)
                        update.deps_update()

                    elif update_o[1].lower() in ["full", "all"]:
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
                        raise IndexError

                except IndexError:
                    print()
                    print("[i] Usage: update [OPTION]")
                    print()
                    print("prog  program                     -    Update Shadow Suite from GitHub.")
                    print("deps  dependencies  dependency    -    Update/install dependencies.")
                    print("full  all                         -    Update both Shadow Suite and dependencies.")
                    print()

            elif menu_input.lower().startswith("config"):
                config_o = menu_input.split(" ")
                try:
                    if config_o[1].lower() in ["username"]:
                        config_o[2] = misc.programFunctions().hash(config_o[2], 'sha256')
                        __USERNAME__ = config_o[2]
                        if __ROOTPASS__ == None or __ROOTPASS__ == "":
                            __USERNAME__ = config_o[2]
                            logger.log(3, 'User changed his username...', 'logfile.txt', SESSION_ID)
                            print("[i] Username successfully changed!")

                        else:
                            confirm_rootpass = getpass("Enter root password to continue: ")
                            confirm_rootpass = misc.programFunctions().hash(confirm_rootpass, 'sha256')
                            # print(confirm_rootpass + '\n' + __ROOTPASS__) # DEV0005: just for debugging purposes...
                            if confirm_rootpass == __ROOTPASS__:
                                __USERNAME__ = config_o[2]
                                logger.log(3, 'User changed his username...', 'logfile.txt', SESSION_ID)
                                print("[i] Username successfully changed!")
                                del confirm_rootpass

                            else:
                                logger.log(3, 'User failed to change his username... Wrong root password.', 'logfile.txt', SESSION_ID)
                                print(error.ERROR0013)
                                del confirm_rootpass

                    elif config_o[1].lower() in ["password", "passwd"]:
                        if __USERPASS__ == "" or __USERPASS__ == None:
                            new_userpass1 = getpass("Enter new password: ")
                            new_userpass2 = getpass("Confirm new password: ")
                            if new_userpass1 == new_userpass2:
                                new_userpass1 = misc.programFunctions().hash(new_userpass1, 'sha256')
                                __USERPASS__ = new_userpass1
                                logger.log(3, 'User changed his password...', 'logfile.txt', SESSION_ID)
                                print("[i] Password successfully changed!")
                            
                            else:
                                logger.log(3, 'User failed to change his password... Passwords doesn\'t match', 'logfile.txt', SESSION_ID)
                                print("[i] Passwords doesn't match!")

                        else:
                            old_userpass = getpass("Enter old password: ")
                            old_userpass = misc.programFunctions().hash(old_userpass, 'sha256')
                            if old_userpass == __USERPASS__:
                                new_userpass1 = getpass("Enter new password: ")
                                new_userpass2 = getpass("Confirm new password: ")
                                if new_userpass1 == new_userpass2:
                                    new_userpass1 = misc.programFunctions().hash(new_userpass1, 'sha256')
                                    __USERPASS__ = new_userpass1
                                    logger.log(3, 'User changed his password...', 'logfile.txt', SESSION_ID)
                                    print("[i] Password successfully changed!")

                                else:
                                    logger.log(3, 'User failed to change his username... Passwords doesn\'t match', 'logfile.txt', SESSION_ID)
                                    print("[i] Passwords doesn't match!")

                            else:
                                logger.log(3, 'User failed to change his password... Wrong username/password.', 'logfile.txt', SESSION_ID)
                                print(error.ERROR0013)

                    elif config_o[1].lower() in ["rootname"]:
                        config_o[2] = misc.programFunctions().hash(config_o[2], 'sha256')
                        if __ROOTPASS__ == None or __ROOTPASS__ == "":
                            __ROOTNAME__ = config_o[2]
                            logger.log(3, 'User changed his root username...', 'logfile.txt', SESSION_ID)
                            print("[i] Root username successfully changed!")

                        else:
                            confirm_rootpass = getpass("Enter root password to continue: ")
                            confirm_rootpass = misc.programFunctions().hash(confirm_rootpass, 'sha256')
                            if confirm_rootpass == __ROOTPASS__:
                                __ROOTNAME__ = config_o[2]
                                logger.log(3, 'User changed his root username...', 'logfile.txt', SESSION_ID)
                                print("[i] Root username successfully changed!")
                                del confirm_rootpass

                            else:
                                logger.log(3, 'User failed to change his root username... Wrong username/password.', 'logfile.txt', SESSION_ID)
                                print(error.ERROR0013)
                                del confirm_rootpass

                    elif config_o[1].lower() in ["rootpass"]:
                        if __ROOTPASS__ == "" or __ROOTPASS__ == None:
                            new_rootpass1 = getpass("Enter new root password: ")
                            new_rootpass2 = getpass("Confirm new root password: ")
                            if new_rootpass1 == new_rootpass2:
                                new_rootpass1 = misc.programFunctions().hash(new_rootpass1, 'sha256')
                                __ROOTPASS__ = new_rootpass1
                                logger.log(3, 'User changed his root password...', 'logfile.txt', SESSION_ID)
                                print("[i] Root password successfully changed!")
                            
                            else:
                                logger.log(3, 'User failed to change his root password... Passwords doesn\'t match', 'logfile.txt', SESSION_ID)
                                print("[i] Root passwords doesn't match!")

                        else:
                            old_rootpass = getpass("Enter old root password: ")
                            old_rootpass = misc.programFunctions().hash(old_rootpass, 'sha256')
                            if old_rootpass == __ROOTPASS__:
                                new_rootpass1 = getpass("Enter new root password: ")
                                new_rootpass2 = getpass("Confirm new root password: ")
                                if new_rootpass1 == new_rootpass2:
                                    new_rootpass1 = misc.programFunctions().hash(new_rootpass1, 'sha256')
                                    __ROOTPASS__ = new_rootpass1
                                    logger.log(3, 'User changed his root password...', 'logfile.txt', SESSION_ID)
                                    print("[i] Root password successfully changed!")

                                else:
                                    logger.log(3, 'User failed to change his root password... Passwords doesn\'t match.', 'logfile.txt', SESSION_ID)
                                    print("[i] Root passwords doesn't match!")

                            else:
                                logger.log(3, 'User failed to change his root password... Wrong username/password', 'logfile.txt', SESSION_ID)
                                print(error.ERROR0013)

                    elif config_o[1].lower() in ["module_path"]:
                        new_module_path = input("Enter the new module path: ")
                        if misc.programFunctions().path_exists(new_module_path):
                            if misc.programFunctions().isfolder(new_module_path):
                                __MODULE_PATH__ = new_module_path
                                logger.log(3, 'User changed the module path to ' + new_module_path + '...', 'logfile.txt', SESSION_ID)
                                print("[i] Module path set!")

                            else:
                                print(error.ERROR0015)

                        else:
                            print(error.ERROR0015)

                    elif config_o[1].lower() in ["output_path"]:
                        new_output_path = input("Enter the new output path: ")
                        if misc.programFunctions().path_exists(new_output_path):
                            if misc.programFunctions().isfolder(new_output_path):
                                __OUTPUT_PATH__ = new_output_path
                                logger.log(3, 'User changed the output path to ' + new_output_path + '...', 'logfile.txt', SESSION_ID)
                                print("[i] Output path set!")
                            
                            else:
                                print(error.ERROR0015)
                            
                        else:
                            print(error.ERROR0015)

                    elif config_o[1].lower() in ["export", "save"]:
                        config_dict = {
                                "username": __USERNAME__,
                                "userpass": __USERPASS__,
                                "rootname": __ROOTNAME__,
                                "rootpass": __ROOTPASS__,
                                "module_path": __MODULE_PATH__,
                                "output_path": __OUTPUT_PATH__
                                }
                        try:
                            open(config_file, 'r').read()
                            open(config_file, 'r').close()
                            confirm_export_overwrite = input("Do you really want to overwrite the current configuration file? (y/n) > ").lower()
                            if confirm_export_overwrite == 'y':
                                export_conf_result = API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).export_conf(config_file, config_dict)
                                if export_conf_result == True:
                                    logger.log(3, 'Current user settings successfully saved to ' + config_file + '.', 'logfile.txt', SESSION_ID)
                                    print("[i] Settings successfully saved to configuration file: \"" + config_file + "\".")

                                else:
                                    print("[i] There was a problem exporting the settings.")

                            elif confirm_export_overwrite == 'n':
                                print("[i] Saving of settings to configuration file aborted.")

                            else:
                                print("[i] Unknown answer, assuming no.")

                        except FileNotFoundError:
                            export_conf_result = API.ShadowSuiteLE(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).export_conf(config_file, config_dict)
                            if export_conf_result == True:
                                logger.log(3, 'Current user settings successfully saved to ' + config_file + '.', 'logfile.txt', SESSION_ID)
                                print("[i] Settings successfully saved to configuration file: \"" + config_file + "\".")
                            
                            else:
                                print("[i] There was a problem exporting the settings.")

                    elif config_o[1].lower() in ['generate']:
                        new_config = config_o[2]
                        if 'data/' not in new_config:
                            new_config = "data/" + new_config

                        if '.dat' not in new_config:
                            new_config = new_config + '.dat'

                        if misc.programFunctions().path_exists(new_config) and misc.programFunctions().isfile(new_config):
                            print("[i] Saving of settings to new configuration file aborted. File already exists.")
                            continue

                        else:
                            print('[i] Exporting...')
                            config_dict = {
                                    "username": __USERNAME__,
                                    "userpass": __USERPASS__,
                                    "rootname": __ROOTNAME__,
                                    "rootpass": __ROOTPASS__,
                                    "module_path": __MODULE_PATH__,
                                    "output_path": __OUTPUT_PATH__
                                    }
                            export_conf_result = API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, misc.debugging).export_conf(new_config, config_dict)
                            if export_conf_result == True:
                                logger.log(3, 'User generated new config file named ' + new_config +'.', 'logfile.txt', SESSION_ID)
                                print("[i] " + new_config + " successfully generated!")

                            else:
                                print("[i] There was a problem generating the configuration file.")

                    elif config_o[1].lower() in ['remove', 'del', 'delete']:
                        if '.dat' not in config_o[2]:
                            config_o[2] += '.dat'

                        if 'data/' in config_o[2]:
                            config_o[2] = config_o[2].replace('data/', '')

                        if config_o[2] == 'config.dat':
                            print(error.WARNING0005)
                            ask_remove_default_config = input("Do you still want to continue? (y/n) > ").lower()
                            if ask_remove_default_config == 'y':
                                os.remove('data/' + config_o[2])
                                logger.log(3, 'User removed '+ config_o[2] + ' configuration file...', 'logfile.txt', SESSION_ID)
                                print("[i] Configuration file removed succesfully!")

                            else:
                                pass

                            del ask_remove_default_config

                        else:
                            ask_remove_config = input("Do you really want to remove " + config_o[2] + "? (y/n) > ").lower()
                            if ask_remove_config == 'y':
                                os.remove('data/' + config_o[2])
                                logger.log(3, 'User removed ' + config_o[2] + ' configuration file...', 'logfile.txt', SESSION_ID)
                                print("[i] Configuration file removed successfully!")

                            else:
                                pass

                            del ask_remove_config

                    else:
                        raise IndexError

                except(IndexError, FileNotFoundError):
                    print()
                    print("[i] Usage: config [OPTION] [VALUE]")
                    print()
                    print("username [VALUE]    -    Change username.")
                    print("password | passwd   -    Change password.")
                    print("rootname [VALUE]    -    Change root username.")
                    print("rootpass            -    Change root password.")
                    print("module_path         -    Change the path where modules will be found.")
                    print("output_path         -    Change the path where module outputs will be found.")
                    print("export | save       -    Save changes to current configuration file.")
                    print("generate [FILENAME] -    Save changes to a new configuration file.")
                    print("remove [FILENAME]   -    Delete a configuration file.")
                    print()

            elif menu_input.startswith("module"):
                module_o = menu_input.split(" ")
                try:
                    if module_o[1] in ['show', 'list', 'lst', 'ls']:
                        list_module.list(__MODULE_PATH__)

                    elif module_o[1] in ['use', 'run', 'exec', 'execute']:
                        module_name = __MODULE_PATH__ + module_o[2]
                        try:
                            module_name = module_name.replace('/', '.')
                            logger.log(3, 'User used ' + module_name + '.', 'logfile.txt', SESSION_ID)
                            module = importlib.import_module(module_name)
                            module.main(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, misc.debugging)

                        except ModuleNotFoundError as modulenotfounderror_msg:
                            print("[i] " + str(modulenotfounderror_msg))

                    elif module_o[1] in ['info', 'information', 'search', 'query']:
                        module_name = __MODULE_PATH__ + module_o[2]
                        try:
                            module_name = module_name.replace('/', '.')
                            logger.log(3, 'User looks for ' + module_name + ' information.', 'logfile.txt', SESSION_ID)
                            module = importlib.import_module(module_name)
                            module.module_info()

                        except ModuleNotFoundError as modulenotfounderror_msg:
                            print("[i] " + str(modulenotfounderror_msg))

                    elif module_o[1] in ['generate', 'produce', 'new']:
                        module_name = module_o[2]
                        logger.log(0, 'User generated a new module named ' + module_name, 'logfile.txt', SESSION_ID)
                        if misc.programFunctions().is_windows() == ('windows' or 'win' or 'nt'):
                            os.system("xcopy core/temp.py output/" + module_name + ".py")

                        else:
                            os.system("cp core/temp.py output/" + module_name + ".py")

                        if misc.programFunctions().path_exists('output/' + module_name + '.py'):
                            print("[i] " + module_name + ".py successfully generated!")

                        else:
                            print(error.ERROR0015 + " (Generated module not found)")

                    elif module_o[1].startswith("install"):
                        if misc.programFunctions().path_exists(module_o[2]):
                            logger.log(3, 'User is trying to install ' + module_o[2] + ' package...', 'logfile.txt', SESSION_ID)
                            print("[i] Path found...")
                            if '.py' in module_o[2]:
                                logger.log(3, 'Parsing ' + module_o[2] + ' package...', 'logfile.txt', SESSION_ID)
                                print("[i] Parsing " + module_o[2] + '...')
                                try:
                                    parse_module = module_o[2].replace('/', '.').replace('.py', '')
                                    parser = importlib.import_module(parse_module)
                                    parser.module_info()

                                except Exception as parsingerror_msg:
                                    logger.log(3, module_o[2] + ': ' + error.ERROR0017 + "(" + str(parsingerror_msg) + ")", 'logfile.txt', SESSION_ID)
                                    print("[i] " + error.ERROR0017)
                                    print("[i] " + str(parsingerror_msg))

                                else:
                                    logger.log(3, module_o[2] + ': Parsing successful... Now installing', 'logfile.txt', SESSION_ID)
                                    print("[i] Parsing successful!")
                                    print("[i] Installing " + module_o[2] + '...')
                                    if misc.programFunctions().is_windows():
                                        os.system("xcopy " + module_o[2] + " modules/")

                                    else:
                                        os.system("cp " + module_o[2] + " modules/")

                                    module_dependencies = parser.dependencies
                                    bin_manual_install = []
                                    manual_install =[]
                                    #print(module_dependencies) # DEV0005: for debugging purposes only
                                    for deps in module_dependencies:
                                        logger.log(3, 'Installing dependency: ' + deps, 'logfile.txt', SESSION_ID)
                                        #print(deps) # DEV0005: For debugging purposes only
                                        if 'BINARY: ' in deps:
                                            deps = deps.replace('BINARY: ', '')
                                            if misc.programFunctions().is_windows():
                                                bin_manual_install += ('BINARY: ' + deps)

                                            else:
                                                if misc.programFunctions().path_exists('/usr/bin/apt'):
                                                    os.system("apt install " + deps)
                                                    continue

                                                elif misc.programFunctions().path_exists('/usr/bin/yum'):
                                                    os.system("yum install " + deps)
                                                    continue

                                                elif misc.programFunctions().path_exists('/usr/bin/pkg'):
                                                    os.system("pkg install " + deps)
                                                    continue

                                                else:
                                                    manual_install.append('BINARY: ' + deps)

                                        elif 'PYTHON: ' in deps:
                                            deps = deps.replace('PYTHON: ', '')
                                            for pip in ['pip', 'pip3.6', 'pip3']:
                                                os.system(pip + " install " + deps)

                                        elif 'PERL: ' in deps:
                                            os.system("cpan install " + deps)

                                        else:
                                            manual_install.append(deps)

                                    if manual_install != (None or [] or ""):
                                        manual_install += bin_manual_install
                                        print("[i] Can't install the following:\n")
                                        logger.log(3, 'Failed to install dependencies: ' + str(manual_install), 'logfile.txt', SESSION_ID)
                                        for ideps in manual_install:
                                            print("- " + ideps)

                                        print("\nPlease install to use the module without errors...")

                            else:
                                logger.log(3, module_o[2] + ' is not a valid SSF module.', 'logfile.txt', SESSION_ID)
                                print("[i] " + error.ERROR0016)

                        else:
                            print("[i] " + error.ERROR0015)

                    elif module_o[1].lower() in ["uninstall"]:
                        if __MODULE_PATH__ not in module_o[2]:
                            module_name = __MODULE_PATH__ +  module_o[2]

                        else:
                            module_name = module_o[2]

                        if '.py' not in module_name:
                            module_name = module_name + '.py'

                        print(module_name) # DEV0005: For debugging purposes only

                        if misc.programFunctions().path_exists(module_name):
                            confirm_uninstall = input("Do you really want to uninstall " + module_name + "? (y/n) > ")
                            if confirm_uninstall.lower() == ('y' or 'yes'):
                                logger.log(3, 'User is trying to uninstall ' + module_name + '...', 'logfile.txt', SESSION_ID)
                                print("[i] Uninstalling " + module_name + "...")
                                os.remove(module_name)
                                if misc.programFunctions().path_exists(module_name):
                                    logger.log(3, module_name + ": " + error.ERROR0018, 'logfile.txt', SESSION_ID)
                                    print("[i] " + error.ERROR0018)

                                else:
                                    logger.log(3, 'User successfully uninstalled ' + module_name, 'logfile.txt', SESSION_ID)
                                    print("[i] " + module_name + " successfully uninstalled...")

                            else:
                                print("[i] User cancelled uninstallation...")

                        else:
                            print("[i] " + error.ERROR0015 + ' (Module not found)')

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("[i] Usage: module [OPTION] [ARGUMENTS]")
                    print()
                    print("show  list  lst  ls                                -    List available modules.")
                    print("use || run || exec || execute [MODULE]             -    Use specified module.")
                    print("info || information || search || query [MODULE]    -    Show information of the specified module.")
                    print("generate || produce || new [MODULE]                -    Generate a new module template.")
                    print("install [MODULE_PATH]                              -    Install a module.")
                    print("uninstall [MODULE_PATH]                            -    Uninstall a module.")
                    print()

            elif menu_input.lower().startswith("suggest"):
                try:
                    if '=' not in menu_input:
                        raise IndexError

                    suggest_o = menu_input.split('=')
                    suggest_o[1] = suggest_o[1].lower()
                    #print(suggest_o[1]) # DEV0005: For debugging purposes only.
                    logger.log(0, 'User want a suggestion with the criteria ' + suggest_o[1] + '.', 'logfile.txt', SESSION_ID)
                    suggest.api(suggest_o[1], __MODULE_PATH__)

                except IndexError:
                    print()
                    print("Usage: suggest=CRITERIA1,CRITERIA2,CRITERIA3,...,CRITERIA4")
                    print()

            elif menu_input.lower().startswith(("clear", "clr", "cls", "clrscrn")):
                misc.programFunctions().clrscrn()

            elif menu_input.lower().startswith("run") or menu_input.lower().startswith('exec'):
                try:
                    run_o = menu_input.split(' ')
                    run_o[0] = ''
                    command = ''
                    index_error = False
                    for args in run_o:
                        command += str(args) + ' '

                    #print('|', command, '|') # DEV0005: For debugging purposes only
                    if command == (None or '' or ' '):
                        raise IndexError

                    else:
                        logger.log(3, 'User run the command: "' + command + '".', 'logfile.txt', SESSION_ID)
                        os.system(command)

                except IndexError:
                    print()
                    print("Usage: run [COMAMND] || exec [COMMAND]")
                    print()
                    print("Example: run ls")
                    print("         exec ls")
                    print()

            elif menu_input in ["back"]:
                logger.log(2, "ERROR 0004: Back cannot be used in the main module", 'logfile.txt', SESSION_ID)
                print(error.ERROR0004)

            elif menu_input in ["restart", "reboot"]:
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

def no_escape_chars(string):
    result = string.replace('\n', '').replace('\t', '')
    return result

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

    current_user = "user"
    __USERNAME__ = None
    __USERPASS__ = None
    __ROOTNAME__ = None
    __ROOTPASS__ = None

    __MODULE_PATH__ = "modules/"
    __OUTPUT_PATH__ = "output/"

    USERLEVEL = 2
    
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
                print()
                print("Compatibility Switches:")
                print("-w           --no-warn          Disable last session exit fail warning.")
                print()
                print("Customization Switches:")
                print("-c [FILE]    --config=[FILE]    Define a custom configuration file.")
                print()
                sys.exit(0)

            if '-w' == arg or '--no-warn' == arg:
                NO_WARN = True

        except IndexError:
            pass

    # Parse configuration file
    logger.log(3, 'Parsing configuration file...', 'logfile.txt', SESSION_ID)
    config_file = "data/config.dat"
    try:
        iterator_config = 0
        while iterator_config < len(sys.argv):
            if '-c' in sys.argv[iterator_config]:
                iterator_config += 1
                config_file = sys.argv[iterator_config]
                config_file = "data/" + config_file
                if os.path.exists(config_file):
                    del iterator_config
                    break

                else:
                    print(error.ERROR0012)
                    sys.exit(12)

            else:
                iterator_config += 1

    except IndexError:
        config_file = "data/config.dat"
        del iterator_config

    try:
        iterator_config = 0
        while iterator_config < len(sys.argv):
            if '--config=' in sys.argv[iterator_config]:
                config_filf = sys.argv[iterator_config]
                config_filf = config_filf.split("=")
                config_file = config_filf[1]
                config_file = "data/" + config_file
                if os.path.exists(config_file):
                    del iterator_config
                    break
                
                else:
                    print(error.ERROR0012)
                    sys.exit(12)
                
            else:
                iterator_config += 1

    except IndexError:
        config_file = "data/config.dat"
        del iterator_config

    # Reading the configuration file...
    logger.log(3, 'Using ' + config_file + " configuration file; Now reading data...", 'logfile.txt', SESSION_ID)
    try:
        config_data = open(config_file, 'r').readlines()
        open(config_file, 'r').close()
        # print(config_data) # DEV0005: For debugging purposes only#####
        new_config_data = []
        for data in config_data:
            if data.startswith("#"):
                continue

            elif "username=" in data:
                __USERNAME__ = data.replace('username=', '')
                __USERNAME__ = __USERNAME__.replace('"', '')
                __USERNAME__ = no_escape_chars(__USERNAME__)

            elif "userpass=" in data:
                __USERPASS__ = data.replace('userpass=', '')
                __USERPASS__ = __USERPASS__.replace('"', '')
                __USERPASS__ = no_escape_chars(__USERPASS__)

            elif "rootname=" in data:
                __ROOTNAME__ = data.replace('rootname=', '')
                __ROOTNAME__ = __ROOTNAME__.replace('"', '')
                __ROOTNAME__ = no_escape_chars(__ROOTNAME__)

            elif "rootpass=" in data:
                __ROOTPASS__ = data.replace('rootpass=', '')
                __ROOTPASS__ = __ROOTPASS__.replace('"', '')
                __ROOTPASS__ = no_escape_chars(__ROOTPASS__)

            elif "module_path=" in data:
                __MODULE_PATH__ = data.replace('module_path="', '')
                __MODULE_PATH__ = __MODULE_PATH__.replace('"', '')
                __MODULE_PATH__ = no_escape_chars(__MODULE_PATH__)

            elif "output_path=" in data:
                __OUTPUT_PATH__ = data.replace('output_path=', '')
                __OUTPUT_PATH__ = __OUTPUT_PATH__.replace('"', '')
                __OUTPUT_PATH__ = no_escape_chars(__OUTPUT_PATH__)

            else:
                continue

        # DEV0005: For debugging purposes only
        """
        print(config_data)
        print(__USERNAME__)
        print(__USERPASS__)
        print(__ROOTNAME__)
        print(__ROOTPASS__)
        print(__MODULE_PATH__)
        print(__OUTPUT_PATH__)
        misc.programFunctions().pause()
        """
        logger.log(3, "Someone is trying to use Shadow Suite...", 'logfile.txt')
        if __USERNAME__ == None or __USERNAME__ == "":
            pass

        else:
            if __USERPASS__ == None or __USERPASS__ == "":
                pass

            else:
                attempts = 0
                while True:
                    try:
                        misc.programFunctions().clrscrn()
                        print()
                        print(misc.LOGO)
                        print()
                        print("Attempts: " + str(attempts))
                        print()
                        print("Please login to continue...\n")
                        login_user = input("Username: ")
                        current_user = login_user
                        login_user = misc.programFunctions().hash(login_user, 'sha256')
                        login_pass = getpass()
                        login_pass = misc.programFunctions().hash(login_pass, 'sha256')
                        # print(login_user) # DEV0005
                        # print(login_pass) # DEV0005
                        if login_user == __USERNAME__ and login_pass == __USERPASS__:
                            print("[i] You are now logged in!")
                            logger.log(3, login_user + " logged in successfully on " + time.asctime() + " with " + str(attempts) + " attempts.", 'logfile.txt')
                            misc.programFunctions().pause()
                            break

                        else:
                            print(error.ERROR0013)
                            logger.log(4, login_user + " failed to log in on " + time.asctime() + " with " + str(attempts) + " attempts.", 'logfile.txt')
                            misc.programFunctions().pause()
                            if attempts < 3:
                                attempts += 1
                                continue

                            else:
                                print(error.ERROR0014 + " Now quitting...")
                                sys.exit(13)

                    except KeyboardInterrupt:
                        print(error.ERROR0002)
                        sys.exit(2)

    except IndexError:
        print(error.ERROR0012)
        sys.exit(12)

    except FileNotFoundError:
        print(error.ERROR0015)
        sys.exit(15)

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
