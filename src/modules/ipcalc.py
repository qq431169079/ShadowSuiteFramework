########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

# Module version: 5.0

# Import directives
try:
    import os
    import sys
    import traceback
    from core import error
    from core.logger import log
    import API

    # Place your 'import' directives below
    import ipcalc

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "IPCalc", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "3.0", # version
        "author": "Catayao56", # Author
        "desc": "An IP Calculator.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "Apr. 13, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  
module_status = 0
category = ['ipcalc', 'ip', 'calculator', 'catayao', 'python']

# Changelog of the module
changelog = "Version 3.0:\nMandatory module update\n\nVersion 2.0:\nMandatory module update\n\nVersion 1.0:\nInitial module release"
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
                print(error.ERROR0005)
                return 0

            else:
                module_body()

        else:
            module_body()

def module_body():
    print(info['name'] + '\t' + "An IP Calculator")
    print()
    try:
        ip = str(input("Enter IP Address > "))
        ipc = ipcalc.IP(ip)
        ipn = ipcalc.Network(ip)
        ip_ver = ipc.version()

    except ValueError:
        print("Invalid IP Address!")
        return "Error"

    print("IP Address version: ", ip_ver)
    if ip_ver == 4:
        ipv6 = ipc.to_ipv6()
        print("IP Address v6: ", ipv6)

    elif ip_ver == 6:
        ipv4 = ipc.to_ipv4()
        print("IP Address v4: ", ipv4)

    else:
        print("ERROR: Unsupported or unknown version of IP Address!")

    subnet_size = ipc.subnet()
    print("CIDR subnet size: ", subnet_size)
    flbin = ipc.bin()
    print('Full-length binary: ', flbin)
    flhex = ipc.hex()
    print('Full-length hexadecimal: ', flhex)
    iana_alloc_info = ipc.info()
    print('IANA allocation information:', iana_alloc_info)
    compressed = ipc.to_compressed()
    print('Shortest possible compressed form: ', compressed)
    ptr_rec = ipc.to_reverse()
    print('PTR record: ', ptr_rec)
    net_size = ipc.size()
    print('Network size: ', net_size)
    broadcast_addr = ipn.broadcast()
    print('Broadcast Address: ', broadcast_addr)
    host_first = ipn.host_first()
    print('First available host in this subnet: ', host_first)
    host_last = ipn.host_last()
    print('Last available host in this subnet: ', host_last)
    netmask = ipn.netmask()
    print('Network netmask derived from subnet size, as IP object: ', netmask)
    size = ipn.size()
    print('Number of ip\'s within the network: ', size)
    print()
    print(API.ShadowSuite().FINISH)
