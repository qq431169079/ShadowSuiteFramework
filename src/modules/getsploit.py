########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

module_version = 7.3

# Import directives
try:
    import os
    import sys
    import traceback
    from core import error
    from core.logger import log
    import API

    # Place your 'import' directives below

    import_error = False

except(ImportError, ModuleNotFoundError):
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "GetSploit", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "1.0", # version
        "author": "Kir Ermakov", # Author
        "desc": "It allows you to search online for the exploits across all the most popular collections: Exploit-DB, Metasploit, Packetstorm and others.", # Brief description
        "email": "isox(at)vulners.com", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "May. 17, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3', 'PYTHON: urllib', 'PYTHON: argparse', 'PYTHON: optparse', 'PYTHON: textwrap', 'PYTHON: optik', 'PYTHON: sqlite3'] # Put needed dependencies here.
module_status = 0 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
category = ['all', 'python', 'search', 'exploit', 'online', 'database', 'metasploit', 'packetstorm', 'vuln']
files = ['GETSPLOIT/'] # Uncomment this line if the module needs a subdirectory to use.
#E.g.: MODULE_NAME_OR_SUBDIRECTORY_NAME/

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
def main(global_variables):
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
                module_body(global_variables)

        else:
            module_body(global_variables)

def module_body(global_variables):
    # To support module versions older than v7.0
    API_ShadowSuite = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING'])
    misc = API.misc
    
    print()
    print(info['name'] + " " + info['version']+ " :: " + info['desc'])
    print()
    print("Type 'help' for information")
    print()
    while True:
        try:
            getsploit_comm = input("[" + global_variables['current_user'] + "@GETSPLOIT] $ ")
            if getsploit_comm.lower().startswith("help"):
                print()
                print("""usage: Exploit search and download utility [-h] [-t] [-j] [-m] [-c COUNT] [-l]
                                           [-u]
                                           [query [query ...]]

positional arguments:
  query                 Exploit search query. See https://vulners.com/help for
                        the detailed manual.

optional arguments:
  -h, --help            show this help message and exit
  -t, --title           Search JUST the exploit title (Default is description
                        and source code).
  -j, --json            Show result in JSON format.
  -m, --mirror          Mirror (aka copies) search result exploit files to the
                        subdirectory with your search query name.
  -c COUNT, --count COUNT
                        Search limit. Default 10.
  -l, --local           Perform search in the local database instead of
                        searching online.
  -u, --update          Update getsploit.db database. Will be downloaded in
                        the script path.

module commands:
  help                  Prints this help menu.
  quit                  Quit GetSploit module.
[i] In this case, you only need to supply the arguments, and the module will do the rest for you. """)
                print()

            elif getsploit_comm.lower().startswith("quit"):
                print(API_ShadowSuite.FINISH)
                break

            else:
                #print("skek") # DEV0005
                os.system("cd " + global_variables['MODULE_PATH'] + "/GETSPLOIT && python3 getsploit.py " + getsploit_comm)
                #print("kdkd") # DEV0005
                paths = os.listdir(global_variables['MODULE_PATH'] + '/GETSPLOIT/')
                #print(paths) # DEV0005
                for path in paths:
                    #print(path) # DEV0005
                    if path == '__pycache__':
                        continue

                    else:
                        if misc.programFunctions().isfolder(global_variables['MODULE_PATH'] + 'GETSPLOIT/' + path):
                            if misc.programFunctions().is_windows():
                                os.system("move " + global_variables['MODULE_PATH'] + 'GETSPLOIT/' + path + " " + global_variables['OUTPUT_PATH'])

                            else:
                                os.system("mv -f " + global_variables['MODULE_PATH'] + "GETSPLOIT/" + path + " " + global_variables['OUTPUT_PATH'])

                        else:
                            continue

        except Exception as err:
            print(misc.BR + misc.CK + "[EXCEPTION] " + str(err) + misc.END)
            continue

        except(urllib.error.URLError, socket.gaierror) as sockerr:
            print(misc.BR + misc.CK + "[EXCEPTION] " + str(sockerr) + misc.END)
            continue
