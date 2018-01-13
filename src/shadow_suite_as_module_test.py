#!/data/data/com.termux/files/usr/bin/bash

loop = True

print("[T] Shadow Suite as Module Testing Script\n")
print("[i] This script will run Shadow Suite as module...\n")
while loop == True:
    print("Please type \'run\' to begin...")
    entered = input(" >>> ")
    if entered == "run":
    	try:
    		import ShadowSuite
    	except ImportError:
    		print("[E] Import Error! Please make sure that Shadow Suite is in this directory!")
    else:
        print("[E] ERROR!")
