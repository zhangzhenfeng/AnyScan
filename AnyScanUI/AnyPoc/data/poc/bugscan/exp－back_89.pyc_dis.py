#Embedded file name: rdp_vuln_ms12020.py
if 0:
    i11iIiiIii
import struct
import socket
if 0:
    O0 / iIii1I11I1II1 % OoooooooOO - i1IIi

def assign(service, arg = None):
    if service == '''rdp''':
        return (True, arg)
        if 0:
            II111iiii


def audit(arg):
    IiII1IiiIiI1, iIiiiI1IiI1I1 = arg
    o0OoOoOO00 = decode('\x01J\xf5bLUIF\x0e\xaeP')
    I11i = decode('\x01J\xf5\x1b\\W\xc99z\xe1@\xcf\x99\xd5}\x06(z\xfbL\x02\x07\xb8Z,)\x85\xfe\x12\xe2\x10c\tB\xf1o\\\xb1MN\x06Q\xaf\xc3\x99\xcd[\x01$z\x00f\x01\x0b\xb4v %\xa1\xf2\x1e\xe6\x18o\tN\xfdk\xab\xbdMN,\xa9X\xcfb\xcd}\xfd$z\xfbf\x01\x0b\xb4v$%\xa1\xf2\x1e\xea\xe7\x98\x05N\xfd\x7fT')
    O0O = decode('\x01J\xf5n\\W\xc9g')
    try:
        Oo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Oo.settimeout(10)
        Oo.connect((IiII1IiiIiI1, iIiiiI1IiI1I1))
        Oo.send(o0OoOoOO00)
        I1ii11iIi11i = Oo.recv(1024)
        if I1ii11iIi11i != decode('\x01J\xf5bLwIF\x04\x9cP'):
            return False
        Oo.send(I11i)
        Oo.send(O0O)
        I1ii11iIi11i = Oo.recv(1024)
        I1IiI, = struct.unpack(decode('6\x0b'), I1ii11iIi11i[9:11])
        Oo.send(O0O)
        I1ii11iIi11i = Oo.recv(1024)
        o0OOO, = struct.unpack(decode('6\x0b'), I1ii11iIi11i[9:11])
        o0OOO += 1001
        iIiiiI = struct.pack(decode('6\x0b\xb4'), I1IiI, o0OOO)
        Iii1ii1II11i = decode('\x01J\xf5~\\W\xc9e')
        iI111iI = Iii1ii1II11i + iIiiiI
        Oo.send(iI111iI)
        I1ii11iIi11i = Oo.recv(1024)
        if I1ii11iIi11i[7:9] == decode('6J'):
            if 0:
                iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
            iIiiiI = struct.pack(decode('6\x0b\xb4'), o0OOO - 1001, o0OOO)
            iI111iI = Iii1ii1II11i + iIiiiI
            Oo.send(iI111iI)
            Oo.recv(1024)
            security_warning(decode('g:\x97Di\x88}(%\x9a ') % (IiII1IiiIiI1, iIiiiI1IiI1I1))
        Oo.close()
    except:
        if 0:
            i11Ii11I1Ii1i.ooO - OOoO / ooo0Oo0 * i1 - OOooo0000ooo


if __name__ == '__main__':
    from dummy import *
    audit(assign('''rdp''', (decode("'h\xdbV~\x97w\x7f(\x89f\xf2\xbb\xe7Z"), 3389))[1])

#KEY---0d4af56f54b549460eae50cb9dc579022c7e046e050fbc72242da5f616e21867---