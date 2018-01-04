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

# Shadow Suite modules
import core.error
import core.list_module
import core.manage_module
import core.misc
import core.module_manager
import core.update
import core.use_module
import core.use_framework
import core.version

class Class:
    API_version = core.version.vapi
    ShadowSuite_ver_num = core.version.vnumber
    ShadowSuite_ver_type = core.version.vtype
    ShadowSuite_ver_codename = core.version.vcodename
    # Hey! Learn how to use 'self'!

    def list_module():
        core.list_module.list()

    def use_module(module):
        core.use_module.use(module)

    def use_framework(framework):
        core.use_framework.use(framework)

    def finish():
        print("\n[i] Module finished running...\n")
