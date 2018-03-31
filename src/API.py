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

# This Application Programming Interface (API) is meantly built for
# Shadow Suite LE custom modules. This may be used to integrate with
# Shadow Suite Linux Edition's features.

# Please take note that the API for Linux Edition is different from
# Windows Edition. Using an API from a different edition may not work.

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
    #      error = API.error.error****
    #
    #      (Replace * with warning number. See core/error.py for details.)
    #      error = API.error.warning****
    #
    from core import find_module
    from core import list_module
    from core import manage_module
    from core import misc
    # misc calling
    #
    #      (Prints Shadow Suite logo and version.)
    #      print(API.misc.logo)
    #
    #      (Prints "module mode" message.)
    #      print(API.misc.module_mode_info)
    #
    #      (Restarts Shadow Suite.)
    #      API.misc.restart_program()
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
    from core import use_module
    from core import version
    # version calling
    #
    #      (Print the Shadow Suite's version number)
    #      print(API.version.vnumber)
    #
    #      (Print the Shadow Suite's version type.)
    #      print(API.version.vtype)
    #
    #      (Print the Shadow Suite's version codename.)
    #      print(API.version.vcodename)
    #
    #      (Print the Shadow Suite's version number, type and codename.)
    #      print(API.version.both)
    #
    from core import quote
    # quote calling
    #
    #      (Print a random quote)
    #      print(API.quote.quote)
    #
    from core import joke
    # joke calling
    #
    #      (Print a random joke)
    #      print(API.joke.joke)
    #
    from core import logger
    # logger calling
    #
    #      (Logging something)
    #      # This function needs three arguments, type, message, and logfile.
    #      # The type is an integer, message is a string, and logfile is also a string.
    #      # Log Type codes: 0 == INF (Information)
    #      #                 1 == WRN (Warning)
    #      #                 2 == ERR (Error)
    #      # If none above met, then UNK (Unknown) will be used.
    #
    #      # Example usage:
    #
    #      API.logger.log(2, 'Error message', 'logfile.txt')
    #

except ImportError:
    print("Error While Importing Modules! Now Quitting...")
    print()
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    logger.log(2, "SystemExit raised with error code 8.", 'logfile.txt')
    sys.exit(8)

class ShadowSuiteLE:
    # Method calling: API.ShadowSuiteLE().[METHOD NAME]()
    # Variable assignment: variable = API.ShadowSuiteLE().[VARIABLE]

    API_version = version.vapi # This API's version
    ShadowSuite_ver_num = version.vnumber # Shadow Suite's version number
    ShadowSuite_ver_type = version.vtype # Shadow Suite's version type
    ShadowSuite_ver_codename = version.vcodename # Shadow Suite's version codename
    finish = "\n[i] Module finished running...\n"

    def generate_new_module(self, cmn):
        # Converts capital characters to lowercase characters.
        cmn = cmn.lower()
        # Copies the custom module template from module directory to output directory.
        manage_module.generate_new(cmn)
        logger.log(0, 'User generates a new module named ' + cmn + ' via API.', 'api_logfile.txt')

    def list_module(self):
        logger.log(0, 'User used list_module method via API.', 'api_logfile.txt')
        list_module.list()

    def find_module(self, module):
        # Argument "module" is the target module to view the info.
        module = module.lower()
        logger.log(0, 'User used find_module method to look for ' + module + ' via API.', 'api_logfile.txt')
        find_module.find(module)

    def use_module(self, module):
        # Argument "module" is the target module to run.
        module = module.lower()
        logger.log(0, 'User used use_module method to use ' + module + ' via API.', 'api_logfile.txt')
        use_module.use(module)

    def suggest(self, criteria):
        # Argument "criteria" is the keywords typed in by user.
        criteria = criteria.lower()
        logger.log(0, 'User wants a suggestion about ' + criteria + ' via API.', 'api_logfile.txt')
        suggest.api(criteria)

    def clrscrn(self):
        # Clears the contents of the screen.
        logger.log(0, 'User clears the screen via API.', 'api_logfile.txt')
        misc.programFunctions().clrscrn()

    def pause(self, silent=False):
        # Waits the user to press enter.
        logger.log(0, 'User used pause method via API with \'silent\' argument to ' + str(silent) + '.', 'api_logfile.txt')
        misc.programFunctions().pause(silent)
