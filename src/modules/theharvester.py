########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################

# Module version: 3.2

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
        "name": "The Harvester", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "1.4", # version
        "author": "Christian Martorella", # Author
        "desc": "A tool for gathering e-mail accounts, subdomain names, virtual hosts, open ports/banners, and employee names from different public sources (search engines, pgp key servers).", # Brief description
        "email": "cmartorella@edge-security.com", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Jan. 14, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.4:\nAdding full functionality\n\nVersion 1.0:\nInitial module release"

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
    print("*******************************************************************")
    print("*                                                                 *")
    print("* | |_| |__   ___    /\\  /\\__ _ _ ____   _____  ___| |_ ___ _ __  *")
    print("* | __| '_ \\ / _ \\  / /_/ / _` | '__\\ \\ / / _ \\/ __| __/ _ \\ '__| *")
    print("* | |_| | | |  __/ / __  / (_| | |   \ V /  __/\\__ \\ ||  __/ |    *")
    print("*  \\__|_| |_|\\___| \\/ /_/ \\__,_|_|    \\_/ \\___||___/\\__\\___|_|    *")
    print("*                                                                 *")
    print("* TheHarvester Ver. 2.7.1                                         *")
    print("* Coded by Christian Martorella                                   *")
    print("* Edge-Security Research                                          *")
    print("* cmartorella@edge-security.com                                   *")
    print("*******************************************************************")
    print()
    TARGET = input("Domain to search or company name > ")
    SOURCE = input("(Supported sources:\n\tbaidu\n\tbing,\n\tbingapi\n\tdogpile\n\tgoogle\n\tgoogleCSE\n\tgoogleplus\n\tgoogle-profiles\n\tlinkedin\n\tpgp\n\ttwitter\n\tvhost\n\tyahoo\n\tall\nSelect your data source > ")
    START = input("Start in result number X (default: 0) > ")
    OUTPUT = input("Output filename > ")
    LIMITloop = True
    while LIMITloop == True:
        LIMT = input("Limit the number of results to work with\n(bing goes from 50 to 50 results, google 100 to 100, and pgp doesn't use this option) > ")
        LIMT = LIMT.lower()

        if LIMT == "y":
            LIMITloop = False
            LIMITSWITCH = ' -l '
            LIMIT = input("Set the limit of results to work with > ")

        else:
            LIMITloop = False
            LIMITSWITCH = ''
            LIMIT = ''

    os.system("python2 modules/THEHARVESTER/theHarvester.py -d " + TARGET + " -b " + SOURCE + " -s " + START + " -f $PWD/output/" + OUTPUT + LIMITSWITCH + LIMIT)
    API.Class().finish()
