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
        "name": "URLCrazy", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "4.0", # version
        "author": "Andrew Horton", # Author
        "desc": "UrlCrazy is for the study of domainname typos and URL hijacking.", # Brief description
        "email": "none", # Email
        "authorinfo": "www.morningstarsecurity.com/research/urlcrazy", # Additional information about the author; this could be
        "lastupdate": "May. 08, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['Ruby'] # Put needed dependencies here.  
module_status = 0
category = ['urlcrazy', 'study', 'domain', 'typo', 'url', 'hijack']

# Changelog of the module
changelog = "Version 4.0:\nMandatory module update\n\nVersion 3.0:\nMandatory module update\n\nVersion 2.0:\nMandatory bug fix\n\nVersion 1.0:\nInitial module release"
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
def main(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging):
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
                print(error.errorCodes().ERROR0005)
                return 0

            else:
                module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging)

        else:
            module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging)

def module_body(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging):
    domain = str(input("Domain name to test > "))
    print("""\n
        Available Keyboard Layouts:
            QWERTY
            AZERTY
            QWERTZ
            DVORAK
            \n""")
    kb_layout = str(input("Keyboard layout > "))
    check_popularity = str(input("Do you want to check domain popularity with Google? (y/n) > "))
    no_resolve = str(input("Do not resolve DNS? (y/n) > "))
    show_invalid = str(input("Show invalid domain names? (y/n) > "))
    csv = str(input("Show result as CSV? (y/n) > "))
    output = str(input("Output filename > "))

    check_popularity = check_popularity.lower()
    if check_popularity == 'y':
        cp_switch = '-p '

    else:
        cp_switch = ''

    no_resolve = no_resolve.lower()
    if no_resolve == 'y':
        nr_switch = '-r '

    else:
        nr_switch = ''

    show_invalid = show_invalid.lower()
    if show_invalid == 'y':
        si_switch = '-i '
    
    else:
        si_switch = ''
        
    csv = csv.lower()
    if csv == 'y':
        csv_switch = '-f csv '

    else:
        csv_switch = '-f human '

    os.system("cd modules/URLCRAZY && ruby urlcrazy -k " + kb_layout + " " + cp_switch + nr_switch + si_switch + csv_switch + "-o ../../output/" + output + ' ' + domain)
    print(API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).FINISH)

def moduleAPI(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging):
    pass
