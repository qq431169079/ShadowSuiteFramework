#!/data/data/com.termux/files/usr/bin/bash

import ShadowSuite

loop = True

print("[T] Shadow Suite as Module Testing Script\n")
print("[i] This script will run Shadow Suite as module...\n")
while loop == True:
    print("Please type \'test\' to begin...")
    entered = input(" >>> ")
    if entered == "run":
        ShadowSuite()
    else:
        print("[E] ERROR!")
