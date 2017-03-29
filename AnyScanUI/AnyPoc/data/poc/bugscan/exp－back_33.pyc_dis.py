#Embedded file name: nginx.py
import urlparse
import re
if 0:
    i11iIiiIii

def assign(service, arg):
    if service != '''www''':
        return
    else:
        OO0o = urlparse.urlparse(arg)
        return (True, '''%s://%s/''' % (OO0o.scheme, OO0o.netloc))
    if 0:
        Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o


def ii11i(head):
    OO0o = re.search(decode(')\xd5\x93%\xa3\x90\x15A\xbdx\xbc`\xb5z\xa7z\t\xa9\x91\xdd\x9b7\x1f'), head, re.I)
    if OO0o:
        return OO0o.group(1).lower().strip()
    else:
        return decode('"\x95\xd1(\xa6\xdc\x18')
    if 0:
        iIiI * iIiiiI1IiI1I1 * o0OoOoOO00


def I11i(url):
    O0O, Oo, I1ii11iIi11i, I1IiI, I1IiI = curl.curl(url)
    if O0O != 200 or len(I1ii11iIi11i) < 0:
        return False
    else:
        o0OOO = ii11i(Oo)
        if url.endswith('''robots.txt''') and o0OOO.find('''text/plain''') == -1:
            return False
            if 0:
                ooOo + Ooo0O
        debug('''[%03d] <nginx> %s''', O0O, url)
        if 0:
            iII111i % IiII + I1Ii111 / ooOoO0o * o00O0oo
        for O0oOO0o0, i1ii1iIII in [('''/%20\0.php''', '''/%20\0.abczzz'''), ('''%00.php''', '''%00.abczzz'''), ('''/a.php''', '''/a.abczzz''')]:
            Oo0oO0oo0oO00 = url + O0oOO0o0
            i111I = url + i1ii1iIII
            II1Ii1iI1i, iiI1iIiI, OOo, I1IiI, I1IiI = curl.curl(Oo0oO0oo0oO00)
            Ii1IIii11, Oooo0000, i11, I1IiI, I1IiI = curl.curl(i111I)
            if II1Ii1iI1i == 200 and OOo in I1ii11iIi11i and OOo != i11 and ii11i(iiI1iIiI) != o0OOO:
                security_hole(Oo0oO0oo0oO00)
                if 0:
                    O00o0o0000o0o.oOo0oooo00o * I1i1i1ii - IIIII

        return True
    if 0:
        I1i1i1ii.ooOoO0o - I1Ii111 % Iii1I1 + I1Ii111


def audit(arg):
    i1iiIIiiI111 = arg
    if I11i(i1iiIIiiI111 + '''robots.txt'''):
        return
    oooOOOOO = util.get_url_host(i1iiIIiiI111)
    O0O, Oo, I1ii11iIi11i, I1IiI, I1IiI = curl.curl(i1iiIIiiI111)
    i1iiIII111ii = []
    i1iIIi1 = re.findall(decode('\\\x96\x9dm\xe2\x99_\x1e\xd1&\xb7o\xf9\x1e\x8afr\xb1\xf9\xd3\xe4\x0c^\x83^\xe0\xd3\x99\xcc\x1dj\xd8\x1d\x8c\xb3\x0b\xe4\xde\x11\x1e\x92+\xfem\xff\x14\x8ddR\xdc\xaa\xf4\x84\x15\x1f\xc3'), I1ii11iIi11i, re.I)
    if i1iIIi1:
        for I1IiI, ii11iIi1I, iI111I11I1I1 in i1iIIi1:
            ii11iIi1I = util.urljoin(i1iiIIiiI111, ii11iIi1I)
            if util.get_url_host(ii11iIi1I) != oooOOOOO:
                continue
            i1iiIII111ii.append(ii11iIi1I)

    if not i1iiIII111ii:
        for i1iIIi1 in re.finditer(decode('%\xf1\xb5q\xc4\xb3B@\xb8C\xee!\xd8\t\xe691\xda\xed\xd4'), I1ii11iIi11i, re.I):
            ii11iIi1I = util.urljoin(i1iiIIiiI111, i1iIIi1.group(1))
            if util.get_url_host(ii11iIi1I) != oooOOOOO:
                continue
            i1iiIII111ii.append(ii11iIi1I)
            if 0:
                ooOo % ii1I / o00O0oo - IiII - Iii1I1 / ooO0OO000o

    for ii11iIi1I in i1iiIII111ii:
        if I11i(ii11iIi1I):
            break
            if 0:
                OO0O0O - ii1I


if __name__ == '__main__':
    from dummy import *

#KEY---48a2a41fd1a72f6feb52c058c767b31726ef9480f5624b9733cf8088e26475b6---