#		 Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)

# Python modules

import os
import sys
import requests
import json

import urllib.request
import shutil
import distutils.dir_util
from core.packaging import version
from glob import glob
from core import misc
from core import error

def check_for_updates():
    try:
        print(misc.CG + "[i] Checking for updates..." + misc.CW)
        if misc.debugging == True:
            print("[DEBUG] getting https://api.github.com/repos/Sh4d0w-T34m/ShadowSuiteLE/releases/latest...")
        r = requests.get("https://api.github.com/repos/Sh4d0w-T34m/ShadowSuiteLE/releases/latest")
        if(r.ok):
            items = json.loads(r.text or r.content)
            rver = items['tag_name']
        
        else:
            print(error.ERROR0007)

    except Exception as error:
        print(misc.CR + "Error: " + str(error) + misc.CW)

def update():
    answer = input(misc.CGR + "Do you want to start update? > " + misc.CW)
    answer = answer.lower()
    if answer != "yes" and answer != "y":
        return None
    
    else:
        url = "https://github.com/Sh4d0w-T34m/ShadowSuiteLE/tarball/master"
        print(misc.CG + "Downloading..." + misc.CW)
        try:
            if misc.debugging == True:
                print("[DEBUG] Opening https://github.com/Sh4d0w-T34m/ShadowSuiteLE/tarball/master")
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
            if "ShadowSuiteLE.py" in file and os.path.isfile(file) == False:
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
        print(misc.CY + "Update installed! closing Shadow Suite LE..." + misc.CW)
        sys.exit(0)
