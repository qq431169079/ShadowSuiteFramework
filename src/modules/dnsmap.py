# Import directives
import os
import sys
from core import error
# import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here
import socket

# Put your module information here.
info = {
        "name": "DNSmap", # Module filename (Change filename if you want to change this)
        "version": "2.0", # version
        "author": "Filip Waeytens", # Author
        "desc": "Dnsmap is mainly meant to be used by pentesters during the information\ngathering/enumeration phase of infrastructure security assessments.", # Brief description
        "email": "N/A", # Email
        "authorinfo": "N/A", # Additional information about the author; this could be
        "lastupdate": "Mar. 21, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "False", # Using API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

# Changelog of the module
changelog = "Version 1.0:\nInitial module release"

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

# Main module function
def main():
    if info['needsroot'] == "0":
        if os.geteuid() != 0:
            print(error.error0005)
            return 0

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Colours
    D  = "\033[0m"
    W  = "\033[01;37m"
    O  = "\033[01;33m"
    SUCESS = "\033[01;32m"
    FAIL = "\033[01;31m"
    print("\nDNSMap\n")
    print (W+"")
    domain = input("[DNSMap] Set domain: ") # www.domain.com

    try:
        ip = socket.gethostbyname(domain)
        print (SUCESS + "The DNS of \'" + domain + "\' is \'" + ip + "\'.")

    except socket.gaierror:
        print (FAIL+'Invalid Domain or no internet connection.\n')
