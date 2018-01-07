########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################

# Module version: 2.5

# Import directives
import os
import sys
import core.error
# import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "NWrap", # Module filename (Change filename if you want to change this)
        "version": "3.4", # version
        "author": "Catayao56", # Author
        "desc": "Wrapper script for NMap Network Mapper.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Jan. 07, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "False", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['NMap'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 3.4:\nRewritten to be a Shadow Suite module\n\nVersion 3.0:\nAdded new scan types\n\nVersion 2.1:\nFixed bugs\n\nVersion 1.0:\nInitial module release"

# Prints the module information
def module_info():
    # Unofficial way to convert integer to Boolean. if [argument] == 0 then True;
    # Otherwise, False.
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
    # and modify it XD
    print("Dependencies:", end=' ')
    for item in dependencies:
        print(item, ",", end=' ')
    print()
    # Prints the changelog of the module.
    print("Changelog:\n" + "\n" + changelog)
    print("\n\n")

# Main module function
def main():
    """ First, it checks the value assigned to the 'needsroot' variable in the 
    dictionary 'info', then if the value is equal to zero, it calls the 'geteuid()'
    function from the 'os' module. If the result from geteuid is also zero, then
    the module will call the function 'module_body()'. Otherwise, it will print an
    error message. If the value assigned to the 'needsroot' variable in the dictionary
    'info' is not equal to zero, then the module will not call the 'geteuid()' function
    from the 'os' module, and will immediately call 'module_body()' function. """
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            core.error.error0005()

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    # Remove module_info(), or leave it here. It's your call.
    print("Nmap: Network exploration tool and security / port scanner\n\n")
    print("Target's IP Address or URL: ")
    TARGET = input("[NWRAP] > ")
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
    print("Ping Scanning Types:")
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
    print("[15] OS scan              [i] ROOT REQUIRED\n\n")
    print("[99] Quit")
    # nmap -O [TARGET]
    print()
    SCANTYPE = input("[NWRAP] > ")
    
    if SCANTYPE == "1":
        print()
        print()
        print()
        print()
        print("TCP Connect scan")
        print()
        os.system("nmap -sT " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "2":
        print()
        print()
        print()
        print()
        print("Half-open scan")
        print()
        os.system("nmap -sS " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "3":
        print()
        print()
        print()
        print()
        print("Ping scan")
        print()
        os.system("nmap -sP " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "4":
        print()
        print()
        print()
        print()
        print("UDP scan")
        print()
        os.system("nmap -sU " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "5":
        print()
        print()
        print()
        print()
        print("IP Protocol scan")
        print()
        os.system("nmap -sO " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "6":
        print()
        print()
        print()
        print()
        print("TCP SYN ping")
        print()
        os.system("nmap -PS20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "7":
        print()
        print()
        print()
        print()
        print("TCP ACK ping")
        print()
        os.system("nmap -PA20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "8":
        print()
        print()
        print()
        print()
        print("UDP ping")
        print()
        os.system("nmap -PU20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "9":
        print()
        print()
        print()
        print()
        print("SCTP INIT ping")
        print()
        os.system("nmap -PY20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "10":
        print()
        print()
        print()
        print()
        print("ARP ping")
        print()
        os.system("nmap -PR20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "11":
        print()
        print()
        print()
        print()
        print("List scan")
        print()
        os.system("nmap -sL " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "12":
        print()
        print()
        print()
        print()
        print("SCTP INIT scan")
        print()
        os.system("nmap -sY " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "13":
        print()
        print()
        print()
        print()
        print("TCP ACK scan")
        print()
        os.system("nmap -sA " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "14":
        print()
        print()
        print()
        print()
        print("TCP Window scan")
        print()
        os.system("nmap -sW " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "15":
        print()
        print()
        print()
        print()
        print("OS scan")
        print()
        os.system("nmap -O " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "99":
        print()
        print()
        print()
        print()
        print("Quitting NWRAP...")

    else:
	    core.error.error0001()

