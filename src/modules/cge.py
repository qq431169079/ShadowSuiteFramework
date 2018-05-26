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
        "name": "Cisco Global Exploiter", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "4.0", # version
        "author": "Nemesis and E4m", # Author
        "desc": "Cisco Global Exploiter (CGE), is an advanced,simple and fast security\ntesting tool, that is able to exploit the most dangerous vulnerabilities\nof Cisco systems.", # Brief description
        "email": "nemesis@blackangels.it -- e4m@blackangels.it,", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "May. 08, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: Perl 5.26.1'] # Put needed dependencies here.  
module_status = 0
category = ['cisco', 'global', 'universal', 'exploit', 'nemesis', 'e4m', 'advance', 'fast', 'perl']

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
    print()
    print()
    print()
    loop = True
    while loop == True:
        print("**************************")
        print("* Cisco Global Exploiter *")
        print("**************************")
        print()
        print("[01] Start")
        print("[02] Changelog")
        print("[03] Documentation")
        print("[04] Quit")
        print()
        selection = input("[CGE] > ")
        if selection == "1":
            start()

        elif selection == "2":
            prog_changelog()
    
        elif selection == "3":
            documentation()
        
        elif selection == "4":
            loop = False
            quitsequence()

        else:
            print("Wrong input!")

    print(API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).FINISH)

def start():
    TARGET = input("Target IP: ")
    vulnlst()
    TGTNUM = input("Vulnerability number: ")
    print("[i] Running...")
    exploit(TARGET, TGTNUM)

def prog_changelog():
    os.system("less modules/CGE/doc/Changelog")

def documentation():
    os.system("less modules/CGE/doc/Documentation")

def quitsequence():
    pass

def vulnlst():
    print()
    print("[1] - Cisco 677/678 Telnet Buffer Overflow Vulnerability")
    print("[2] - Cisco IOS Router Denial of Service Vulnerability")
    print("[3] - Cisco IOS HTTP Auth Vulnerability")
    print("[4] - Cisco IOS HTTP Configuration Arbitrary Administrative Access Vulnerability")
    print("[5] - Cisco Catalyst SSH Protocol Mismatch Denial of Service Vulnerability")
    print("[6] - Cisco 675 Web Administration Denial of Service Vulnerability")
    print("[7] - Cisco Catalyst 3500 XL Remote Arbitrary Command Vulnerability")
    print("[8] - Cisco IOS Software HTTP Request Denial of Service Vulnerability")
    print("[9] - Cisco 514 UDP Flood Denial of Service Vulnerability")
    print("[10] - CiscoSecure ACS for Windows NT Server Denial of Service Vulnerability")
    print("[11] - Cisco Catalyst Memory Leak Vulnerability")
    print("[12] - Cisco CatOS CiscoView HTTP Server Buffer Overflow Vulnerability")
    print("[13] - 0 Encoding IDS Bypass Vulnerability (UTF)")
    print("[14] - Cisco IOS HTTP Denial of Service Vulnerability")
    print()

def exploit(TARGET, TGTNUM):
    space = ' '
    os.system("cd modules/CGE && perl cge.pl " + TARGET + space + TGTNUM)
    print(API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).FINISH)
