#Embedded file name: www_form.py
if __name__ == '__main__':
    from dummy import *
import urllib
import urlparse
import difflib
if 0:
    i11iIiiIii

def assign(service, arg):
    if service != '''www-form''':
        return None
    else:
        OO0o = 0
        Oo0Ooo = 0
        for input in arg['''inputs''']:
            if input['''type'''] == '''text''':
                OO0o += 1
            if input['''type'''] == '''password''':
                Oo0Ooo += 1
                if 0:
                    OOO0O0O0ooooo % IIii1I.II1 - O00ooooo00

        if OO0o <= 1 and Oo0Ooo == 1:
            return (True, arg)
            if 0:
                ooOoO + iIiiiI1IiI1I1 * IIiIiII11i * o0oOOo0O0Ooo
        return None
    if 0:
        o0 * i1 * ii1IiI1i % OOooOOo / I11i / Ii1I


def IiiIII111iI(a, b):
    return util.str_ratio(a, b)
    if 0:
        iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - iIiiiI1IiI1I1


def o00ooo0(a, b, threshold = 0.98):
    if len(a) == len(b):
        return True
    else:
        Oo00O0 = IiiIII111iI(a, b)
        return Oo00O0 > threshold
    if 0:
        O00oOoOoO0o0O


def IiiiIiI1iIiI1(ref, action, method, inputs, username, password):
    curl.reset()
    ooo0Oo0 = []
    for input in inputs:
        try:
            if 0:
                OOO0O0O0ooooo.Oo0ooO0oo0oO * i1
            input[decode('n;p\xc14')] = input[decode('n;p\xc14')].encode(decode('b-y\x82c'), decode('q#x\xca*\xc0'))
        except:
            input[decode('n;p\xc14')] = repr(input[decode('n;p\xc14')])
            if 0:
                IIii1I.O0oo0OO0 / O0oo0OO0 % O0oo0OO0

        if input['''type'''] == '''text''':
            ooo0Oo0.append((input[decode('m;t\xc3')], username))
        elif input['''type'''] == '''password''':
            ooo0Oo0.append((input[decode('m;t\xc3')], password))
        else:
            ooo0Oo0.append((input[decode('m;t\xc3')], input[decode('n;p\xc14')]))
            if 0:
                iii1I1I.O0oo0OO0

    I11 = urllib.urlencode(ooo0Oo0)
    if 0:
        i11iIiiIii * iIiiiI1IiI1I1 % O00oOoOoO0o0O * O00oOoOoO0o0O * ooOoO
    if method.lower() == decode('h+s'):
        o0o0Oo0oooo0 = urlparse.urlparse(action)
        oO0O0o0o0 = action + (decode(',') if o0o0Oo0oooo0.query else decode('+')) + I11
    else:
        oO0O0o0o0 = decode('!/!\x9ft\xdaLq\xf8m') % (I11, action)
        if 0:
            o0oOOo0O0Ooo
    oOOOo0o0O, OOoOoo00oo, iiI11, OOooO, OOooO = curl.curl(decode('!\x0e!\x82u\xde\x10#\xa6d\x9b\x80\xbdc\x8a\x11\xcb\xb1\xc4@3\xb5\xc7') % (ref, oO0O0o0o0))
    return util.html2text(iiI11, OOoOoo00oo)
    if 0:
        o0oOOo0O0Ooo + o0 / iii1I1I * II1


def II111iiii(a, b):
    II = difflib.SequenceMatcher()
    II.set_seqs(a, b)
    oOoOo00oOo = [0, 0, 0]
    for Oo, o00O00O0O0O, OooO0OO, iiiIi, IiIIIiI1I1 in II.get_opcodes():
        if Oo != decode('`9w\xd31') and OooO0OO - o00O00O0O0O > oOoOo00oOo[0]:
            oOoOo00oOo = [OooO0OO - o00O00O0O0O, o00O00O0O0O, OooO0OO]

    return a[oOoOo00oOo[1]:oOoOo00oOo[2]]
    if 0:
        i11iIiiIii + iii1I1I + I1i1iI1i * Ii1I + i1


