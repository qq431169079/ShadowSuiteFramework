########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################
# Coding=UTF-8

# Module version: 3.5

# Import directives
try:
    import os
    import sys
    from core import error
    import API
    # Uncomment the line above if your module will use Shadow Suite's API.

    # Place your 'import' directives below

except ImportError:
    print("[!] A module is missing! Please install the required modules...")

# Put your module information here.
info = {
        "name": "Common User Passwords Profiler (CUPP)", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "2.0", # version
        "author": "Muris Kurgas aka j0rgan", # Author
        "desc": "Common user passwords profiler.", # Brief description
        "email": "j0rgan@remote-exploit.org", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Mar. 21, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nInitial module release"
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
    """ First, it checks the value assigned to the 'needsroot' variable in the 
    dictionary 'info', then if the value is equal to zero, it calls the 'geteuid()'
    function from the 'os' module. If the result from geteuid is also zero, then
    the module will call the function 'module_body()'. Otherwise, it will print an
    error message. If the value assigned to the 'needsroot' variable in the dictionary
    'info' is not equal to zero, then the module will not call the 'geteuid()' function
    from the 'os' module, and will immediately call 'module_body()' function. """
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            print(error.error0005)

        else:
            module_body()

    else:
        module_body()

def module_body():
    go = "cd modules/CUPP"
    back = os.system("cd ../..")
    print("  ___________")
    print(" | cupp.py! |               # Common")
    print("      \\                     # User")
    print("       \\   ,__,             # Passwords")
    print("        \\  (oo)____         # Profiler")
    print("           (__)    )\\")
    print("              ||--|| *   Muris Kurgas <j0rgan@remote-exploit.org>")
    print('\n\nOutput files are in the modules/CUPP folder...\n\n')
    print("[1] Interactive questions for user password profiling")
    print("[2] Use this option to improve existing dictionary, or WyD.pl output to make some pwnsauce")
    print("[3] Download huge wordlists from repository")
    print("[4] Test CUPP.py")
    print("\n[9] Quit\n\n")
    select = input("Input > ")
    select = int(select)
    if select == 1:
        os.system(go + " && python cupp3.py -i -q")
        back

    elif select == 2:
        os.system(go + " && python cupp3.py -w -q")
        back

    elif select == 3:
        os.system(go + " && python cupp3.py -l -q")
        back

    elif select == 4:
        os.system(go + " && python test_cupp.py")
        back

    elif select == 9:
        return

    else:
        print(error.error0001)