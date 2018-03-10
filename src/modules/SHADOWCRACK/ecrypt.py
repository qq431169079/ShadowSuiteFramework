import sys, hashlib, time
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'
print '%s%s  %s' % (W, RR, W)
print '%s                            %s' % (RR, W)
print '                          %s  %s' % (RR, W)
print '    %s                                            %s' % (RR, W)
print '%s      %s%s%s[ md5|sha1|sha224|sha256|sha384|sha512 ]%s%s  %s' % (RR, W, B, O, W, RR, W)
print '%s  %s  %s                                            %s' % (RR, W, RR, W)
print '%s  %s' % (RR, W)
algorithm1 = raw_input('%s    %s%s[%s#%s%s] Algorithm:%s ' % (RR, W, B, R, W, B, O))
if algorithm1.strip() in 'md5 MD5 Md5 mD5'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.md5(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
elif algorithm1.strip() in 'sha1 SHA1 Sha1 sHa1 sHA1'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.sha1(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
elif algorithm1.strip() in 'sha224 SHA224 Sha224 sHa224 sHA224'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.sha224(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
elif algorithm1.strip() in 'sha256 SHA256 Sha256 sHa256 sHA256'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.sha256(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
elif algorithm1.strip() in 'sha384 SHA384 Sha384 sHa384 sHA384'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.sha384(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
elif algorithm1.strip() in 'sha512 SHA512 Sha512 sHa512 sHA512'.split():
    print '%s%s  %s' % (W, RR, W)
    hash = hashlib.sha512(raw_input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O))).hexdigest()
    hash = hash.upper()
    print '%s%s  %s' % (W, RR, W)
    print '%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash)
    print '%s' % W
    sys.exit()
else:
    print '\n%s%s[%s!%s%s] %sWrong Input...%s' % (W, B, R, W, B, R, W)
    time.sleep(2)
    sys.exit()
