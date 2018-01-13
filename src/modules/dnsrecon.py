########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################

# Module version: 2.6

# Import directives
import os
import sys
import core.error
import API
# Uncomment the line above if your module will use Shadow Suite's API.

# Place your 'import' directives here

# Put your module information here.
info = {
        "name": "DNSrecon", # Module filename (Change filename if you want to change this)
        "version": "1.0", # version
        "author": "N/A", # Author
        "desc": "DNS reconnaissance tool", # Brief description
        "email": "none", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Jan. 12, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

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
    print("\n\n\n")
    target = input("Target Domain: ")
    print()
    print("Enumeration Types:")
    print("std       SOA, NS, A, AAAA, MX and SRV.")
    print("rvl       Reverse lookup of a given CIDR or IP range.")
    print("brt       Brute force domains and hosts using a given dictionary.")
    print("srv       SRV records.")
    print("axfr      Test all NS servers for a zone transfer.")
    print("goo       Perform Google search for subdomains and hosts.")
    print("bing      Perform Google search for subdomains and hosts.")
    print("snoop     Perform cache snooping against all NS servers for a given domain, testing")
    print("          all with file containing the domains, file given with -D option.")
    print("tld       Remove the TLD of given domain and test against all TLDs registered in IANA.")
    print("zonewalk  Perform a DNSSEC zone walk using NSEC records.")
    print()
    enumtype = input("Type of enumeration to perform (Comma separated; choose any of the above): ")
    output = input("Output filename: ")
    print()
    print("Running...")
    os.system("cd modules/DNSRECON && python dnsrecon.py -d " + target + " -t " + enumtype + " --xml " + output)
    os.system("cd ../..")
    API.Class().finish()