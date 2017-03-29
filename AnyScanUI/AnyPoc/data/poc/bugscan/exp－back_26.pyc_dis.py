#Embedded file name: php_cgi.py
import urlparse
if 0:
    i11iIiiIii

def assign(service, arg):
    if service != '''www''':
        return
    else:
        OO0o = urlparse.urlparse(arg)
        if OO0o.path == decode('') or OO0o.path[-1] != decode('\x94'):
            Oo0Ooo = OO0o.path
            O0O0OO0O0O0 = '''php-cgi-type''' + OO0o.path.split(decode('\x95'))[-1]
        else:
            Oo0Ooo = decode('\x94')
            O0O0OO0O0O0 = '''php-cgi-index'''
        return (True, '''%s://%s%s''' % (OO0o.scheme, OO0o.netloc, Oo0Ooo), O0O0OO0O0O0)
    if 0:
        iiI / ii1I
    if 0:
        iII111iiiii11 % I1IiiI


def audit(arg):
    IIi1IiiiI1Ii = arg
    I11i11Ii, oO00oOo, OOOo0, Oooo000o, Oooo000o = curl.curl(IIi1IiiiI1Ii)
    IiIi11iIIi1Ii = IIi1IiiiI1Ii + '''?-s'''
    Oo0O, IiI, ooOo, Oooo000o, Oooo000o = curl.curl(IiIi11iIIi1Ii)
    debug('''[%03d] %s''', Oo0O, IiIi11iIIi1Ii)
    if I11i11Ii == Oo0O and OOOo0.find('''<code>''') == -1 and OOOo0.find('''</code>''') == -1:
        if Oo0O == 200 and ooOo.find('''<code>''') != -1 and ooOo.find('''</code>''') != -1 and ooOo.find(decode('\x9d!\xf3\x06\xc5')) != -1:
            security_hole(IiIi11iIIi1Ii)
            if 0:
                Ii1I.OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO


if __name__ == '__main__':
    from dummy import *

#KEY---bb4d873dfab45ce19dbb43ea954ddf1248a2a41fd1a72f6feb52c058c767b317---