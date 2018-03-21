# Import directives
import os
import sys
from core import error
# import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "Red Hawk", # Module filename (Change filename if you want to change this)
        "version": "3.0", # version
        "author": "R3D#@0R_2H1N A.K.A Tuhinshubhra", # Author
        "desc": "All in one tool for Information Gathering and Vulnerability Scanning", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Mar. 21, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "False", # Using API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['PHP 7.1.12-1', 'PHP-dev', 'PHP-curl', 'PHP-xml'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 2.0:\nMerge pull request #15 from Romain/master; Fixed a typo\n\nVersion 1.0:\nInitial wrapper module release"

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
    print()
    print("Dependencies:", end=' ')
    for item in dependencies:
        print(item, ",", end=' ')
    print()
    print("Changelog:\n" + "\n" + changelog)
    print("\n\n")

# Main module function
def main():
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            print(error.error0005)
            return 0

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    os.system("php modules/RED_HAWK/rhawk.php")
    print()
