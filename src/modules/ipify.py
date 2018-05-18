########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

module_version = 7.3

# Import directives
try:
    import os
    import sys
    import traceback
    from core import error
    from core.logger import log
    import API

    # Place your 'import' directives below
    import requests

    import_error = False

except(ImportError, ModuleNotFoundError):
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Ipify", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "3.1", # version
        "author": "Catayao56", # Author
        "desc": "A public IP address API.", # Brief description
        "email": "Catayao56", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "May. 18, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3', 'PYTHON: requests'] # Put needed dependencies here.
module_status = 0 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
category = ['all', 'python', 'public', 'ip', 'address', 'ipify', 'catayao']
#files = [] # Uncomment this line if the module needs a subdirectory to use.
#E.g.: MODULE_NAME_OR_SUBDIRECTORY_NAME/

# Changelog of the module
changelog = "Version 3.1:\nBug fix\n\nVersion 3.0:\nMandatory module update\n\nVersion 2.0:\nMandatory module update\n\nVersion 1.0:\nInitial module release"
# Changelog format:
#
# changelog = "Version 2.0:\nUpdate Description\n\nVersion1.0\nInitial module release"

# Prints the module information
def module_info():
    # Unofficial way to convert integer to Boolean
    # (well, not really a boolean, as it is a string).
    # if [argument] == 0 then True; Otherwise, False.
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
    print("Shadow Suite API Support: " + info['usingapi'])
    print("Needs root: " + superm)
    print()
    # Prints the dependencies via for loop. I just copy/pasted it from a reference book
    # and modified it XD
    print("Dependencies:", end=' ')
    for item in dependencies:
        print(item, ",", end=' ')
    print()
    # Prints the changelog of the module.
    print("Changelog:\n" + "\n" + changelog)
    print("\n\n")

# Main module function
def main(global_variables):
    if import_error is True:
        return None

    else:
        """ First, it checks the value assigned to the 'needsroot' variable in the 
        dictionary 'info', then if the value is equal to zero, it calls the 'geteuid()'
        function from the 'os' module. If the result from geteuid is also zero, then
        the module will call the function 'module_body()'. Otherwise, it will print an
        error message. If the value assigned to the 'needsroot' variable in the dictionary
        'info' is not equal to zero, then the module will not call the 'geteuid()' function
        from the 'os' module, and will immediately call 'module_body()' function. """
        if info['needsroot'] == "0":
            if os.geteuid() != 0:
                print(error.ERROR0005)
                return 0

            else:
                module_body(global_variables)

        else:
            module_body(global_variables)

def module_body(global_variables):
    # To support module versions older than v7.0
    API_ShadowSuite = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING'])
    print()
    try:
        ip = requests.get('https://api.ipify.org/').text
        print("Your public IP Address is '" + str(ip) + "'.")

    except ConnectionError:
        print(error.ERROR0010)
    
    except requests.exceptions.ConnectionError:
        print(error.ERROR0010)

    except Exception as error_msg:
        print("[i] " + str(error_msg))

    print(API_ShadowSuite.FINISH)
