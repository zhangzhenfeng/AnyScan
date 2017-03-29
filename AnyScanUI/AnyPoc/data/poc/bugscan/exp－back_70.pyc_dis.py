#Embedded file name: url_redirect.py
import re
import urlparse
import urllib
import time
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


def iI1(action, query, k, v):
    i1I11i = []
    OoOoOO00 = decode('\x8e\xc3\x8f\x9f\xb28\xd4U\xd2\xad\x9cJ\x01=\x1e\xb0\x03\xda\x1d') + str(time.time())
    for I11i, O0O in query:
        O0O = OoOoOO00 if I11i == k else O0O
        i1I11i.append((I11i, O0O))
        if 0:
            i11ii11iIi11i.oOoO0oo0OOOo + IiiI / Iii1ii1II11i

    iI111iI = urllib.urlencode(i1I11i)
    IiII = decode('\xdb\xdf\xc2\xc9\xf7') % (action, iI111iI)
    iI1Ii11111iIi, i1i1II, O0oo0OO0, I1i1iiI1, I1i1iiI1 = curl.curl(IiII)
    if i1i1II.find(decode('\xbe\xcc\x91\x99\xeb`\x94R\x87\xf3\xc4D\x0e%\x0c\xe1G\x99\\\xd5F]3n\r\xda\x9bm')) != -1:
        return (True, decode('\xdb\xdf\xc2\xc9\xf7') % (action, iI111iI))
        if 0:
            oOOOO0o0o


def audit(arg):
    Ii1iI = arg
    Oo = urlparse.urlparse(Ii1iI)
    I1Ii11I1Ii1i = urlparse.urlunsplit((Oo.scheme,
     Oo.netloc,
     Oo.path,
     decode(''),
     decode('')))
    Oo0Ooo = urlparse.parse_qsl(Oo.query)
    if 0:
        iiI1iIiI.ooo0Oo0 * i1 - Oooo0000 * i1IIi11111i / o000o0o00o0Oo
    oo = [decode('\xb0\xee\xa7\xb8\xcd[\xa7y\xe8\x81\xf1'), decode('\xaa\xd9\x8f\x84\xcd|\x9b_\xc6\xea\xc6'), decode('\xaa\xd9\x8f\x84\xcd|\x9b_\xc6\xea\xc2')]
    for O0O0OO0O0O0, iiiii in Oo0Ooo:
        if O0O0OO0O0O0 in oo:
            continue
        debug(decode('\xa0\xfb\xad\xb5\xce%\xddE\x8c\xe7\xcb'), O0O0OO0O0O0, I1Ii11I1Ii1i)
        IiII1I1i1i1ii = iI1(I1Ii11I1Ii1i, Oo0Ooo, O0O0OO0O0O0, iiiii)
        if IiII1I1i1i1ii:
            security_info(IiII1I1i1i1ii[1])
            return
            if 0:
                OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + i1iiIII111ii + i1iIIi1


if __name__ == '__main__':
    from dummy import *

#KEY---efb1fdfd9905e92bacd3a5367c4727dc7ae722ab7f214e1434b6e25041d34190---