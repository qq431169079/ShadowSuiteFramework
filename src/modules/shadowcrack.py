########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

# Module version: 5.0

# Import directives
try:
    import os
    import sys
    import traceback
    from core import error
    from core.logger import log
    import API

    # Place your 'import' directives below

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Shadow Crack", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "4.0", # version
        "author": "Catayao56", # Author
        "desc": "A tool to encrypt and/or decrypt many kinds of ciphers and hashes.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "Apr. 12, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  
module_status = 1
category = ['encrypt', 'decrypt', 'crack', 'hash', 'cipher', 'md', 'sha', 'rc', 'catayao56', 'python']

# Changelog of the module
changelog = "Version 4.0:\nMandatory module update\n\nVersion 3.0:\nMandatory module update\n\nVersion 2.5:\nBug fix\n\nVersion 2.0:\nMandatory bug fix\n\nVersion 1.2:\nUpdated wordlist.\n\nVersion 1.0:\nInitial module release"
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
def main():
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
                module_body()

        else:
            module_body()

def module_body():
    banner = r"""
 ____  _               _                ____                _
/ ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |   | '__/ _` |/ __| |/ /
 ___) | | | | (_| | (_| | (_) \ V  V /| |___| | | (_| | (__|   <
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/  \____|_|  \__,_|\___|_|\_\
                           Launcher
    """
    print(banner)
    while True:
        print()
        print("[01] ShadowCrack v2.0\n[02] ShadowCrack Legacy\n\n[99] Quit")
        choice = int(input(" >>> "))
        if choice == 1:
            os.system("cd modules/SHADOWCRACK && python3 -B ShadowCrack.py")

        elif choice == 2:
            os.system("cd modules/SHADOWCRACK/legacy && python2 -B ShadowCrack.py")

        elif choice == 99:
            break

        else:
            print(API.error.ERROR0001)

    print(API.ShadowSuite().FINISH)
