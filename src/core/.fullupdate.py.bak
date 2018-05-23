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


###########################################################################
#                                                                         #
#             Original code from Hakku Framework by 4shadoww:             #
#             Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)             #
#                                                                         #
###########################################################################

# Python modules

import os
import sys
from core import requests
import json

import urllib.request
import shutil
import distutils.dir_util
from core.packaging import version
from glob import glob
from core import misc
from core import error

def check_for_updates(DEBUGGING):
    misc.debugging = DEBUGGING
    try:
        print(misc.CG + "[i] Checking for updates..." + misc.CW)
        if misc.debugging == True:
            print("[DEBUG] getting https://api.github.com/repos/Sh4d0w-T34m/ShadowSuiteFramework/releases/latest...")
        r = requests.get("https://api.github.com/repos/Sh4d0w-T34m/ShadowSuiteFramework/releases/latest")
        if(r.ok):
            items = json.loads(r.text or r.content)
            rver = items['tag_name']
        
        else:
            print(error.ERROR0007)

    except Exception as error:
        print(misc.CR + "Error: " + str(error) + misc.CW)

def update(DEBUGGING):
    misc.debugging = DEBUGGING
    answer = input(misc.CGR + "Do you want to start update? > " + misc.CW)
    answer = answer.lower()
    if answer != "yes" and answer != "y":
        return None
    
    else:
        url = "https://github.com/Sh4d0w-T34m/ShadowSuiteFramework/tarball/master"
        print(misc.CG + "Downloading..." + misc.CW)
        try:
            if misc.debugging == True:
                print("[DEBUG] Opening https://github.com/Sh4d0w-T34m/ShadowSuiteFramework/tarball/master")
            u = urllib.request.urlopen(url)

        except urllib.error.URLError:
            print(error.ERROR0010)
            return None

        print(misc.CG + "Clearing tmp..." + misc.CW)
        mscop.clear_tmp()
        print(misc.CG + "Writing..." + misc.CW)
        f = open(getpath.tmp()+"update.tar.gz", "wb")
        f.write(u.read())
        f.close()
        print(misc.CG + "Extracting..." + misc.CW)
        os.system("tar -zxvf '" + getpath.tmp() + "update.tar.gz' -C '" + getpath.tmp() + "'")
        files = glob(getpath.tmp()+"*/")
        update_path = None
        for file in files:
            if "SSF.py" in file and os.path.isfile(file) == False:
                update_path = file
                break
            
        if update_path == None:
            print(misc.CR + error.ERROR0009 + misc.CW)
            return
        
        files = glob(update_path + "*")
        print(misc.CG + "Installing update..." + misc.CW)
        for file in files:
            file_name = file.replace(update_path, "")
            print(getpath.main() + file_name)
            if os.path.isfile(file):
                shutil.copyfile(file, getpath.main() + file_name)

            else:
                distutils.dir_util.copy_tree(file, getpath.main() + file_name)
                
        print(misc.CG + "Clearing tmp..." + misc.CW)
        mscop.clear_tmp()
        print(misc.CY + "Update installed! closing Shadow Suite Framework..." + misc.CW)
        sys.exit(0)
