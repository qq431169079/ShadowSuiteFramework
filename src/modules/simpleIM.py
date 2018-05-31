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
    import time
    import socket
    import random
    import importlib
    from core import misc
    from getpass import getpass
    from core import multitasking

    from modules.SIMPLEIM import AES
    from modules.SIMPLEIM import DES

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
        "version": "1.2", # version
        "author": "Catayao56", # Author
        "desc": "A simple encrypted messenger in python based on Beyar Nahro's \"talkwithme.py\".", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "May. 25, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3'] # Put needed dependencies here.
module_status = 0 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
category = ['all', 'python', 'encrypt', 'message', 'messenger', 'messaging', 'catayao', 'python', 'beyar', 'nahro', 'im']
#files = [] # Uncomment this line if the module needs a subdirectory to use.
#E.g.: MODULE_NAME_OR_SUBDIRECTORY_NAME/

# <!--HTML Fan? No, not really :P -->
global H1
global H2
global P1
global P2
global P3
global BR
H1 = misc.FB + misc.FI + misc.CC # Title
H2 = misc.FB + misc.CC # Subtitle
BR = misc.END # Break of colors
P1 = '[' + misc.CB + "?" + BR + '] ' # Information msg
P2 = '[' + misc.CY + "!" + BR + '] ' # Warning msg
P3 = '[' + misc.CR + "#" + BR + '] ' # Error msg

# Changelog of the module
changelog = "Version 1.2:\nModule update.\n\nVersion 1.1:\nUpdated Module.\n\nVersion 1.0:\nInitial module release"
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

    ### VARIABLE DECLARATIONS ###
    misc = API.misc
    mpf = misc.programFunctions()
    try:
        module_path = global_variables['MODULE_PATH'].replace('/', '.') + 'ipify'
        ipify = importlib.import_module(module_path)
        ip = ipify.API() # Get the current device IP Address.

    except Exception as ipifyexception:
        #ip = str(ipifyexception)
        ip = traceback.print_exc()
        
    ### DEFAULT SETTINGS ###
    user_sets = {
            "username": global_variables['current_user'],
            "password": global_variables['USERPASS'],
            "ip": ip,
            }

    server_sets = {
            "port": 8220,
            "algorithm": "Plaintext", # Plaintext? Algorithm? When did Plaintext become an algorithm?!?
            "key": "",
            "hash": "MD5",
            "sign": "None",
            "whitelist": True, #If true, use allowed_ips and allowed_ports; Otherwise, no.
            "allowed_ips": ["127.0.0.1"],
            "allowed_ports": [8220, 8221, 8222, 8223, 8224]
            }

    client_sets = {
            "port": 8220,
            "key": "",
            }

    sets = (user_sets, server_sets, client_sets)

    #print(settings) # DEV0005: For debugging purposes only
    #input()

    # Check if authentication is required.
    if global_variables['USERNAME'] != '' and global_variables['USERPASS'] != '':
        success = Security(global_variables).verify()

    else:
        success = True

    if success:
        del success
        pass

    else:
        return None

    # Start of the loop
    while True:
        try:
            mpf.clrscrn()
            print()
            print(banner())
            print()
            print(P1 + "Current User: " + sets[0]["username"])
            print(P1 + "Current IP: " + sets[0]["ip"])
            print(P1 + "Current Time: " + current_time())
            print()
            print(misc.CLG + "[01] Start a Server" + misc.END)
            print(misc.CG + "[02] Start a Client" + misc.END)
            print(misc.CY + "[03] Configure settings" + misc.END)
            print()
            print(misc.CR + "[99] Reset data and quit" + misc.END)
            print()
            selection = int(input(prompt(global_variables)))
            if selection == 1:
                pass

            elif selection == 2:
                pass

            elif selection == 3:
                user_sets, client_sets, server_sets = settings(user_sets, client_sets, server_sets).main()

            elif selection == 99:
                print(API_ShadowSuite.FINISH)
                break

            else:
                raise ValueError("Invalid selection!")

        except Exception as exceptionerrmsg:
            traceback.print_exc()
            print("[i] " + str(exceptionerrmsg))
            mpf.pause()

def prompt(global_variables):
    return("[" + str(global_variables['current_user']) + "@" + info['name'] + "] ")

def banner():
    return(info['name'] + " " + info['version'] + " :: " + info['desc'])

def current_time():
    return time.asctime()

class Security:

    def __init__(self, global_variables):
        self.gv = global_variables

    def verify(self):
        print(P1 + "Please login first.")
        ulogin = input("Username: ")
        plogin = getpass()
        if misc.programFunctions().login_user(self.gv, ulogin, plogin) == 'Login Successful!':
            print(P1 + "User verified!")
            return True

        else:
            print(P3 + "Invalid credentials!")
            return False

class Settings:

    def __init__(self, user_sets, client_sets, server_sets):
        self.user_sets = user_sets
        self.client_sets = client_sets
        self.server_sets = server_sets

    def main():
        while True:
            try:
                mpf.clrscrn()
                print()
                print(banner())
                print()
                print(H1 + "===User Information===")
                print("Current User:                " + self.user_sets["username"])
                print("Current Password:            " + ('=' * len(self.user_sets["password"])))
                print("Current IP:                  " + self.user_sets["ip"])
                print()
                print(H2 + "===Server Information===")
                print("Listening Port:              " + str(self.server_sets["port"]))
                print("Encryption Algorithm:        " + self.server_sets['algorithm'])
                print("Encryption Key:              " + ('=' * len(self.server_sets['key'])))
                print("Hashing Algorithm:           " + self.server_sets['hash'])
                print("Digital Signature Algorithm: " + self.server_sets['sign'])
                if self.server_sets['whitelist']:
                    print("Whitelist Mode:          True")
                    print("Allowed IPs:")
                    iterator = 0
                    while iterator < (len(self.server_sets['allowed_ips']) - 1):
                        print("\t" + P1 + self.server_sets['allowed_ips'][iterator])

                    print()
                    print("Allowed Ports:")
                    iterator = 0
                    while iterator < (len(self.server_sets['allowed_ports']) -1):
                        print("\t" + P1 + self.server_sets['allowed_ports'][iterator])

                    print()

                else:
                    print("Whitelist Mode:          False")
                    print("Allowed IPs:             N/A")
                    print("Allowed Ports:           N/A")

            except Exception as e:
                print(P3 + str(e))
                mpf.pause()
