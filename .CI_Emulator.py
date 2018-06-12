#!/usr/bin/env python3
import os
import sys
from time import sleep as timeout
from subprocess import getstatusoutput as gso

class testEnvLinux:

    def __init__(self):
        self.job_no = 0
        self.result = [0, '']
        self.retcode = 0
        self.justContinue = False
        self.report = []
        self.rootdir = ''
        self.CG   = '\033[32m'
        self.CY   = '\033[33m'
        self.CR   = '\033[31m'
        self.CGR  = '\033[90m'
        self.END  = '\033[0m'

        self.py36 = 'test-env-3.6'
    
    def main(self):
        self.createEnvironment()
        initialize = ['echo 1', 'echo 2', 'eho 3', 'echo 4', 'echo 5']
        test = ['echo 6', 'echo 7', 'eko 8']
        finalize = ['eao 9', 'echo 10']
        stages = [initialize, test, finalize]
        iterate = 0
        for stage in stages:
            iterate += 1
            print(self.CGR, "[i] Running stage #" + str(iterate), self.END)
            for command in stage:
                if not self.justContinue:
                    self.run(command)

                else:
                    self.report.append((-1, 'Skipped by CI Emulator.'))

            self.justContinue = False
            continue

        self.get_results()

    def run(self, command):
        self.job_no += 1
        if command.startswith('cd'):
            os.chdir(command.partition('cd ')[2])

        else:
            self.result = gso(command)

        print(self.CG, "$ " + command, self.END)
        print(self.result[1])
        print()
        if self.result[0] != 0:
            print(self.CR, "Job #{} failed! Exited with code #{}".format(str(self.job_no), str(self.result[0])), self.END)
            self.retcode = 1

        else:
            self.retcode = 0

        self.report.append(self.result)
        timeout(1)
        return self.retcode

    def createEnvironment(self):
        if not os.path.exists(self.py36):
            print(self.CGR, "[i] Creating Environment...", self.END)
            gso('virtualenv --python=python3.6 ' + self.py36)

        else:
            print(self.CGR, "[i] Reusing Previous Environment...", self.END)
            print(self.CGR, "[i] Remove {} to recreate...".format(self.py36))

        os.chdir(self.py36)
        self.rootdir = os.getcwd()
        print(self.CGR, "[i] Environment set! Now starting to test...", self.END)
        timeout(1)

    def get_results(self):
        print('\n\n')
        print(self.CGR, "Results:", self.END)
        iterator = 0
        for result in self.report:
            iterator += 1
            print(self.CG, "Job #{} exited with code ".format(str(iterator)) + str(result[0]) + "!", self.END)

        print()

if __name__ == '__main__':
    if os.name == 'nt':
        pass

    else:
        testEnvLinux().main()
