import sys, hashlib, time
W = '\x1b[0m'
R = '\x1b[31m'
G = '\x1b[32m'
O = '\x1b[33m'
B = '\x1b[1m'
RR = '\x1b[3m'
print('%s%s  %s' % (W, RR, W))
print('%s                            %s' % (RR, W))
print('                          %s  %s' % (RR, W))
print('    %s                                            %s' % (RR, W))
print('%s      %s%s%s[01] md5\n[02] sha1\n[03] sha224\n[04] sha256\n[05] sha384\n[06] sha512 %s%s  %s' % (RR, W, B, O, W, RR, W))
print('%s  %s  %s                                            %s' % (RR, W, RR, W))
print('%s  %s' % (RR, W))
algorithm1 = int(input('%s    %s%s[%s#%s%s] Algorithm:%s ' % (RR, W, B, R, W, B, O)))
if algorithm1 == 1:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.md5(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
elif algorithm1 == 2:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.sha1(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
elif algorithm1 == 3:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.sha224(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
elif algorithm1 == 4:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.sha256(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
elif algorithm1 == 5:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.sha384(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
elif algorithm1 == 6:
    print('%s%s  %s' % (W, RR, W))
    hash = input('%s    %s%s[%s#%s%s] String:%s ' % (RR, W, B, R, W, B, O)).encode()
    hash = hashlib.sha512(hash).hexdigest()
    hash = hash.upper()
    print('%s%s  %s' % (W, RR, W))
    print('%s    %s%s[%s+%s%s] Hash: %s%s' % (RR, W, B, R, W, B, O, hash))
    print('%s' % W)
    sys.exit()
else:
    print('\n%s%s[%s!%s%s] %sWrong Input...%s' % (W, B, R, W, B, R, W))
    time.sleep(2)
    sys.exit()
