#!/data/data/com.termux/files/usr/bin/bash

loop = True

print("[T] Shadow Suite as Module Testing Script\n")
print("[i] This script will run Shadow Suite as module...\n")
while loop == True:
    print("Please type \'run\' to begin...")
    entered = input(" >>> ")
    if entered == "run":
        import ShadowSuite
    else:
        print("[E] ERROR!")
