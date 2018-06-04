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
        "name": "SimpleIM", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "5.0", # version
        "author": "Catayao56", # Author
        "desc": "An encrypted instant messaging platform for simple and secure chatting.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "Jun. 03, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['PYTHON: socket'] # Put needed dependencies here.
module_status = 1 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
category = ['all', 'python', 'encrypt', 'instant', 'messag', 'im', 'chat']
#files = [] # Uncomment this line if the module needs a subdirectory to use.
#E.g.: MODULE_NAME_OR_SUBDIRECTORY_NAME/

# Changelog of the module
changelog = "Version 5.0:\nRewrite of SimpleIM\n\nVersion 4.0:\nRewrite of SimpleIM\n\nVersion 3.0:\nRewrite of SimpleIM\n\nVersion 2.0:\nModule update\n\nVersion 1.0:\nInitial module release"
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
    ip = API.SSFMain(global_variables).use_module_API('ipify')
    cannot_connect = False
    if 'ERROR' in ip:
        ip = '127.0.0.1'
        cannot_connect = True
    
    while True:
        try:
            API_ShadowSuite.clrscrn()
            print(info['name'] + " :: " + info['desc'])
            if cannot_connect:
                print("[i] Cannot contact the External IP Address API...")

            print()
            print("[01] Connect to a chatroom")
            print("[02] Start SimpleIM Server service")
            print()
            print("[99] Quit")
            selection = int(input("[" + global_variables['current_user'] + " @ " + ip + "] "))
            if selection == 1:
                connect()

            elif selection == 2:
                API.SSFMain(global_variables).send_command("services enable simpleIM_Server")

            elif selection == 99:
                return 0

            else:
                raise ValueError("Please input a valid option!")

        except Exception as e:
            print("[i] " + str(e))

        API_ShadowSuite.pause()

def connect():
    addr = input("Server/Chatroom IP and Port (e.g.: 127.0.0.1:9009): ")
    if ':' not in addr:
        raise ValueError("Server Port is needed!")
    
    else:
        addr = addr.split(':')
        print(addr)
