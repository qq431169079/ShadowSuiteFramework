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
    import time
    import socket
    from modules.DECEPTION import httpd

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Deception", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "5.0", # version
        "author": "Catayao56", # Author
        "desc": "A simple low-interaction honeypot server.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56", # Additional information about the author; this could be
        "lastupdate": "Apr. 13, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['PYTHON: twisted'] # Put needed dependencies here.  
module_status = 0
category = ['deception', 'catayao', 'python', 'low', 'interaction', 'honeypot', 'server', 'http', 'ftp', 'ssh', 'telnet', 'snmp', 'smtp']

# Changelog of the module
changelog = "Version 5.0:\nMandatory module update\n\nVersion 4.0:\nMore honeypot types\n\nVersion 3.0:\nMandatory module update\n\nVersion 2.0:\nFixed bugs\n\nVersion 1.0:\nInitial module release"
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

def getBasicInput():
    host = input('IP Address: ')
    while True:
        try:
            port = int(input('Port: '))

        except TypeError:
            print('Error: Invalid port number.')
            continue

        else:
            if (port < 1) or (port > 65535):
                print('Error: Invalid port number.')
                continue

            else:
                return(host, port)

def telnet_writeLog(client, data=''):
    separator = '=' * 50
    fopen = open('./output/telnet_honeypot.log', 'a')
    fopen.write('Time: %s\nIP: %s\nPort: %d\nData: %s\n%s\n\n'%(time.ctime(), client[0], client[1], data, separator))
    fopen.close()

def ftp_writeLog(client):
    separator = '=' * 50
    fopen = open('./output/ftp_honeypot.log', 'a')
    fopen.write('Time: %s\nIP: %s\nPort: %s\n%s\n\n'%(time.ctime(), client[0], client[1], separator))

def HTTP_honeypot():
    url = input("URL to emulate: ")
    if 'http' not in url:
        url = 'http://' + url

    while True:
        port = int(input("Port: "))
        if port < 1 or port > 65535:
            print("Error: Invalid port number.")
            continue

        else:
            break
    try:
        print("[i] Starting HTTP honeypot!")
        #httpd.__url__privatemethod = url
        #httpd.__port__privatemethod = port
        s = httpd.httpd(url, port)
        s.clone()
        s.serve()

    except KeyboardInterrupt:
        s.cleanup()
        print("\n[i] HTTP Honeypot shutting down... Bye!")

    except OSError:
        print("The port we are trying to use is already being used by another process. Sorry!")

    except PermissionError:
        print(error.ERROR0005)

def Ftp_honeypot():
    host, port = getBasicInput()
    try:
        print('Starting FTP honeypot!')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(100)
        while True:
            (insock, address) = s.accept()
            print('[' + time.asctime() +'] Connection from %s port %d' % (address[0], address[1]))
            try:
                insock.close()
            except KeyboardInterrupt:
                print("\nFTP honeypot shutting down... Bye!")
            
            except socket.error as e:
                ftp_writeLog(address)

            else:
                ftp_writeLog(address)
            
    except KeyboardInterrupt:
        print("\nFTP honeypot shutting down... Bye!")

    except OSError:
        print("The port we are trying to use is already being used by another process. Sorry!")
    
    except PermissionError:
        print(error.ERROR0005)

def Telnet_honeypot():
    host, port = getBasicInput()
    motd = input("MOTD #1 (Enter '' (none) for default): ")
    if motd == None or motd == "":
        motd = """\



Ubuntu LTS 16.1 Telnet Server

#################################################################################
#                                                                               #
# AUTHORIZED USERS ONLY! DISCONNECT IF YOU ARE NOT ONE OF THE AUTHORIZED USERS! #
#                                                                               #
#################################################################################

Login: """

    motd = motd.encode()

    motd2 = input("MOTD #2 (Enter '' (none) for default: ")
    if motd2 == None or motd2 == '':
        motd2 = """\

Password: """

    motd2 = motd2.encode()

    honey_reply = input("Do you want to send a message to the attacker? (Makes the honeypot suspicious; y/n) > ").lower()
    if honey_reply == 'y':
        reply = input("Message: ").encode()

    elif honey_reply == 'n':
        print("[i] You choosed to not send a message. Wise choice, dude!")
        reply = None

    else:
        print("[i] Unknown answer, assuming no...")
        reply = None

    try:
        print('Starting Telnet honeypot!')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen(100)
        while True:
            (insock, address) = s.accept()
            print('[' + time.asctime() + '] Connection from %s port %d' % (address[0], address[1]))
            try:
                insock.send(motd)
                data = insock.recv(1024)
                insock.send(motd2)
                data = insock.recv(1024)
                if reply == None or reply == "":
                    pass

                else:
                    insock.send(reply)
                    data = insock.recv(1024)

                insock.close()

            except KeyboardInterrupt:
                print("\nTelnet honeypot shutting down... Bye!")

            except socket.error as e:
                telnet_writeLog(address)

            else:
                telnet_writeLog(address, data)

    except KeyboardInterrupt:
        print("\nTelnet honeypot shutting down... Bye!")

    except OSError:
        print("The port we are trying to use is already being used by another process. Sorry!")

    except PermissionError:
        print(error.ERROR0005)

def module_body():
    BANNER = r"""
 ____                      _   _
|  _ \  ___  ___ ___ _ __ | |_(_) ___  _ __
| | | |/ _ \/ __/ _ \ '_ \| __| |/ _ \| '_ \
| |_| |  __/ (_|  __/ |_) | |_| | (_) | | | |
|____/ \___|\___\___| .__/ \__|_|\___/|_| |_|
                    |_|         v{}
    """
    while True:
        try:
            pf = API.misc.programFunctions()
            pf.clrscrn()
            print(BANNER.format(info['version']))
            print()
            print("Current Time: " + time.asctime())
            print()
            print("[01] HTTP (80) Honeypot")
            print("[02] FTP (20,21) Honeypot")
            print("[03] SMTP (25) Honeypot")
            print("[04] Telnet (23) Honeypot")
            print("[05] SSH (22) Honeypot")
            print("[06] SNMP (161,162) Honeypot")
            print()
            print("[99] Quit")
            honeytype = int(input("[DECEPTION]: "))
            if honeytype == 1:
                HTTP_honeypot()

            elif honeytype == 2:
                Ftp_honeypot()

            elif honeytype == 3:
                continue

            elif honeytype == 4:
                Telnet_honeypot()

            elif honeytype == 5:
                continue

            elif honeytype == 6:
                continue

            elif honeytype == 99:
                print(API.ShadowSuite().FINISH)
                return 0

            else:
                print(error.ERROR0001)

            API.misc.programFunctions().pause()

        except KeyboardInterrupt:
            print(error.ERROR0002)

        except(ValueError, TypeError):
            pass
