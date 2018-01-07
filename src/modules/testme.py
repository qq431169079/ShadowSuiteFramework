# Import directives
import os
import sys
import core.error
# import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "test", # Module filename (Change filename if you want to change this)
        "version": "1.0", # version
        "author": "none", # Author
        "desc": "none", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "MON. DD, YYYY",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "False", # Using API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none', 'none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nrelease"

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
        print(item, end=' ')

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
    module_info()
