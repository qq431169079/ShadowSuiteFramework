########################################################################################
#                                                                                      #
#                             MODULE FOR SHADOW SUITE                                  #
#                                                                                      #
########################################################################################

# Module version: 3.0

# Import directives
try:
    import os
    import sys
    from core import error
    import API
    # Uncomment the line above if your module will use Shadow Suite's API.
except ImportError:
    print("[!] A module is missing! Please install the required modules...")

# Put your module information here.
info = {
        "name": "Metagoofil", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "2.0", # version
        "author": "Christian Martorella", # Author
        "desc": "A tool for extracting metadata of public documents (pdf,doc,xls,ppt,etc) availables in the target websites.", # Brief description
        "email": "cmartorella@edge-security.com", # Email
        "authorinfo": "none", # Additional information about the author; this could be
        "lastupdate": "Mar. 21, 2018",                     # a website of the author.
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
            print(error.error0005)

        else:
            module_body()

    else:
        module_body()

def module_body():
    # Place your program here. This is the function where your program will be placed.
    # Remove module_info(), or leave it here. It's your call.
    print()
    print("==METAGOOFIL==")
    print()
    print("[01] - Work with remote target")
    print("[02] - Work with local target")
    print()
    print("[99] - Quit")
    print()
    rem_or_loc = input(" > ")
    if rem_or_loc == "1":
        remote()

    elif rem_or_loc == "2":
        local()

    elif rem_or_loc == "99":
        pass

    else:
        API.core.error.error0001()

def remote():
    # This function is called if user wants to work with remote target.
    target = input("Domain to search: ")
    filetypes = input("filetype/s to download (pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx): ")
    search_limit = input("results to search (enter 200 for default): ")
    downld_limit = input("files to download: ")
    wd = input("working directory (location to save downloaded files): ")
    output = input("HTML Output filename: ")
    print()
    print("Running...")
    os.system("cd modules/METAGOOFIL && python2 metagoofil.py -d " + target + " -t " + filetypes + " -l " + search_limit + " -n " + downld_limit + " -o ../../output/" + wd + " -f ../../output/" + output + ".html")
    os.system("cd ../..")
    print("Running... Done!")

def local():
    # This function is called if user wants to work with local target.
    target = input("Working directory (where to find downloaded files): ")
    output = input("HTML Output filename: ")
    print()
    print("Running...")
    os.system("cd modules/METAGOOFIL && python2 metagoofil.py -h yes -o " + target + " -f " + output + ".html")
    os.system("cd ../..")
    print("Running... Done!")
