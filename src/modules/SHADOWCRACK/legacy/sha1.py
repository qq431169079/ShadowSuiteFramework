import os, sys, hashlib
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'
print('%s%s  %s' % (W, RR, W))
hash01 = input('%s    %s%s[%s#%s%s] Hash:%s ' % (RR, W, B, R, W, B, O))
hash01 = hash01.upper()
print('%s%s  %s' % (W, RR, W))
wordlist = input('%s    %s%s[%s#%s%s] Wordlist:%s ' % (RR, W, B, R, W, B, O))
try:
    words = open(wordlist, 'r')
except(IOError):
    print('Error: Check your wordlist path\n')
    sys.exit(1)

words = words.readlines()
print('Cracking...')
for word in words:
    word = word.strip('\n')
    hash = hashlib.sha1(word.encode())
    value = hash.hexdigest()
    value = value.upper()
    if value == hash01:
        print('%s%s  %s' % (W, RR, W))
        print('%s%s    %s%s[%s#%s%s] Word:%s %s' % (W, RR, W, B, R, W, B, O, word))
        print('%s' % (W))
        sys.exit()
    else:
        pass
