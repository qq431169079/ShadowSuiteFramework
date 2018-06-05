########################################################################################
#                                                                                      #
#                       SERVICE FOR SHADOW SUITE FRAMEWORK                             #
#                                                                                      #
########################################################################################
# Coding=UTF-8

service_version = 1.0

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

# Put your service information here.
info = {
        "name": "service test", # Service filename (Change this; I recommend you to use the filename as the service name.)
        "version": "1.0", # version
        "author": "none", # Author
        "desc": "none", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "MON. DD, YYYY",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this service using Shadow Suite's API?
        "needsroot": "1", # Does this service needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3', 'PYTHON: none'] # Put needed dependencies here.
service_status = 1 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
#files = [] # Uncomment this line if the service needs a subdirectory to use.
#E.g.: SERVICE_NAME_OR_SUBDIRECTORY_NAME/

# Changelog of the service
changelog = "Version 1.0:\nInitial servicee release"
# Changelog format:
#
# changelog = "Version 2.0:\nUpdate Description\n\nVersion1.0\nInitial service release"

# Prints the servicee information
def service_info():
    # Unofficial way to convert integer to Boolean
    # (well, not really a boolean, as it is a string).
    # if [argument] == 0 then True; Otherwise, False.
    if info['needsroot'] == "0":
        superm = "True"
    else:
        superm = "False"

    print("Service Name: " + info['name'])
    print("Service Version: " + info['version'])
    print("Service Author: " + info['author'])
    print("Service Description: " + info['desc'])
    print()
    print("Service Author's Email: " + info['email'])
    print("Service Author's Info: " + info['authorinfo'])
    print("Service's last update: " + info['lastupdate'])
    print("Shadow Suite API Support: " + info['usingapi'])
    print("Needs root: " + superm)
    print()
    # Prints the dependencies via for loop. I just copy/pasted it from a reference book
    # and modified it XD
    print("Dependencies:", end=' ')
    for item in dependencies:
        print(item, ",", end=' ')
    print()
    # Prints the changelog of the service.
    print("Changelog:\n" + "\n" + changelog)
    print("\n\n")

# Main service function
def main(global_variables):
    if import_error is True:
        return None

    else:
        """ First, it checks the value assigned to the 'needsroot' variable in the 
        dictionary 'info', then if the value is equal to zero, it calls the 'geteuid()'
        function from the 'os' module. If the result from geteuid is also zero, then
        the module will call the function 'service_body()'. Otherwise, it will print an
        error message. If the value assigned to the 'needsroot' variable in the dictionary
        'info' is not equal to zero, then the module will not call the 'geteuid()' function
        from the 'os' module, and will immediately call 'service_body()' function. """
        if info['needsroot'] == "0":
            if os.geteuid() != 0:
                print(error.errorCodes().ERROR0005)
                return 0

            else:
                service_body(global_variables)

        else:
            service_body(global_variables)

def service_body(global_variables):
    # To support module versions older than v7.0
    # Remember, services and modules use the same API!
    API_ShadowSuite = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING'])
    # Place your program here. This is the function where your program will be placed.
    # Remove service_info(), or leave it here. It's your call.
    service_info()
    print()
    print(error.warningCodes().WARNING0002)
    print(API_ShadowSuite.FINISH)
