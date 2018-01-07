# Import directives
import os
import sys
import core.error
import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "Automater", # Module filename (Change filename if you want to change this)
        "version": "1.0", # version
        "author": "TekDefense", # Author
        "desc": "IP, URL, and Hash Passive Analysis tool", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Jan, 06, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Using API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nInitial module release"

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
def main():
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            core.error.error0005()

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    print("\nAutomater -- " + info['desc'] + "\n")
    print("List one IP Address (CIDR or dash notation accepted),\nURL or Hash to query or pass the filename of a file\ncontaining IP Address info, URL or Hash to query each\nseparated by a newline.")
    target = input(" > ")
    print()
    output = input("Enter the name of the output file > ")
    ask_proxy = input("Do you want to use a proxy? > ")
    if ask_proxy == "y":
        # DEV 0003: continue...
