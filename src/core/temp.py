# Import directives
import os
import sys
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
        "lastupdate": "04.01.2018", # Last update on:           a website of the author.
        "usingapi": False, # Using API?
        "needsroot": False, # Does this module needs root permissions?
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nrelease"

# Prints the module information
def module_info():
    print("Module Name: " + info['name'])
    print("Module Version: " + info['version'])
    print("Module Author: " + info['author'])
    print("Module Description: " + info['desc'])
    print()
    print("Module Author's Email: " + info['email'])
    print("Module Author's Info: " + info['authorinfo'])
    print("Module's last update: " + info['lastupdate'])
    print("Using Shadow Suite's API: " + info['usingapi'])
    print("Needs root: " + info['needsroot'])

# Main module function
def main():
    module_info()
    sys.exit(0)
