import socket
import sys
import os

def current():
    # return the current hostname
    try:
        hostname = socket.gethostname()

    except Exception as error:
        return error

    else:
        return hostname

def byname(domain):
    # map a hostname to its IP number
    try:
        ip = socket.gethostbyname(domain)
        return ip
 
    except Exception as error:
        return error

    else:
        return ip

def byaddr(ip):
    # map an IP number or hostname to DNS info
    try:
        host = socket.gethostbyaddr(ip)

    except Exception as error:
        return error

    else:
        return host
