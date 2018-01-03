#!/bin/python

def main():
    # Colours
    D  = "\033[0m"  
    W  = "\033[01;37m"
    O  = "\033[01;33m"
    SUCESS = "\033[01;32m"
    FAIL = "\033[01;31m"
    
    import socket
    import sys
    import os
    print("DNSMap")
    print (W+"")
    domain = input("[DNSMap] Set domain: ") # www.domain.com
    
    try:
        ip = socket.gethostbyname( domain )
        print (SUCESS + "The DNS of \'" + domain + "\' is \'" + ip + "\'.")
    
    except socket.gaierror:
        print (FAIL+'Invalid Domain or no internet connection.\n')
