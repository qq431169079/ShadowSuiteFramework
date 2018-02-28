#!/bin/python
# Coding=UTF-8
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
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import core.error
import core.misc
import core.version

def api(criteria):
    criteria = criteria.lower()
    criteria = criteria.replace(',', ' ')
    print("Searching...")
    results = "0"

    # Saved keywords
    automater = ["automate", "recon", "info", "ga", "tekdefense", "python", "ip", "url", "hash", "passive", "analysis"]
    dnsenum = ["dnsenum", "multithread", "perl", "enum", "dns", "info", "ga", "domain", "ip", "block"]
    
    # Conditional Statements
    if criteria in automater:
        print(core.misc.cg + "Automater : IP, URL, and Hash Passive Analysis Tool." + core.misc.cw)
        results = results + "1"
    
    if criteria in dnsenum:
        print(core.misc.cg + "DNSEnum : Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks." + core.misc.cw)
        results = results + "1"

    # More info
    print("\n")
    if results == "0":
        print("SORRY! No tool matched your criteria... Please contact Shadow Team for Feature requests...")
    elif results == "01":
        print(results + " tool matched your criteria.")
    else:
        print(results + " tools matched your criteria!")
