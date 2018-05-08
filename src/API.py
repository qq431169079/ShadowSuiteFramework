#!usr/bin/env python3
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

# This Application Programming Interface (API) is meantly built for
# Shadow Suite Framework's custom modules. This may be used to integrate
# with Shadow Suite Framework's features.

try:
    # Python modules
    import os
    import sys
    import traceback
    import time

    # Shadow Suite modules
    from core import error
    # error calling
    #      
    #      (Replace * with error number. See core/error.py for details.)
    #      error = API.error.ERROR****
    #
    #      (Replace * with warning number. See core/error.py for details.)
    #      error = API.error.WARNING****
    #
    from core import list_module
    from core import misc
    # misc calling
    #
    #      (Prints Shadow Suite logo and version.)
    #      print(API.misc.LOGO)
    #
    #      (Prints "module mode" message.)
    #      print(API.misc.MODULE_MODE_INFO)
    #
    #      (Restarts Shadow Suite.)
    #      API.misc.programFunctions().restart_program()
    #
    from core import suggest
    from core import update
    # update calling
    #
    #      (Performs a full update.)
    #      API.update.full_update()
    #
    #      (Performs a dependency update.)
    #      API.update.deps_update()
    #
    #      (Performs a program update.)
    #      API.update.prog_update()
    #
    from core import version
    # version calling
    #
    #      (Print the Shadow Suite's version number)
    #      print(API.version.VNUMBER)
    #
    #      (Print the Shadow Suite's version type.)
    #      print(API.version.VTYPE)
    #
    #      (Print the Shadow Suite's version codename.)
    #      print(API.version.VCODENAME)
    #
    #      (Print the Shadow Suite's version number, type and codename.)
    #      print(API.version.BOTH)
    #
    from core import quote
    # quote calling
    #
    #      (Print a random quote)
    #      print(API.quote.quote())
    #
    from core import joke
    # joke calling
    #
    #      (Print a random joke)
    #      print(API.joke.joke())
    #
    from core import logger
    # logger calling
    #
    #      (Logging something)
    #      # This function needs three arguments, type, message, logfile, and session ID.
    #      # The type is an integer, message is a string, and logfile is also a string.
    #      # Log Type codes:          0 == INF       (Information)
    #      #                          1 == WRN       (Warning)
    #      #                          2 == ERR       (Error)
    #      #
    #      # Extended Log Type codes: 3 == ***INF*** (Important)
    #      #                          4 == ***WRN*** (Serious warning)
    #      #                          5 == ***ERR*** (Fatal error)
    #      #
    #      # If none above met, then UNK (Unknown) will be used.
    #
    #      # Session ID is given by Shadow Suite's main module.
    #
    #      # Example usage:
    #
    #      API.logger.log(2, 'Error message', 'logfile.txt', SESSION_ID)
    #
    import importlib
    from core import multitasking
    import signal

except ImportError:
    print("Error While Importing Modules! Now Quitting...")
    print()
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    logger.log(5, "SystemExit raised with error code 8.", 'api_logfile.txt')
    sys.exit(8)

class ShadowSuite:

    # Method calling: API.ShadowSuiteLE().[METHOD NAME]()
    # Variable assignment: variable = API.ShadowSuiteLE().[VARIABLE]

    API_VERSION = version.VAPI # This API's version
    SHADOWSUITE_VER_NUM = version.VNUMBER # Shadow Suite's version number
    SHADOWSUITE_VER_TYPE = version.VTYPE # Shadow Suite's version type
    SHADOWSUITE_VER_CODENAME = version.VCODENAME # Shadow Suite's version codename
    FINISH = "\n[i] Module finished running...\n"

    def __init__(self, current_user='user', MODULE_PATH='modules/', OUTPUT_PATH='output/', SESSION_ID=123456, USERLEVEL=2, debugging=False):
        if not current_user:
            self.current_user = 'user'

        else:
            self.current_user = current_user

        if not MODULE_PATH:
            self.MODULE_PATH = 'modules/'

        else:
            self.MODULE_PATH = MODULE_PATH

        if not OUTPUT_PATH:
            self.OUTPUT_PATH = 'output/'

        else:
            self.OUTPUT_PATH = OUTPUT_PATH

        if not SESSION_ID:
            self.SESSION_ID = 123456

        else:
            self.SESSION_ID = SESSION_ID
        
        if not USERLEVEL:
            self.USERLEVEL = 2

        else:
            self.USERLEVEL = USERLEVEL

        if not debugging:
            self.debugging = False

        else:
            self.debugging = debugging

    def generate_new_module(self, cmn):
        logger.log(0, 'User generated a new module named ' + module_name, 'logfile.txt', self.SESSION_ID)
        if misc.programFunctions().is_windows() == ('windows' or 'win' or 'nt'):
            os.system("xcopy core/temp.py output/" + module_name + ".py")
        
        else:
            os.system("cp core/temp.py output/" + module_name + ".py")
            
        if misc.programFunctions().path_exists('output/' + module_name + '.py'):
            print("[i] " + module_name + ".py successfully generated!")
        
        else:
            print("[i] " + error.ERROR0015 + " (Generated module not found)")

    def list_module(self):
        logger.log(0, 'User used list_module method via API.', 'api_logfile.txt', self.SESSION_ID)
        list_module.list(self.__MODULE_PATH__)

    def find_module(self, module):
        # Argument "module" is the target module to view the info.
        module = module.lower()
        logger.log(0, 'User used find_module method to look for ' + module + ' via API.', 'api_logfile.txt', self.SESSION_ID)
        module_name = self.MODULE_PATH + module
        try:
            module_path = module_path.replace('/', '.')
            module_import = importlib.import_module(module_path)
            module_import.module_info()

        except ModuleNotFoundError as modulenotfounderror_msg:
            print("[i] " + str(modulenotfounderror_msg))

    def use_module(self, module):
        # Argument "module" is the target module to run.
        module = module.lower()
        logger.log(0, 'User used use_module method to use ' + module + ' via API.', 'api_logfile.txt', self.SESSION_ID)
        module_name = MODULE_PATH + module
        try:
            module_path = module_path.replace('/', '.')
            module_import = importlib.import_module(module_path)
            module_import.main()

        except ModuleNotFoundError as modulenotfounderror_msg:
            print("[i] " + str(modulenotfounderror_msg))

    def suggest(self, criteria):
        # Argument "criteria" is the keywords typed in by user
        criteria = criteria.lower()
        logger.log(0, 'User wants a suggestion about ' + criteria + ' via API.', 'api_logfile.txt', self.SESSION_ID)
        suggest.api(criteria)

    def clrscrn(self):
        # Clears the contents of the screen.
        logger.log(0, 'User clears the screen via API.', 'api_logfile.txt', self.SESSION_ID)
        misc.programFunctions().clrscrn()

    def pause(self, silent=False):
        # Waits the user to press enter.
        logger.log(0, 'User used pause method via API with \'silent\' argument to ' + str(silent) + '.', 'api_logfile.txt', self.SESSION_ID)
        misc.programFunctions().pause(silent)

    def export_conf(self, config_file, config_dict):
        # Exports the current configuration to a file.
        logger.log(3, config_dict['username'] + " is exporting settings to " + config_file + " via API.", 'api_logfile', self.SESSION_ID)
        result = misc.programFunctions().export_conf(config_file, config_dict)
        return result