def oOoO(s):
    oOo = decode('')
    oOoOoO = [(ord(decode('p')), ord(decode('\x7f'))), (ord(decode('P')), ord(decode('_'))), (ord(decode('6')), ord(decode('3')))]
    for ii1I in s:
        OooO0 = ord(ii1I)
        for II11iiii1Ii, OO0oOoo in oOoOoO:
            if OooO0 >= II11iiii1Ii and OooO0 <= OO0oOoo:
                ii1I = chr(OooO0 + 1) if OooO0 < OO0oOoo else chr(II11iiii1Ii)
                break

        oOo += ii1I

    return oOo
    if 0:
        Ii1I + I11i.IIii1I - O0oo0OO0 % IIii1I - I1i1iI1i


def audit(arg):
    oOOO00o = arg[decode('p3s\xd2=\xcd')]
    O0O00o0OOO0 = arg['''inputs''']
    Ii1iIIIi1ii = arg[decode('~+y')]
    o0oo0o0O00OO = arg[decode('a+s\xd6=\xc4')]
    if 0:
        O00ooooo00
    oOOO0o0o = True
    iiI1 = True
    for input in arg['''inputs''']:
        if input['''type'''] == '''text''':
            iiI1 = False
        if input['''type'''] == '''password''':
            oOOO0o0o = False
            if 0:
                Ii1I + I1i1iI1i

    o0o0Oo0oooo0 = urlparse.urlparse(Ii1iIIIi1ii)
    ooo = o0o0Oo0oooo0.hostname
    if 0:
        i1
    if 0:
        I11i - O0oo0OO0.O0oo0OO0 + o0 - II1 + OOO0O0O0ooooo
    OOooO, OOooO, OOooO, OOooO, OOooO = curl.curl(Ii1iIIIi1ii)
    if 0:
        o0oOOo0O0Ooo % OOooOOo.OOO0O0O0ooooo
    if iiI1:
        I1i1I = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode(''), decode('l;l\xc3"\xd0\n?\xb2~\xd1\xde'))
        oOO00oOO = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode(''), decode('l;l\xc3"\xd0\n?\xa8\x7f\xdf\xcb\xe4'))
    elif oOOO0o0o:
        I1i1I = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode('l;l\xc36\xda\x10;\xb5g\xce\xda'), decode(''))
        oOO00oOO = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode('l;l\xc36\xda\x10;\xa8\x7f\xdf\xcb\xe4'), decode(''))
    else:
        I1i1I = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode('l;l\xc36\xda\x10;\xb5g\xce\xda'), decode('l;l\xc3"\xd0\n?\xb2~\xd1\xde'))
        oOO00oOO = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, decode('l;l\xc36\xda\x10;\xa8\x7f\xdf\xcb\xe4'), decode('l;l\xc3"\xd0\n?\xa8\x7f\xdf\xcb\xe4'))
        if 0:
            O00ooooo00 / II1 - OOO0O0O0ooooo / o0.ooOoO - O00ooooo00
    if not o00ooo0(I1i1I, oOO00oOO):
        return
        if 0:
            I11i + iii1I1I * I11i - o0oOOo0O0Ooo * i1
    Oooo0Ooo000 = I1i1I
    if 0:
        i11iIiiIii.iIiiiI1IiI1I1 + ooOoO
    II111ii1II1i = util.load_password_dict(ooo, decode('d;s\xd3(\xd0\n%\xf1{\xc6\xc4\xe8\t\x88_\x97\xef\x93\x1ap\xf3'), decode('d;s\xd3(\xd0\n%\xf1{\xc6\xc4\xe8\t\x9cU\x8d\xeb\x93\x1ap\xf3'), mix=False)
    if 0:
        OOO0O0O0ooooo + iIiiiI1IiI1I1 + O0oo0OO0 % iIiiiI1IiI1I1
    filter = []
    for o0OOoo0OO0OOO in II111ii1II1i:
        iI1iI1I1i1I, iIi11Ii1 = o0OOoo0OO0OOO
        if iIi11Ii1 in filter or not oOOO0o0o and not iIi11Ii1:
            continue
        filter.append(iIi11Ii1)
        if iiI1:
            debug(decode('[}#\x95\x17\x94We\xa28\x9b\x9a\xf3'), iIi11Ii1, oOOO00o)
        else:
            debug(decode('[}#\x95\x17\x94We\xa2(\x8f\xc0\xa6v\xca_'), iI1iI1I1i1I, iIi11Ii1, oOOO00o)
        Ii11iII1 = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, iI1iI1I1i1I, iIi11Ii1)
        if 0:
            ooOoO * o0oOOo0O0Ooo % i1 * ooOoO % ii1IiI1i / I1i1iI1i
        if o00ooo0(Ii11iII1, Oooo0Ooo000):
            continue
            if 0:
                i1
            if 0:
                o0 - II1 / ii1IiI1i % O00ooooo00
            if 0:
                Ii1I
            if 0:
                I11i + I1i1iI1i % i11iIiiIii + ii1IiI1i - O0oo0OO0
        for oO0OOoO0 in range(2):
            OOooO, OOooO, OOooO, OOooO, OOooO = curl.curl(Ii1iIIIi1ii)
            I111Ii111 = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, iI1iI1I1i1I, iIi11Ii1 + oOoO(iIi11Ii1))
            OOooO, OOooO, OOooO, OOooO, OOooO = curl.curl(Ii1iIIIi1ii)
            i111IiI1I = IiiiIiI1iIiI1(Ii1iIIIi1ii, oOOO00o, o0oo0o0O00OO, O0O00o0OOO0, iI1iI1I1i1I, iIi11Ii1)
            if o00ooo0(I111Ii111, Oooo0Ooo000) and not o00ooo0(i111IiI1I, Oooo0Ooo000):
                if oO0OOoO0 == 1:
                    O0 = II111iiii(i111IiI1I, I111Ii111)
                    try:
                        O0 = O0.decode(decode('b-y\x82c'), decode('q#x\xca*\xc0'))[:30].strip().encode(decode('b-y\x82c'), decode('q#x\xca*\xc0'))
                    except:
                        O0 = repr(O0)

                    iII = decode(' 1') % iI1iI1I1i1I if iiI1 else decode(' 1*\x83.') % (iI1iI1I1i1I, iIi11Ii1)
                    security_warning(decode(' 1!\x83.\x94+e\xa2T') % (iII, Ii1iIIIi1ii, O0))
            else:
                break
                if 0:
                    O0oo0OO0.OOooOOo

        break
        if 0:
            o0.ooOoO / O00oOoOoO0o0O.I11i * o0oOOo0O0Ooo.iIiiiI1IiI1I1


