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
    process = "3"

    print(core.misc.fb + core.misc.fi + core.misc.cb + "Performing a full update..." + core.misc.fr + core.misc.cw)
    print(core.misc.cb + "Updating Shadow Suite... (1/" + process + ")\n" + core.misc.cw)
    os.system("git pull")
    print(core.misc.cb + "Installing dependency files... (2/" + process + ")\n" + core.misc.cw)
    os.system("bash instdeps.bash")
    print(core.misc.cb + "Installing python modules... (3/" + process + ")\n" + core.misc.cw)
    os.system("pip install -r python_requirements")
    print(core.misc.fb + core.misc.fi + core.misc.cb + "Performing a full update... Done!" + core.misc.fr + core.misc.cw)
