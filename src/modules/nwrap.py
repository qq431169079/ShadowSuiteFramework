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
    import nmap

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Nwrap", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "6.1", # version
        "author": "Catayao56", # Author
        "desc": "Wrapper script for Nmap Network Mapper.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "May. 08, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: Nmap', 'PYTHON: nmap'] # Put needed dependencies here.  
module_status = 1
category = ['nwrap', 'nmap', 'wrapper', 'catayao56', 'python', 'port', 'scan']

# Changelog of the module
changelog = "Version 6.1:\nFixed false-positive error 'nmap not found on path' by using os.system() module.\n\nVersion 6.0:\nMandatory module update\n\nVersion 5.0:\nMandatory module update\n\nVersion 4.4:\nBug fix\n\nVersion 4.0:\nMandatory bug fix\n\nVersion 3.4:\nRewritten to be a Shadow Suite module\n\nVersion 3.0:\nAdded new scan types\n\nVersion 2.1:\nFixed bugs\n\nVersion 1.0:\nInitial module release"
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
    print("Nmap: Network exploration tool and security / port scanner\n\n")
    print("Target's IP Address or URL: ")
    TARGET = input("[NWRAP] > ")
    while True:
        print("\n")
        print("Common Scanning Types:")
        print("[1] TCP connect scan")
        # nmap -sT [TARGET]
        print("[2] Half-open scan        [i] ROOT REQUIRED")
        # nmap -sS [TARGET]
        print("[3] ping scan")
        # nmap -sP [TARGET]
        print("[4] UDP scan              [i] ROOT REQUIRED")
        # nmap -sU [TARGET]
        print("[5] IP Protocol scan      [i] ROOT REQUIRED")
        # nmap -sO [TARGET]
        print()
        print("Ping Scan Types:")
        print("[6] TCP SYN ping")
        # nmap -PS[PORTLIST] [TARGET]
        print("[7] TCP ACK ping")
        # nmap -PA[PORTLIST] [TARGET]
        print("[8] UDP ping              [i] ROOT REQUIRED")
        # nmap -PU[PORTLIST] [TARGET]
        print("[9] SCTP INIT ping        [i] ROOT REQUIRED")
        # nmap -PY[PORTLIST] [TARGET]
        print("[10] ARP ping")
        # nmap -PR [TARGET]
        print()
        print("Other Scan Types:")
        print("[11] List scan")
        # nmap -sL [TARGET]
        print("[12] SCTP INIT scan       [i] ROOT REQUIRED")
        # nmap -sY [TARGET]
        print("[13] TCP ACK scan         [i] ROOT REQUIRED")
        # nmap -sA [TARGET]
        print("[14] TCP Windows scan     [i] ROOT REQUIRED")
        # nmap -sW [TARGET]
        print("[15] OS scan              [i] ROOT REQUIRED")
        # nmap -O [TARGET]
        print()
        print("More settings:")
        print("[98] Automated scans")
        # DEV0001: Include comprehensive, intense scans
        print("[99] Quit")
        # nmap -O [TARGET]
        print()
        SCANTYPE = int(input("[NWRAP] > "))
        if SCANTYPE == 1:
            print()
            print()
            print()
            print()
            print("TCP Connect scan")
            print()
            try:
                nmap.PortScanner("nmap -sT " + TARGET)

            except:
                os.system('nmap -sT ' + TARGET)

            print()
            print("Scan finished!")
            API.misc.programFunctions().pause()

        elif SCANTYPE == 2:
            print()
            print()
            print()
            print()
            print("Half-open scan")
            print()
            try:
                nmap.PortScanner("nmap -sS " + TARGET)

            except:
                os.system("nmap -sS " + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 3:
            print()
            print()
            print()
            print()
            print("Ping scan")
            print()
            try:
                nmap.PortScanner("nmap -sP " + TARGET)

            except:
                os.system('nmap -sP ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 4:
            print()
            print()
            print()
            print()
            print("UDP scan")
            print()
            try:
                nmap.PortScanner("nmap -sU " + TARGET)

            except:
                os.system("nmap -sU " + TARGET)

            print()
            print("Scan finished!")
            
        elif SCANTYPE == 5:
            print()
            print()
            print()
            print()
            print("IP Protocol scan")
            print()
            try:
                nmap.PortScanner("nmap -sO " + TARGET)

            except:
                os.system("nmap -sO " + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 6:
            print()
            print()
            print()
            print()
            print("TCP SYN ping")
            print()
            try:
                nmap.PortScanner("nmap -PS20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
            
            except:
                os.system("nmap -PS20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
            
            print()
            print("Scan finished!")

        elif SCANTYPE == 7:
            print()
            print()
            print()
            print()
            print("TCP ACK ping")
            print()
            try:
                nmap.PortScanner("nmap -PA20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)

            except:
                os.system('nmap -PA20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 ' + TARGET)

            print()
            print("Scan finished!")
        
        elif SCANTYPE == 8:
            print()
            print()
            print()
            print()
            print("UDP ping")
            print()
            try:
                nmap.PortScanner("nmap -PU20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)

            except:
                os.system("nmap -PU20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060")
            print()
            print("Scan finished!")

        elif SCANTYPE == 9:
            print()
            print()
            print()
            print()
            print("SCTP INIT ping")
            print()
            try:
                nmap.PortScanner("nmap -PY20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)

            except:
                os.system('nmap -PY20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 ' + TARGET)

            print()
            print("Scan finished!")
        
        elif SCANTYPE == 10:
            print()
            print()
            print()
            print()
            print("ARP ping")
            print()
            try:
                nmap.PortScanner("nmap -PR20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)

            except:
                os.system('nmap -PR20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 11:
            print()
            print()
            print()
            print()
            print("List scan")
            print()
            try:
                nmap.PortScanner("nmap -sL " + TARGET)

            except:
                os.system('nmap -sL ' + TARGET)

            print()
            print("Scan finished!")
        
        elif SCANTYPE == 12:
            print()
            print()
            print()
            print()
            print("SCTP INIT scan")
            print()
            try:
                nmap.PortScanner("nmap -sY " + TARGET)

            except:
                os.system('nmap -sY ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 13:
            print()
            print()
            print()
            print()
            print("TCP ACK scan")
            print()
            try:
                nmap.PortScanner("nmap -sA " + TARGET)

            except:
                os.system('nmap -sA ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 14:
            print()
            print()
            print()
            print()
            print("TCP Window scan")
            print()
            try:
                nmap.PortScanner("nmap -sW " + TARGET)

            except:
                os.system('nmap -sW ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 15:
            print()
            print()
            print()
            print()
            print("OS scan")
            print()
            try:
                nmap.PortScanner("nmap -O " + TARGET)

            except:
                os.system('nmap -O ' + TARGET)

            print()
            print("Scan finished!")

        elif SCANTYPE == 98:
            automated_scans()
    
        elif SCANTYPE == 99:
            print()
            print()
            print()
            print()
            print("Quitting NWRAP...")
            break
        
        else:
            print(error.errorCodes().ERROR0001)

    print(API.ShadowSuite(current_user, __MODULE_PATH__, __OUTPUT_PATH__, SESSION_ID, USERLEVEL, debugging).FINISH)

def automated_scans():
    print()
    print()
    print()
    print()
    print("Coming soon!")
