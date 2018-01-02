#!/bin/python

# Shadow Suite :: Ethical Hacking Toolkit
# Copyright (C) 2017  Shadow Team <Public.ShadowTeam@gmail.com>
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
# You should have received a copy of the GNU General Public License.
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import core.misc
import core.error

global version_number
global version_type

version_number = "0.0.3.2"
version_type = "Weekly Build"

def number():
    # example:
    # Program's version is...
    #
    #           0     .     1     .     14     .     27
    #
    #           ^           ^           ^            ^
    #         Major       Minor        Beta      Weekly Build
    #        version     version     version       version
    print(core.misc.cg + version_number + core.misc.cw)
    # Major version: Major release of the prpgram.
    #                e.g. it's the 5th major release, then the major
    #                version is 5.
    #
    # Minor version: Minor release of the program.
    #                e.g. it's the 5th minor release, then the minor
    #                version is 5.
    #
    # Beta version: Beta release of the program.
    #               e.g. it's the 5th beta release, then the beta
    #               version is 5.
    #
    # Weekly Build version: Weekly Builds of the program.
    #               Very unstable, many tools are under production.
    #               like nightly builds, but instead of updating nightly,
    #               it's updating weekly.

def type():
    print(core.misc.cg + version_type + core.misc.cw)
    #
    # Weekly Build: first phase of release cycle. Many tools under
    #               production, program has so many bugs, very unstable.
    #
    # Unstable:     second phase of release cycle. Tools are already
    #               produced, debugging of the program takes place here.
    #
    # Experimental: third phase of release cycle. Tools are produced,
    #               almost all bugs are eradicated.
    #
    # Stable:       last phase of release cycle. Tools are produced,
    #               all known bugs are fixed. In this phase, you can now
    #               start a new maintenance update, which means the release
    #               cycle will go back to Weekly Build.

def both():
    print(core.misc.cg + version_number + "\t" + version_type + core.misc.cw)
