#Embedded file name: backup_file.py
import re
import urlparse
import time
if 0:
    i11iIiiIii

def assign(service, arg):
    if service != '''www''':
        return
    OO0o = urlparse.urlparse(arg)
    if OO0o.path and OO0o.path != '''/''' and OO0o.path.find('''.htm''') == -1 and OO0o.path.split('''/''')[-1].find(decode('\xd6')) != -1:
        return (True, '''%s://%s%s''' % (OO0o.scheme, OO0o.netloc, OO0o.path))
        if 0:
            Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o


def ii11i(head):
    OO0o = re.search(decode('\xbb_D\xba\x84m\x05\x80\x0c\xf8\xe9Y\xd6\x99w\x1e\xe2\xd1\x11\x05\x92\xc4\xc6'), head, re.I)
    if OO0o:
        return OO0o.group(1).lower().strip()
        if 0:
            iIiI * iIiiiI1IiI1I1 * o0OoOoOO00


def I11i(backup_url, normal_mime):
    O0O = False
    Oo, I1ii11iIi11i, I1IiI, o0OOO, o0OOO = curl.curl(backup_url)
    if ii11i(I1ii11iIi11i) == normal_mime:
        return False
    elif Oo == 404:
        return False
    else:
        if Oo == 200:
            O0O = False
            iIiiiI = util.get_fuzzpage(backup_url)
            Iii1ii1II11i, iI111iI, IiII, o0OOO, o0OOO = curl.curl(iIiiiI)
            if Iii1ii1II11i == Oo:
                if util.str_ratio(I1IiI, IiII) < 0.9:
                    O0O = True
            else:
                O0O = True
        return O0O
    if 0:
        Ii11111i * iiI1i1


def audit(arg):
    i1I1ii1II1iII = ['''.bak''',
     '''.BAK''',
     '''.tmp''',
     decode('\x86'),
     '''.back''',
     '''.backup''',
     '''.old''',
     '''.swp''',
     '''.txt''']
    oooO0oo0oOOOO = arg
    Oo, I1ii11iIi11i, I1IiI, o0OOO, o0OOO = curl.curl(oooO0oo0oOOOO)
    O0oO = ii11i(I1ii11iIi11i)
    if 0:
        o00ooo0 / Oo00O0
    for ooO0oooOoO0 in i1I1ii1II1iII:
        II11i = oooO0oo0oOOOO + ooO0oooOoO0
        for i1 in range(2):
            O0O = I11i(II11i, O0oO)
            debug('''[%03d] %s''', 200 if O0O else 404, II11i)
            if O0O:
                if i1 > 0:
                    security_info(II11i)
                    return
                if 0:
                    oo % O0Oooo00
                time.sleep(5)
            else:
                break
                if 0:
                    i1IIi11111i / I11i1i11i1I % ooIiII1I1i1i1ii / oOOOo0o0O + OoOoo0 % O0Oooo00


if __name__ == '__main__':
    from dummy import *

#KEY---f8302acee10371dc21ac9029b3a35f45bcdc1b3ecfefefb25771bac202ac32ec---