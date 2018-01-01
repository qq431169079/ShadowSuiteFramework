#!/bin/python

# Shadow Suite :: Ethical Hacking Toolkit                                                 # Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>                           #                                                                                         # This program is free software: you can redistribute it and/or modify                    # it under the terms of the GNU General Public License as published by                    # the Free Software Foundation, either version 3 of the License, or                       # (at your option) any later version.                                                     #                                                                                         # This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.                                            #                                                                                         # You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
import core.misc
import core.error

def full_update():
    process = "2"

    print(core.misc.fb + core.misc.fi + core.misc.cb + "Performing a full update..." + core.misc.fr + core.misc.cw)
    print("Installing dependency files... (1/" + process + ")\n")
    os.system("xargs -0 apt install -y <(tr \\n \\0 < $PWD/apt_requirements)")
    print("Installing python modules... (2/" + process + ")\n")
    os.system("pip install -r python_requirements")
    print(core.misc.fb + core.misc.fi + core.misc.cb + "Performing a full update... Done!" + core.misc.fr + core.misc.cw)
