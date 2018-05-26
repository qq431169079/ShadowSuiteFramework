# Import directives
import os
import sys
from core import error
import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here
import time

# Put your module information here.
info = {
        "name": "Sample", # Module filename (Change filename if you want to change this)
        "version": "6.0", # version
        "author": "Catayao56", # Author
        "desc": "A sample module that uses the Shadow Suite API.", # Brief description
        "email": "N/A", # Email
        "authorinfo": "https://github.com/Catayao56/", # Additional information about the author; this could be
        "lastupdate": "May. 08, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Using API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3'] # Put needed dependencies here.  
module_status = 0
category = ['sample', 'api', 'shadow', 'suite', 'framework']

# Changelog of the module
changelog = "Version 6.0:\nMandatory module update\n\nVersion 5.0:\nMandatory module update\n\nVersion 4.0:\nMandatory bug fix\n\nVersion 3.3:\nUpdated Sample module to keep up with API's update.\n\nVersion 3.2:\nSample module update\n\nVersion 2.1:\nAnother Update\n\nVersion 1.0:\nSample Module Initial Release"

# Prints the module information
def module_info():
    if info['needsroot'] == "0":
        superm = "True"
    else:
        superm = "False"

    print("Module Name: " + info['name'])
    print("Module Version: " + info['version'])
    print("Module Author: " + info['author'])
    print("Module Description: " + info['desc'])
    print()
    print("Module Author's Email: " + info['email'])
    print("Module Author's Info: " + info['authorinfo'])
    print("Module's last update: " + info['lastupdate'])
    print("Using Shadow Suite's API: " + info['usingapi'])
    print("Needs root: " + superm)

# Main module function
def main(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging):
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            print(error.errorCodes().ERROR0005)
            return

        else:
            module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging)

    else:
        module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging)

def module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging):
    # Place your program here. This is the function where your program will be placed.
    module_info()
    print("Hello!")
    time.sleep(2)
    print("This is a sample module for Shadow Suite...")
    time.sleep(2)
    print("Shadow Suite's version number is " + API.ShadowSuite().SHADOWSUITE_VER_NUM + ".")
    time.sleep(2)
    print("Shadow Suite's version type is " + API.ShadowSuite().SHADOWSUITE_VER_TYPE + ".")
    time.sleep(2)
    print("Shadow Suite's version codename is " + API.ShadowSuite().SHADOWSUITE_VER_CODENAME + ".")
    time.sleep(2)
    print("Shadow Suite's API version is " + API.ShadowSuite().API_VERSION + ".")
    time.sleep(2)
    print("Listing installed modules...")
    time.sleep(2)
    API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).list_module()
    time.sleep(2)
    print("Quitting in 3...")
    time.sleep(1)
    print("Quitting in 2...")
    time.sleep(1)
    print("Quitting in 0.700...")
    time.sleep(0.700)
    print("Quitting in 0...")
    time.sleep(.300)
    print(API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).FINISH)
