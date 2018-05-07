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

import os
import importlib

from core import error
from core import misc
from core import version

def api(criteria, module_path):
    criteria = criteria.split(',')
    crilist = []
    for crit in criteria:
        crilist.append(crit)

    modules = os.listdir(module_path)
    module_iterator = 0
    module_path = module_path.replace('/', '.')
    for module in modules:
        module = module.replace('.py', '')
        ms = importlib.import_module(module_path + module)
        if '.py' in module or '.Py' in module or '.pY' in module or '.PY' in module:
            module_iterator += 1
            module = module.replace('.py', '')
            status = ms.category
            for category in status:
                if category in crilist:
                    print(module + " :: " + ms.info['description'])
                    break

                else:
                    continue

        else:
            continue
