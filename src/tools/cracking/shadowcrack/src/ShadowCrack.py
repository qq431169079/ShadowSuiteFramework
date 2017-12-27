#!/usr/bin/python
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

print ("\n\n")
os.system("figlet ShadowCrack") #Prints the title NOTE: This needs the package figlet!
os.system("figlet -mini HASHING TOOL")
print ("\nCopyright (C) 2017 Shadow Team\n")
print ("\n\n")
# Asks if encrypt or decrypt.
encryptordecrypt = raw_input("\n(E) Encrypt a String        (C) Crack a hash\n\nInput: ")

if encryptordecrypt == 'e' or encryptordecrypt == 'E':
  import ecrypt
   
elif encryptordecrypt == 'c' or encryptordecrypt == 'C':
    print ("%s%s  %s" % (W, RR, W))
    print ("%s                            %s" % (RR, W))
    print ("                          %s  %s" % (RR, W))
    print ("    %s                                            %s" % (RR, W))
    print ("%s      %s%s%s[ md5|sha1|sha224|sha256|sha384|sha512 ]%s%s  %s" % (RR, W, B, O, W, RR, W))
    print ("%s  %s  %s                                            %s" % (RR, W, RR, W))
    print ("%s  %s" % (RR, W))
    algorithm2 = raw_input("%s    %s%s[%s#%s%s] Algorithm:%s " % (RR, W, B, R, W, B, O))
  
else:
	print ("\n%s%s[%s!%s%s] %sWrong Input... Please check your input...%s" % (W, B, R, W, B, R, W))
	time.sleep(2)
	restart_ShadowCrack()
	
if algorithm2 == "md5" or algorithm2 == "MD5" or algorithm2 == "Md5" or algorithm2 == "mD5":
  import md5
  
if algorithm2 == "sha1" or algorithm2 == "SHA1" or algorithm2 == "Sha1" or algorithm2 == "sHA1":
  import sha1
  
if algorithm2 == "sha224" or algorithm2 == "SHA224" or algorithm2 == "Sha224" or algorithm2 == "sHA224":
  import sha224
  
if algorithm2 == "sha256" or algorithm2 == "SHA256" or algorithm2 == "Sha256" or algorithm2 == "sHA256":
  import sha256
  
if algorithm2 == "sha384" or algorithm2 == "SHA384" or algorithm2 == "Sha384" or algorithm2 == "sHA384":
  import sha384

if algorithm2 == "sha512" or algorithm2 == "SHA512" or algorithm2 == "Sha512" or algorithm2 == "sHA512":
  import sha512
     
else:
    # If user enters an invalid password, this will show up.
	print ("\n%s%s[%s!%s%s] %sWrong Input... Please check your input...%s" % (W, B, R, W, B, R, W))
	time.sleep(2)
	sys.exit()
