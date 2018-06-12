#!/usr/bin/env python3
import os
import sys
from subprocess import call
from time import sleep as timeout

def main():
    try:
        if sys.argv[1] in ('-h', '--help', '--usage'):
            print()
            print("Usage: " + sys.argv[0] + "[SWITCHES]")
            print()
            print("This script is made to setup the repository for every")
            print("comands like clone, commit, checkout, etc.")
            print()
            print("SWITCHES:")
            print("-s    --setup    setup        Setup newly-cloned repository.")
            print("-c    --commit   commit       Git commit wrapper.")
            print()
            sys.exit(0)

        else:
            if os.path.exists('.git'):
                if sys.argv[1] in ('-s', '--setup', 'setup'):
                    print("Setting up SSF in PATH:\n\t" + os.getcwd())
                    timeout(1)
                    try:
                        with open('.git/info/exclude', 'a') as fopen:
                            fopen.write('src/dev/FUTURE/\n')
                            fopen.write('src/data/*.dat\n')
                            fopen.write('__pycache__/\n')
                            fopen.write('*.pyc\n')

                    except(IOError, EOFError, FileNotFoundError):
                        print("Cannot write to .git/info/exclude!")
                        sys.exit(3)

                    else:
                        call(['git', 'gc'])
                        timeout(3)
                        call(['git', 'status'])
                        timeout(3)
                        call(['git', 'log', '--graph'])
                        print("Finished setting up repository!")
                        sys.exit(0)

                elif sys.argv[1] in ('-c', '--commit', 'commit'):
                    print("Please manually update the contents of these files...")
                    timeout(3)
                    call(['vim', 'README.md', 'README-DEV', 'MANUAL', 'src/core/__init__.py', 'src/core/version.py'])
                    try:
                        with open('src/core/__init__.py') as fopen:
                            data = fopen.readlines()

                        for dat in data:
                            if dat.startswith('__version__'):
                                version = dat.partition('=')[2]
                                version = version.replace(' ', '')
                                version = version.replace('"', '')
                                version = version.replace("'", '')

                            elif dat.startswith('__codename__'):
                                codename = dat.partition('=')[2]
                                codename = codename.replace('"', '')
                                codename = codename.replace("'", '')

                            elif dat.startswith('__type__'):
                                vtype = dat.partition('=')[2]
                                vtype = vtype.replace(' ', '')
                                vtype = vtype.replace('"', '')
                                vtype = vtype.replace("'", '')

                            elif dat.startswith('__edition__'):
                                edition = dat.partition('=')[2]
                                edition = edition.replace(' ', '')
                                edition = edition.replace('"', '')
                                edition = edition.replace("'", '')

                            else:
                                continue

                        assert(version is not '' and version is not \
                                None), "Cannot get version!"

                    except(IOError, EOFError, FileNotFoundError, AssertionError):
                        print("Cannot get version!")
                        sys.exit(5)

                    else:
                        print("New SSF Version: " + version.replace('\n', ''))
                        print("New SSF Codename: " + codename.replace('\n', ''))
                        print("SSF Update Type: " + vtype.replace('\n', ''))
                        print("SFF Update Edition: " + edition.replace('\n', ''))

                        print("\nTesting Update " + version.replace('\n', '') + '...')
                        call(['python', '.CI_Emulator.py'])

                else:
                    print("Unknown command; Type {} --help.".format(sys.argv[0]))
                    sys.exit(1)

            else:
                print("Please change directory to the root of SSF's repository!")
                sys.exit(2)

    except IndexError:
        print("Unknown command; Type {} --help.".format(sys.argv[0]))
        sys.exit(4)

if __name__ == '__main__':
    main()
