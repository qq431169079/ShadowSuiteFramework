import os, sys, hashlib
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'
print '%s%s  %s' % (W, RR, W)
hash01 = raw_input('%s    %s%s[%s#%s%s] Hash:%s ' % (RR, W, B, R, W, B, O))
print '%s%s  %s' % (W, RR, W)
wordlist = raw_input('%s    %s%s[%s#%s%s] Wordlist:%s ' % (RR, W, B, R, W, B, O))
try:
    words = open(wordlist, 'r')
except(IOError):
    print 'Error: Check your wordlist path\n'
    sys.exit(1)

words = words.readlines()
for word in words:
    hash = hashlib.sha1(word[:-1])
    value = hash.hexdigest()
    if hash01 == value:
        print '%s%s  %s' % (W, RR, W)
        print '%s%s    %s%s[%s#%s%s] Word:%s %s' % (W, RR, W, B, R, W, B, O, word)
        print '%s' % (W)
        sys.exit()