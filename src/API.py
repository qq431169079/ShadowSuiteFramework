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
import core.version

class ShadowSuiteAPI:
    API_version = "0.0.1.5"

    def ShadowSuite_version(self):
        ShadowSuite_ver_num = core.version.version_number
        ShadowSuite_ver_type = core.version.version_type
        ShadowSuite_codename = core.version.codename

    def prn_API_version(self):
        print(API_version)

    def list_module(self):
        core.