if __name__ == '__main__':
    Oo0oOOo = {decode('p3s\xd2=\xcd'): decode('u-s\xd5k\x89Yw\xea=\x82\x84\xb7o\xd4\x07\xc9\xbc\x80N)\xaa\x97\xd6\xecbb\x15\xea\xc3\x81\x88e+<\xde\x1f\xda\x10=\xbai\xde\xdc\xfa\t\x92P\x97\xe9\xc7'),
     '''inputs''': [{'''type''': '''text''',
                               decode('m;t\xc3'): decode('}\x00w\xd94\xde\x1d5\xb9w'),
                               decode('n;p\xc14'): decode('f+o\xc5')}, {'''type''': '''password''',
                               decode('m;t\xc3'): decode('}\x00c\xd3.\xda\x1a,\xa6s'),
                               decode('n;p\xc14'): decode('f+o\xc5')}],
     decode('~+y'): decode('u-s\xd5.\x9fYl\xea)\x91\x97\xb7|\xc0\x08\xd9\xbf\x93B1\xbb\x94'),
     decode('a+s\xd6=\xc4'): decode('v"o\xc5')}
    audit(assign('''www-form''', Oo0oOOo)[1])
    exit()

#KEY---145f01b740b46451cc03bbae9d56fe31e385aa681381a9f4ce445f7997baeff5---