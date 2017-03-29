#Embedded file name: compressed_file.py
import urlparse
import re

def assign(service, arg):
    if service != '''www''':
        return
        if 0:
            i11iIiiIii
    OO0o = urlparse.urlparse(arg)
    Oo0Ooo = OO0o.path.split('''/''')
    O0O0OO0O0O0 = len(Oo0Ooo)
    iiiii = []
    if O0O0OO0O0O0 < 3:
        return (True, '''%s://%s/''' % (OO0o.scheme, OO0o.netloc))
    else:
        if 0:
            iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
        for iI1 in range(1, O0O0OO0O0O0 - 1):
            i1I11i = '''/'''.join(Oo0Ooo[1:iI1 + 1])
            OoOoOO00 = '''%s://%s/%s/''' % (OO0o.scheme, OO0o.netloc, i1I11i)
            if decode('\x11') not in i1I11i:
                iiiii.append(OoOoOO00)
                if 0:
                    OOOo0 / Oo - Ooo00oOo00o.I1IiI
            if iI1 == 2:
                break

        return (True, iiiii)
    if 0:
        OOooOOo / ii11ii1ii


def O00ooOO(http_code, head):
    if http_code == 200 and re.search(decode('|\xf9\\\x83d\xfbI\xa53/j\xc4M\xeb\xd1\xe9\xa8C\x0f"P\xbcZ*\xf1/\xe2\x9cr\xfcX(a\x9b8\xaa+\xbdG\x90n\x07p\xdbE\xa1\xf8\xd2\xd6:.{E\xbeO\'\xf5e'), head, re.M | re.I):
        I1iII1iiII = re.search(decode('|\xf9\\\x83d\xfbI\xa537v\xdaO\xa5\xe2\x8d\xf9:x m\xa8\x01o'), head, re.M | re.I)
        if I1iII1iiII and int(I1iII1iiII.group(1)) > 10:
            return True
    return False
    if 0:
        Ii11111i * iiI1i1


def i1I1ii1II1iII(url_dir, name):
    if 0:
        oO0o
    IIII = '''%snoexists.zip''' % url_dir
    Oo0oO0oo0oO00, i111I, II1Ii1iI1i, II1Ii1iI1i, II1Ii1iI1i = curl.curl('''-I --retry 3 ''' + IIII)
    if 0:
        o0oOoO00o
    if O00ooOO(Oo0oO0oo0oO00, i111I):
        return False
        if 0:
            O0OOo.II1Iiii1111i
    i1IIi11111i = ['''rar''',
     '''zip''',
     '''7z''',
     '''tar.gz''',
     '''tar''',
     '''bz2''',
     '''gz''']
    for o000o0o00o0Oo in i1IIi11111i:
        oo = '''%s%s.%s''' % (url_dir, name, o000o0o00o0Oo)
        Oo0oO0oo0oO00, i111I, II1Ii1iI1i, II1Ii1iI1i, II1Ii1iI1i = curl.curl('''-I --retry 3 ''' + oo)
        debug('''[%d] %s''', Oo0oO0oo0oO00, oo)
        if O00ooOO(Oo0oO0oo0oO00, i111I):
            security_warning(oo)
            return True
            if 0:
                I1I1i1 * oO0 / OOo0o0 / OOoOoo00oo - OOooOOo + Oo

    return False
    if 0:
        o0oOoO00o * oO0o * Ooo00oOo00o


def audit(arg):
    if 0:
        Oo
    OoOoOO00 = arg
    IIIiI11ii = util.get_url_host(OoOoOO00)
    if 0:
        I1I1i1 + o0oOoO00o % oOooOoO0Oo0O / i11iIiiIii
    if re.match('''^\w+://[\w\-\.]+/$''', OoOoOO00):
        iiIIi1IiIi11 = ['''wwwroot''',
         '''htdocs''',
         '''site''',
         '''www''',
         '''default''',
         '''web''']
        iiIIi1IiIi11.append(IIIiI11ii)
        iiIIi1IiIi11.append(IIIiI11ii.replace(decode('\x11'), decode('')))
        iiIIi1IiIi11.append(IIIiI11ii.replace(decode('\x11'), '''_'''))
        i1Ii = util.get_domain_root(IIIiI11ii)
        iiIIi1IiIi11.append(i1Ii)
        iiIIi1IiIi11.append(i1Ii.replace(decode('\x11'), decode('')))
        iiIIi1IiIi11.append(i1Ii.replace(decode('\x11'), '''_'''))
        if 0:
            I1I1i1 + OOoOoo00oo % OOoOoo00oo - oO0o * Ii11111i % I1I1i1
        if i1Ii != IIIiI11ii:
            OOooO0OOoo = IIIiI11ii.replace(decode('\x11') + i1Ii, decode('')).split(decode('\x11'))
            iiIIi1IiIi11 += OOooO0OOoo
            if 0:
                Ii11111i / ii11i
        iiIIi1IiIi11.append(i1Ii.split(decode('\x11'))[0])
        for IiIIIiI1I1 in set(iiIIi1IiIi11):
            if i1I1ii1II1iII(OoOoOO00, IiIIIiI1I1):
                break

    else:
        I1iII1iiII = re.match('''^(\w+://.*/)([^/]+)/''', OoOoOO00)
        if I1iII1iiII:
            if not i1I1ii1II1iII(OoOoOO00, I1iII1iiII.group(2)):
                i1I1ii1II1iII(I1iII1iiII.group(1), I1iII1iiII.group(2))
                if 0:
                    i11iIiiIii + II1Iiii1111i + OOoOoo00oo * O0OOo + Ii11111i


if __name__ == '__main__':
    from dummy import *
    oOoO = [decode('W\xe2F\x87;\xba\x12\x8ei\x0c=\x87\x1e\xe1\xee\xd8\xc6g1g\\\xe3Ki\xfac\xe0\xc7\x7f\xbc')]
    for OoOoOO00 in oOoO:
        IiiiI1II1I1 = assign('''www''', OoOoOO00)[1]
        if isinstance(IiiiI1II1I1, list):
            for ooIi11iI1i in IiiiI1II1I1:
                audit(ooIi11iI1i)

        elif IiiiI1II1I1:
            audit(IiiiI1II1I1)
            if 0:
                i11iIiiIii.o0oOoO00o / I1IiI * iIIi1iI1II111 % oO0o % ii11i
            if 0:
                ii11i - II1Iiii1111i * OOooOOo + Ii11111i + I1I1i1 + I1I1i1

#KEY---3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673---