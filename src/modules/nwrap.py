#!/bin/python

def main():
    import os
    import core.error
    
    print("Nmap: Network exploration tool and security / port scanner\n\n")
    print("Target's IP Address or URL: ")
    TARGET = input("[NWRAP] > ")
    print("\n")
    print("Common Scanning Types:")
    print("[1] TCP connect scan")
    # nmap -sT [TARGET]
    print("[2] Half-open scan        [i] ROOT REQUIRED")
    # nmap -sS [TARGET]
    print("[3] ping scan")
    # nmap -sP [TARGET]
    print("[4] UDP scan              [i] ROOT REQUIRED")
    # nmap -sU [TARGET]
    print("[5] IP Protocol scan      [i] ROOT REQUIRED")
    # nmap -sO [TARGET]
    print()
    print("Ping Scanning Types:")
    print("[6] TCP SYN ping")
    # nmap -PS[PORTLIST] [TARGET]
    print("[7] TCP ACK ping")
    # nmap -PA[PORTLIST] [TARGET]
    print("[8] UDP ping              [i] ROOT REQUIRED")
    # nmap -PU[PORTLIST] [TARGET]
    print("[9] SCTP INIT ping        [i] ROOT REQUIRED")
    # nmap -PY[PORTLIST] [TARGET]
    print("[10] ARP ping")
    # nmap -PR [TARGET]
    print()
    print("Other Scan Types:")
    print("[11] List scan")
    # nmap -sL [TARGET]
    print("[12] SCTP INIT scan       [i] ROOT REQUIRED")
    # nmap -sY [TARGET]
    print("[13] TCP ACK scan         [i] ROOT REQUIRED")
    # nmap -sA [TARGET]
    print("[14] TCP Windows scan     [i] ROOT REQUIRED")
    # nmap -sW [TARGET]
    print("[15] OS scan              [i] ROOT REQUIRED\n\n")
    print("[99] Quit")
    # nmap -O [TARGET]
    print()
    SCANTYPE = input("[NWRAP] > ")
    
    if SCANTYPE == "1":
        print()
        print()
        print()
        print()
        print("TCP Connect scan")
        print()
        os.system("nmap -sT " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "2":
        print()
        print()
        print()
        print()
        print("Half-open scan")
        print()
        os.system("nmap -sS " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "3":
        print()
        print()
        print()
        print()
        print("Ping scan")
        print()
        os.system("nmap -sP " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "4":
        print()
        print()
        print()
        print()
        print("UDP scan")
        print()
        os.system("nmap -sU " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "5":
        print()
        print()
        print()
        print()
        print("IP Protocol scan")
        print()
        os.system("nmap -sO " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "6":
        print()
        print()
        print()
        print()
        print("TCP SYN ping")
        print()
        os.system("nmap -PS20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "7":
        print()
        print()
        print()
        print()
        print("TCP ACK ping")
        print()
        os.system("nmap -PA20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")
    
    elif SCANTYPE == "8":
        print()
        print()
        print()
        print()
        print("UDP ping")
        print()
        os.system("nmap -PU20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "9":
        print()
        print()
        print()
        print()
        print("SCTP INIT ping")
        print()
        os.system("nmap -PY20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "10":
        print()
        print()
        print()
        print()
        print("ARP ping")
        print()
        os.system("nmap -PR20,21,22,23,25,53,80,88,110,119,123,137,139,143,161,162,163,164,194,443,514,563,989,990,5060 " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "11":
        print()
        print()
        print()
        print()
        print("List scan")
        print()
        os.system("nmap -sL " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "12":
        print()
        print()
        print()
        print()
        print("SCTP INIT scan")
        print()
        os.system("nmap -sY " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "13":
        print()
        print()
        print()
        print()
        print("TCP ACK scan")
        print()
        os.system("nmap -sA " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "14":
        print()
        print()
        print()
        print()
        print("TCP Window scan")
        print()
        os.system("nmap -sW " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "15":
        print()
        print()
        print()
        print()
        print("OS scan")
        print()
        os.system("nmap -O " + TARGET)
        print()
        print("Scan finished!")

    elif SCANTYPE == "99":
        print()
        print()
        print()
        print()
        print("Quitting NWRAP...")

    else:
	    core.error.error0001()
