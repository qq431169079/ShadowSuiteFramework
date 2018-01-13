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
import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "DNSEnum", # Module filename (Change filename if you want to change this)
        "version": "1.0", # version
        "author": "Filip Waeytens", # Author
        "desc": "multithreaded perl script to enumerate DNS information of a domain\nand to discover non-contiguous ip blocks.", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Jan. 08, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['Perl'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nInitial module release"

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
    print()
    print("DNSEnum")
    print()
    target = input("Target Domain > ")
    output = input("Output filename > ")
    print("Performing enumeration...")
    os.system("perl modules/DNSENUM/dnsenum.pl --enum -v -o $PWD/output/"+ output + " " + target)
    print()
    API.Class().finish()