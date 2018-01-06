#!/bin/python
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

class Class:
    API_version = core.version.vapi
    ShadowSuite_ver_num = core.version.vnumber
    ShadowSuite_ver_type = core.version.vtype
    ShadowSuite_ver_codename = core.version.vcodename
    # Hey! Learn how to use 'self'!

    def generate_new_module(cmn):
        # Copies the custom module template from module directory to output directory.
        core.manage_module.generate_new(cmn)

    def list_module():
        core.list_module.list()

    def find_module(module):
        # Argument "module" is the target module to view the info.
        core.find_module.find(module)

    def use_module(module):
        # Argument "module" is the target module to run.
        core.use_module.use(module)

    def use_framework(framework):
        # Argument "framework" is the target framework to run.
        core.use_framework.use(framework)

    def finish():
        print("\n[i] Module finished running...\n")
