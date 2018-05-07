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
from core import misc
from core import error

def list(module_path):
    COLOR_SUPPORT = misc.programFunctions().cli_color_support()
    if COLOR_SUPPORT == True:
        cw = '\033[0m'                         #  white  (normal)
        cb = '\033[34m'                        #  blue   (highlights)

        cg = '\033[32m'                        #  green  (Stable)
        cy = '\033[33m'                        #  yellow (Experimental)
        cr = '\033[31m'                        #  red    (Unstable)
        nyi = "\t[i] Not yet Implemented!!!"   #  Not yet Implemented
        cp = '\033[35m'                        #  Unknown status
    
        # Font types
        fr = '\033[0m'                         #  regular (Modules)
        fb = '\033[1m'                         #  bold    (Sections)
        fi = '\033[3m'                         #  italic  (Sub-Sections)

    else:
        cw = ''
        cb = ''

        cg = ''
        cy = ''
        cr = ''
        nyi = '\t[i] Not yet Implemented/Working'
        cp = ''

        fr = ''
        fb = ''
        fr = ''

    print(cg + fb + fi + "===Shadow Suite Modules and Frameworks===\n\n" + cb + fr)
    print(cw + "[i] The stability of the tools is color-coded:" + cw)
    print(cg + "\tStable" + cw)
    print(cy + "\tExperimental" + cw)
    print(cr + "\tUnstable" + cw)
    print(cp + "\tCustom Module\n\n" + cw)

    modules = os.listdir(module_path)
    module_iterator = 0
    # 0 == Stable
    # 1 == Experimental
    # 2 == Unstable
    # 3 == Not yet implemented/working
    for module in modules:
        imodule_path = module_path.replace('/', '.')
        imodule = module.replace('.py', '')
        ms = importlib.import_module(imodule_path + imodule)
        if '.py' in module or '.Py' in module or '.pY' in module or '.PY' in module:
            module_iterator += 1
            module = module.replace('.py', '')
            status = ms.module_status
            if status == 0:
                print("[" + str(module_iterator) +"] " + cg + module + " :: " + ms.info['desc'] + cw)
                print()

            elif status == 1:
                print("[" + str(module_iterator) +"] " + cy + module + " :: " + ms.info['desc'] + cw)
                print()

            elif status == 2:
                print("[" + str(module_iterator) +"] " + cr + module + " :: " + ms.info['desc'] + cw)
                print()

            elif status == 3:
                print("[" + str(module_iterator) +"] (" + nyi + ")" + module + " :: " + ms.info['desc'] + cw)
                print()

            else:
                print("[" + str(module_iterator) +"] " + cp + module + " :: " + ms.info['desc'] + cw)
                print()

        else:
            continue

        print(matched_modules) # DEV0005: For debugging purposes only

    # Old, lame, lazy, hard-coded algorithm :)
    """
    print(cb + fb + "\t==01-Information Gathering==\n" + cw + fr)
    print(cg + "\t\tAutomater" + cw)
    print(cg + "\t\tDNSEnum" + cw)
    print(cg + "\t\tDNSMap" + cw)
    print(cg + "\t\tDNSrecon" + cw)
    print(cg + "\t\tLANScan" + cw)
    print(cg + "\t\tMetagoofil" + cw)
    print(cg + "\t\tNwrap" + cw)
    print(cg + "\t\tRed Hawk" + cw)
    print(cg + "\t\tThe Harvester" + cw)
    print()
    print(cb + fb + "\t==02-Vulnerability Analysis==\n" + fr + cw)
    print(cb + fi + "\t\t==Cisco Tools==\n" + cw + fr)
    print(cg + "\t\t\tCisco Auditing Tool (CAT)" + cw)
    print(cg + "\t\t\tCisco Global Exploiter (CGE)" + cw)
    print()
    print(cb + fi + "\t\t==Fuzzing Tools==\n" + cw + fr)
    print(cg + "\t\t\tAngry Fuzzer" + cw)
    print(cr + "\t\t\tDotDotPwn" + cw)
    print()
    print(cb + fi + "\t\t==Stress Testing==\n" + cw + fr)
    print(cg + "\t\t\tfl00d" + cw)
    print(cg + "\t\t\tSlowloris" + cw)
    print()
    print(cb + fi + "\t\t==VoIP Tools==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fb + "\t==03-Web Application Analysis==\n" + cw + fr)
    print(cb + fi + "\t\t==CMS and Framework Identification==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fi + "\t\t==Web Application Proxies==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fi + "\t\t==Web Crawlers and Directory Bruteforcing Tools==\n" + fr + cw)
    print(nyi)
    print()
    print(cb + fb + "\t\t==Web Vulnerability Scanners==\n" + cw + fr)
    print(cg + "\t\t\tD-TECT (DTECT)" + cw)
    print(cg + "\t\t\tShellshocker" + cw)
    print(cg + "\t\t\tStriker" + cw)
    print()
    print(cb + fb + "\t==04-Database Assessment==\n" + cw + fr)
    print(cy + "\t\tDSSS" + cw)
    print(cg + "\t\tSQLMap" + cw)
    print()
    print(cb + fb + "\t==05-Password Attacks==\n" + cw + fr)
    print(cb + fi + "\t\t==Offline Attacks==\n" + cw + fr)
    print(cg + "\t\t\tHash Identifier" + cw)
    print(cg + "\t\t\tShadowCrack" + cw)
    print()
    print(cb + fi + "\t\t==Online Attacks==\n" + cw + fr)
    print(cr + "\t\t\tSocial Media Toolkit (SMT)" + cw)
    print(cg + "\t\t\tBlack Hydra" + cw)
    print(cg + "\t\t\tHash Buster" + cw)
    print()
    print(cb + fi + "\t\t==Passing the Hash Tools==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fi + "\t\t==Password Profiling and Wordlists==\n" + cw + fr)
    print(cg + "\t\t\tCUPP" + cw)
    print()
    print(cb + fb + "\t==06-Wireless Attacks==\n" + cw + fr)
    print("\t\tWifite" + cw + nyi) # DEV0001 #####
    print()
    print(cb + fb + "\t==07-Reverse Engineering==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fb + "\t==08-Exploitation Tools==\n" + cw + fr)
    print(cg + "\t\tLinux Exploit Suggester (LES)" + cw)
    print("\t\tMetasploit Framework (MSF)" + cw + nyi) # DEV0001 #####
    print(cg + "\t\tRouterSploit" + cw)
    print()
    print(cb + fb + "\t==09-Sniffing and Spoofing==\n" + fr +cw)
    print(cb + fi + "\t\t==Network Sniffers==\n" + fr + cw)
    print(nyi)
    print()
    print(cb + fi + "\t\t==Spoofing and MITM==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fb + "\t==10-Post Exploitation==\n" + cw + fr)
    print(nyi)
    print()
    print(cb + fb + "\t==11-Forensics==\n" + fr + cw)
    print(nyi)
    print()
    print(cb + fb + "\t==12-Reporting Tools==\n" + cw + fr)
    print(cg + "\t\tPipal" + cw)
    print()
    print(cb + fb + "\t==13-Social Engineering Tools==\n" + fr + cw)
    print(cg + "\t\tSocial Engineer Toolkit (SET)" + cw)
    print(cg + "\t\tURLCrazy" + cw)
    print(cg + "\t\tWeeman" + cw)
    print()
    print(cb + fb + "\t==14-System Services==\n" + cw + fr)
    print(cg + "\t\tIpify" + cw)
    print(cg + "\t\tIPcalc" + cw)
    print(cg + "\t\tWebExpose" + cw)
    print()
    print(cb + fb + "\t==15-Others==\n" + cw + fr)
    print(cy + "\t\tDeception" + cw)
    print()
    print(cb + fb + "\t==Custom Modules==\n" + cw + fr)
    # If you are adding a custom module, duplicate the code below:
    # print(core.misc.cp + "[MODULE NAME]")
    print(cp + "\t\tsample" + cw)
    """
