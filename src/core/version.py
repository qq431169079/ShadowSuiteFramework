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

global vapi
global vnumber
global vtype
global vcodename

vapi = "0.0.6.0"
vnumber = "0.0.4.4"
vtype = "Weekly Build"
vcodename = "Implementation"

def number():
    # example:
    # Program's version is...
    #
    #           0     .     1     .     14     .     27
    #
    #           ^           ^           ^            ^
    #         Major       Minor        Beta      Weekly Build
    #        version     version     version       version
    print(core.misc.cg + vnumber + core.misc.cw)
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
    print(core.misc.cg + vtype + core.misc.cw)
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

def codename():
    print(core.misc.cg + vcodename + core.misc.cw)
    #
    # (Catayao56:) I suggest that you use codenames in alphabetical order.
    # What i mean is this:
    #
    # Default Codenames:
    # 
    # Abstraction                                        ( Used in v0.0.0.1 )
    # Bang                                               ( Used in v0.0.1.0 )
    # Cache                                              ( Used in v0.0.2.0 )
    # Dark                                               ( Used in v0.0.3.0 )
    # Elliot                                             ( Used in v0.0.3.4 )
    # Faraday                                            ( Used in v0.0.3.5 )
    # Game Blaster                                       ( Used in v0.0.3.6 )
    # Handshake                                          ( Used in v0.0.3.8 )
    # Implementation                                     ( Used in v0.0.4.0 )
    # Job                                                ( Not yet used )
    # Knight                                             ( Not yet used )
    # Lazy                                               ( Not yet used )
    # Metro                                              ( Not yet used )
    # New ways                                           ( Not yet used )
    # Open Grounds                                       ( Not yet used )
    # PHP                                                ( Not yet used )
    # Querty                                             ( Not yet used )
    # Ruby                                               ( Not yet used )
    # Silicon                                            ( Not yet used )
    # Time                                               ( Not yet used )
    # Universal                                          ( Not yet used )
    # Variable                                           ( Not yet used )
    # Wireless                                           ( Not yet used )
    # Xfr                                                ( Not yet used )
    # You There                                          ( Not yet used )
    # Zero-Day                                           ( Not yet used )

def both():
    print(core.misc.cg + vnumber + "\t" + vtype + "\tCodename: " + vcodename + core.misc.cw)
