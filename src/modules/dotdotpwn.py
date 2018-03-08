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
    # import API
    # Uncomment the line above if your module will use Shadow Suite's API.

    # Place your 'import' directives below

except ImportError:
    print("[!] A module is missing! Please install the required modules...")

# Put your module information here.
info = {
        "name": "DotDotPwn", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "1.0", # version
        "author": "SecTester", # Author
        "desc": "A very flexible intelligent fuzzer to discover traversal directory vulnerabilities in software such as HTTP/FTP/TFTP servers, Web platforms such as CMSs, ERPs, Blogs, etc.", # Brief description
        "email": "dotdotpwn@sectester.net", # Email
        "authorinfo": "http://dotdotpwn.sectester.net", # Additional information about the author; this could be
        "lastupdate": "Mar. 03, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "False", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['Perl', 'Nmap'] # Put needed dependencies here.  

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
            core.error.error0005()

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    # Remove module_info(), or leave it here. It's your call.
    print("DotDotPwn : The directory Traversal Fuzzer\n")
    print("\n\n[E] Sorry! This module is not yet working! Can you help us develop this module?")

    # DEV0001: Develop this
    """
    module = input("Module [http | http-url | ftp | tftp | payload | stdout] > ")
    url = input("URL with the part to be fuzzed marked as TRAVERSAL (e.g. http://foo:8080/id.php?x=TRAVERSAL&y=31337) > ")
    depth = input("Depth of traversals (e.g. deepness 3 equals to ../../../; default: 6) > ")
    port = input("Port to connect (default: HTTP=80; FTP=21; TFTP=69) > ")
    print("\n\n[i] This module is still under development, so some features are not yet available, like intelligent fuzzing...\n\n")
    print("[i] Running module...")
    os.system("cd modules/DOTDOTPWN && perl dotdotpwn.pl -m " + module + " -u " + url + " -d " + depth + " -x " + port)
    os.system("cd ../..")
    """