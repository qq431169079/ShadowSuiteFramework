#!/bin/python
# Coding=UTF-8
# Shadow Suite :: Ethical Hacking Toolkit
# Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com
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
# Shadow Suite custom modules. This may be used to integrate with
# Shadow Suite's features.
try:
    # Python modules
    import os
    import sys
    import time

    # Shadow Suite modules
    import core.error
    # core.error calling
    #      
    #      (Replace * with error number. See core/error.py for details.)
    #      API.core.error.error****()
    #
    #      (Replace * with warning number. See core/error.py for details.)
    #      API.core.error.warning****()
    #
    import core.find_module
    import core.hakku
    import core.list_module
    import core.manage_module
    import core.misc
    # core.misc calling
    #
    #      (Prints Shadow Suite logo and version.)
    #      API.core.misc.prn_logo()
    #
    #      (Prints "module mode" message.)
    #      API.core.misc.module_mode()
    #
    import core.update
    # core.update calling
    #
    #      (Performs a full update.)
    #      API.core.update.full_update()
    #
    #      (Performs a dependency update.)
    #      API.core.update.deps_update()
    #
    #      (Performs a program update.)
    #      API.core.update.prog_update()
    #
    import core.use_framework
    import core.use_module
    import core.version
    # core.version calling
    #
    #      (Print the Shadow Suite's version number)
    #      API.core.version.number()
    #
    #      (Print the Shadow Suite's version type.)
    #      API.core.version.type()
    #
    #      (Print the Shadow Suite's version codename.)
    #      API.core.version.codename()
    #
    #      (Print the Shadow Suite's version number, type and codename.)
    #      API.core.version.both()
    #
except ImportError:
    print("Error Importing Modules! Now Quitting...")
    sys.exit(1)

class Class:
    # Method calling: API.Class().[METHOD NAME]()
    API_version = core.version.vapi # This API's version
    ShadowSuite_ver_num = core.version.vnumber # Shadow Suite's version number
    ShadowSuite_ver_type = core.version.vtype # Shadow Suite's version type
    ShadowSuite_ver_codename = core.version.vcodename # Shadow Suite's version codename

    def generate_new_module(self, cmn):
        # Converts capital characters to lowercase characters.
        cmn = cmn.lower()
        # Copies the custom module template from module directory to output directory.
        core.manage_module.generate_new(cmn)

    def list_module(self):
        core.list_module.list()

    def find_module(self, module):
        # Argument "module" is the target module to view the info.
        module = module.lower()
        core.find_module.find(module)

    def use_module(self, module):
        # Argument "module" is the target module to run.
        module = module.lower()
        core.use_module.use(module)

    def use_framework(self, framework):
        # Argument "framework" is the target framework to run.
        framework = framework.lower()
        core.use_framework.use(framework)

    def finish(self):
        print("\n[i] Module finished running...\n")
