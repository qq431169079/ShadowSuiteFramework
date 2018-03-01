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
    results = 0

    # Conditional Statements
    if 'automater' in criteria or 'auto' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'tekdefese' in criteria or 'python' in criteria or 'ip' in criteria or 'url' in criteria or 'hash' in criteria or 'passive' in criteria and 'analysis' in criteria:
        print(core.misc.cg + "Automater : IP, URL, and Hash Passive Analysis Tool.\n" + core.misc.cw)
        results = results + 1
    
    if 'dnsenum' in criteria or 'multithread' in criteria or 'perl' in criteria or 'enum' in criteria or 'dns' in criteria or 'info' in criteria and 'ga' in criteria or 'domain' in criteria or 'ip' in criteria or 'block' in criteria or 'filip' in criteria and 'waeytens' in criteria:
        print(core.misc.cg + "DNSEnum : Multithreaded perl script to enumerate DNS information of a domain and to discover non-contiguous ip blocks.\n" + core.misc.cw)
        results = results + 1

    if 'dnsmap' in criteria or 'filip' in criteria and 'waeytens' in criteria or 'info' in criteria and 'ga' in criteria or 'enum' in criteria or 'sec' in criteria or 'assess' in criteria or 'dns' in criteria or 'python' in criteria:
        print(core.misc.cg + "DNSMap : Mainly meant to be used by pentesters during the information gathering/enumeration phase of infrastructure security assessments.\n" + core.misc.cw)
        results = results + 1

    if 'dnsrecon' in criteria or 'dns' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'tool' in criteria or 'python' in criteria:
        print(core.misc.cg + "DNSRecon : DNS Reconnaissance Tool.\n" + core.misc.cw)
        results = results + 1

    if 'lanscan' in criteria or 'stephan' in criteria and 'van' in criteria and 'de' in criteria and 'kerkhof' in criteria or 'ping' in criteria or 'tcp' in criteria or 'net' in criteria and 'scan' in criteria or 'recon' in criteria or 'info' in criteria and 'ga' in criteria or 'python' in criteria:
        print(core.misc.cg + "LANScan : System ping / TCP network scanner.\n" + core.misc.cw)
        results = results + 1

    if 'metagoofil' in criteria or 'christian' in criteria and 'martorella' in criteria or 'extract' in criteria or 'meta' in criteria or 'doc' in criteria or 'pdf' in criteria or 'xls' in criteria or 'ppt' in criteria or 'web' in criteria or 'python' in criteria:
        print(core.misc.cg + "Metagoofil : A tool for extracting metadata of public documents (pdf,doc,xls,ppt,etc) availables in the target websites.\n" + core.misc.cw)
        results = results + 1

    if 'nmap' in criteria or 'nwrap' in criteria or 'catayao56' in criteria or 'net' in criteria and 'map' in criteria or 'port' in criteria and 'scan' in criteria or 'ping' in criteria or 'tcp' in criteria or 'udp' in criteria or 'python' in criteria:
        # DEV0001: Update this description
        print(core.misc.cg + "Nwrap : [UPDATE DESC]\n")
        results = results + 1

    if 'red' in criteria and 'hawk' in criteria or 'r3d#@0r_2h1n' in criteria or 'tuhinshubhra' in criteria or 'info' in criteria and 'ga' in criteria or 'vuln' in criteria and 'scan' in criteria or 'wordpress' in criteria or 'wp' in criteria or 'php' in criteria:
        print(core.misc.cg + "Red Hawk : All in One tool for Information Gathering and Vulnerability Scanning.\n")
        results = results + 1

    if 'the' in criteria and 'harvest' in criteria or 'python' in criteria or 'christian' in criteria and 'martorella' in criteria or 'ga' in criteria or 'email' in criteria or 'acc' in criteria or 'subdomain' in criteria or 'virtual' in criteria and 'host' in criteria or 'port' in criteria or 'banner' in criteria or 'employee' in criteria and 'name' in criteria or 'search' in criteria:
        print(core.misc.cg + "The Harvester : A tool for gathering e-mail accounts, subdomain names, virtual hosts, open ports/banners, and employee names from different public sources (search engines, pgp key servers).\n" + core.misc.cw)
        results = results + 1

    if 'cisco' in criteria or 'audit' in criteria or 'g0ne' in criteria or 'null0' in criteria or 'net' in criteria:
        print(core.misc.cg + "Cisco Auditing Tool : A tool for auditing Cisco networks.\n" + core.misc.cw)
        results = results + 1

    if 'cisco' in criteria or 'exploit' in criteria or 'vuln' in criteria:
        print(core.misc.cg + "Cisco Global Exploiter : An advanced,simple and fast security testing tool, that is able to exploit the most dangerous vulnerabilities of Cisco systems.\n")
        results = results + 1

    # More info
    print("\n")
    results = str(results)
    if results == "0":
        print("SORRY! No tool matched your criteria... Please contact Shadow Team for Feature requests...")
    elif results == "1":
        print(results + " tool matched your criteria.")

    else:
        print(results + " tools matched your criteria!")
