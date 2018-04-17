#!/usr/bin/python2
import os, sys, hashlib, time

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[1m'  # bold
RR = '\033[3m'  # greencolor

# Restart ####################
def restart_ShadowCrack():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

print("\n\n")
print(" ____  _               _                ____                _")
print("/ ___|| |__   __ _  __| | _____      __/ ___|_ __ __ _  ___| | __")
print("\\___ \\| '_ \\ / _` |/ _` |/ _ \\ \\ /\\ / / |   | '__/ _` |/ __| |/ /")
print(" ___) | | | | (_| | (_| | (_) \\ V  V /| |___| | | (_| | (__|   <")
print("|____/|_| |_|\\__,_|\\__,_|\\___/ \\_/\\_/  \\____|_|  \\__,_|\\___|_|\\_\\")
print ("")
print("Hashing Tool and Hash Cracker")
print ("\n\nCopyright (C) 2018 Shadow Team\n")
print ("\n\n")
# Asks if encrypt or decrypt.
encryptordecrypt = input("\n[E] Encrypt a String\n[C] Crack a hash\n[Q] Quit\n\nInput: ")

if encryptordecrypt == 'e' or encryptordecrypt == 'E':
  import ecrypt
   
elif encryptordecrypt == 'c' or encryptordecrypt == 'C':
    print(("%s%s  %s" % (W, RR, W)))
    print(("%s                            %s" % (RR, W)))
    print(("                          %s  %s" % (RR, W)))
    print(("    %s                                            %s" % (RR, W)))
    print(("%s      %s%s%s[ md5|sha1|sha224|sha256|sha384|sha512 ]%s%s  %s" % (RR, W, B, O, W, RR, W)))
    print(("%s  %s  %s                                            %s" % (RR, W, RR, W)))
    print(("%s  %s" % (RR, W)))
    algorithm2 = input("%s    %s%s[%s#%s%s] Algorithm:%s " % (RR, W, B, R, W, B, O))
    algorithm2 = algorithm2.upper()

elif encryptordecrypt == 'q' or encryptordecrypt == 'Q':
    print ("Quitting...")
    sys.exit(0)
  
else:
	print(("\n%s%s[%s!%s%s] %sWrong Input... Please check your input...%s" % (W, B, R, W, B, R, W)))
	time.sleep(2)
	restart_ShadowCrack()
	
if algorithm2 == "MD5":
  import md5
  
elif algorithm2 == "SHA1":
  import sha1
  
elif algorithm2 == "SHA224":
  import sha224
  
elif algorithm2 == "SHA256":
  import sha256
  
elif algorithm2 == "SHA384":
  import sha384

elif algorithm2 == "SHA512":
  import sha512
     
else:
    # If user enters an invalid password, this will show up.
	print(("\n%s%s[%s!%s%s] %sWrong Input... Please check your input...%s" % (W, B, R, W, B, R, W)))
	time.sleep(2)
	sys.exit()
