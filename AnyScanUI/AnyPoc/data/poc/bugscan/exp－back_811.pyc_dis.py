#Embedded file name: www_auth_digest.py
import sys
import urlparse
import re
import hashlib
import struct
if 0:
    i11iIiiIii
if 0:
    O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = None
oo = None
if 0:
    oO0OooOoO * o0Oo

def i1IiI1I11(data):
    return hashlib.md5(data).hexdigest()
    if 0:
        ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o.oOoO0oo0OOOo + iiiiIi11i


def Ii1I(arg):
    IiiIII111iI = {decode('\x92\x8a\xd5\x93t'): decode(''),
     decode('\x88\x83\xc4\x86dB'): decode(''),
     decode('\x81\x83\xc8\x8eu'): decode(''),
     decode('\x85\x9c\xd5\x84wO'): decode(''),
     decode('\x96\x8c\xd5\x93u'): decode(''),
     decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3'): decode(''),
     decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd'): decode(''),
     decode('\x9c\x88\xc3\x83^Y\xfc\xfc\xe2V'): decode('')}
    IiII, iI1Ii11111iIi, i1i1II, O0oo0OO0, I1i1iiI1 = curl.curl(arg)
    iiIIIII1i1iI = iI1Ii11111iIi.split(decode('\xed\xf7'))
    if IiII != 401:
        return
    o0oO0 = decode('')
    for oo00 in iiIIIII1i1iI:
        if decode('\x86\x80\xcf\xd7eM\xea\xf7\xf2Zx\xf6\xd4\xc11\x86\xf0\xa3\x82\xa9\x179\xd22') in oo00.lower():
            o0oO0 = oo00
            break

    o00 = re.findall(decode('\xd9\xb1\xd5\xd7j\x7f\xad\xdd\xa4\x16-\xc4\x95\x80t\xd3\x94\xe7\xc7\xa7/x\xf7b\xcd\x94<\xf7c^\xd3\xee\xd5\xdb'), o0oO0)
    for Oo0oO0ooo in range(len(o00)):
        if o00[Oo0oO0ooo][0] == decode('\x92\x8a\xd5\x93t'):
            IiiIII111iI[decode('\x92\x8a\xd5\x93t')] = o00[Oo0oO0ooo][1].replace(decode('\xd0'), decode(''))
        elif o00[Oo0oO0ooo][0] == decode('\x81\x83\xc8\x8eu'):
            IiiIII111iI[decode('\x81\x83\xc8\x8eu')] = o00[Oo0oO0ooo][1].replace(decode('\xd0'), decode(''))
        elif o00[Oo0oO0ooo][0] == decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3'):
            IiiIII111iI[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')] = o00[Oo0oO0ooo][1].replace(decode('\xd0'), decode(''))
        elif o00[Oo0oO0ooo][0] == decode('\x9e\x83\xd3'):
            IiiIII111iI[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] = o00[Oo0oO0ooo][1].replace(decode('\xd0'), decode(''))

    if IiiIII111iI[decode('\x92\x8a\xd5\x93t')] == decode('') or IiiIII111iI[decode('\x81\x83\xc8\x8eu')] == decode(''):
        return
    else:
        return IiiIII111iI
    if 0:
        ooO00oOoo - O0OOo


def II1Iiii1111i(username, password, path, getheader):
    i1IIi11111i = decode('\xa4\xaa\xe3')
    o000o0o00o0Oo = decode('')
    ooIiII1I1i1i1ii = {}
    ooIiII1I1i1i1ii[decode('\x8e\x90\xc5\x88x_\xed\xe2')] = username
    ooIiII1I1i1i1ii[decode('\x92\x8a\xd5\x93t')] = getheader[decode('\x92\x8a\xd5\x93t')]
    ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')] = getheader[decode('\x81\x83\xc8\x8eu')]
    ooIiII1I1i1i1ii[decode('\x8e\x94\xc0')] = path
    ooIiII1I1i1i1ii[decode('\x92\x8a\xdf\x80|B\xf6\xe2')] = decode('')
    ooIiII1I1i1i1ii[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')] = getheader[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')]
    ooIiII1I1i1i1ii[decode('\x94\x87\xcc\x9bmO')] = decode('\x90\xdd\xc5\x9ai\x1c\xa6\xb1\xfe\x19b\xf7\x96\x9f/\xcc')
    ooIiII1I1i1i1ii[decode('\x85\x9c\xd5\x84wO')] = getheader[decode('\x85\x9c\xd5\x84wO')]
    ooIiII1I1i1i1ii[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] = getheader[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')]
    ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eud\xf4\xeb\xf0Zx')] = decode('\xda\xdc\x93\xc0#\x19\xba\xb0')
    ooIiII1I1i1i1ii[decode('\x9c\x88\xc3\x83^Y\xfc\xfc\xe2V')] = getheader[decode('\x9c\x88\xc3\x83^Y\xfc\xfc\xe2V')]
    if 0:
        OOo0o0 / OOoOoo00oo - iI1 + OOooO % OOoO00o
    II111iiii = ooIiII1I1i1i1ii[decode('\x8e\x90\xc5\x88x_\xed\xe2')] + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x92\x8a\xd5\x93t')] + decode('\xd3') + password
    II = i1IiI1I11(II111iiii) + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')] + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x94\x87\xcc\x9bmO')]
    if 0:
        ii11iIi1I % O0
    I111I11 = i1IIi11111i + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x8e\x94\xc0')]
    O0O00Ooo = I111I11 + decode('\xd3') + i1IiI1I11(o000o0o00o0Oo)
    if getheader[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')] == decode('\xad\xae\x87') or getheader[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')] == decode(''):
        OOoooooO = II111iiii
    else:
        OOoooooO = A1_int
    if getheader[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] == decode('\x9c\x88\xc3\x83') or getheader[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] == decode(''):
        i1iIIIiI1I = I111I11
    else:
        i1iIIIiI1I = O0O00Ooo
    OOoO000O0OO = i1IiI1I11(i1IiI1I11(OOoooooO) + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')] + decode('\xd3') + i1IiI1I11(i1iIIIiI1I))
    iiI1IiI = i1IiI1I11(i1IiI1I11(OOoooooO) + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')] + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eud\xf4\xeb\xf0Zx')] + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x94\x87\xcc\x9bmO')] + decode('\xd3') + ooIiII1I1i1i1ii[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] + decode('\xd3') + i1IiI1I11(i1iIIIiI1I))
    if getheader[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')] == decode(''):
        ooIiII1I1i1i1ii[decode('\x92\x8a\xdf\x80|B\xf6\xe2')] = OOoO000O0OO
        IIooOoOoo0O = decode('\xbc\x88\xc3\x83|Q\xfd\xfd\xe2Qo\xee\xc1\x8ec\xa2\xbe\xff\x86\xa2\x19m\xca.\x8c\xd9r\xbb+y\xc9\x91\xcc\x90\x99\xd3!Q\xec\xf2\xf7V=\xbb\x8c\xcbk\xc3\xfb\xfa\x8f\xb5\x079\x8bh\xcc\xdd#\xee~{\x94\xdc\xcf\xd6\x85\x8c)\n\xb8\xf2\xf7_w\xf9\xdd\xd7"\x87\xec\xb7\x9c\xfdK\'\xc8.\x9a\xcer\xb1*:\xd6\x8d\x96\xd6\x80\xc2gF\xfa\xa1\xb2M\x1f\x9a') % (ooIiII1I1i1i1ii[decode('\x8e\x90\xc5\x88x_\xed\xe2')],
         ooIiII1I1i1i1ii[decode('\x92\x8a\xd5\x93t')],
         ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')],
         ooIiII1I1i1i1ii[decode('\x8e\x94\xc0')],
         ooIiII1I1i1i1ii[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')],
         ooIiII1I1i1i1ii[decode('\x92\x8a\xdf\x80|B\xf6\xe2')],
         ooIiII1I1i1i1ii[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')])
    else:
        ooIiII1I1i1i1ii[decode('\x92\x8a\xdf\x80|B\xf6\xe2')] = iiI1IiI
        IIooOoOoo0O = decode('\xbc\x88\xc3\x83|Q\xfd\xfd\xe2Qo\xee\xc1\x8ec\xa2\xbe\xff\x86\xa2\x19m\xca.\x8c\xd9r\xbb+y\xc9\x91\xcc\x90\x99\xd3!Q\xec\xf2\xf7V=\xbb\x8c\xcbk\xc3\xfb\xfa\x8f\xb5\x079\x8bh\xcc\xdd#\xee~{\x94\xdc\xcf\xd6\x85\x8c)\n\xb8\xf2\xf7_w\xf9\xdd\xd7"\x87\xec\xb7\x9c\xfdK\'\xc8.\x9a\xcer\xb1*:\xd6\x8d\x96\xd6\x80\xc2gF\xfa\xa1\xb2M;\xb3\xc1\xc9t\xc6\xb5\xb2\xd2\xa0\x120\xc5,\x8c\x84#\xeb0%\xeb\xb0') % (ooIiII1I1i1i1ii[decode('\x8e\x90\xc5\x88x_\xed\xe2')],
         ooIiII1I1i1i1ii[decode('\x92\x8a\xd5\x93t')],
         ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eu')],
         ooIiII1I1i1i1ii[decode('\x8e\x94\xc0')],
         ooIiII1I1i1i1ii[decode('\x9c\x8f\xcd\x9fk^\xea\xf7\xf3')],
         ooIiII1I1i1i1ii[decode('\x92\x8a\xdf\x80|B\xf6\xe2')],
         ooIiII1I1i1i1ii[decode('\x9e\x83\xd3\xbd|Y\xea\xf3\xfbZd')],
         ooIiII1I1i1i1ii[decode('\x81\x83\xc8\x8eud\xf4\xeb\xf0Zx')],
         ooIiII1I1i1i1ii[decode('\x94\x87\xcc\x9bmO')])
    return IIooOoOoo0O
    if 0:
        O0 / oOoO0oo0OOOo.o0Oo * OOoOoo00oo - O0OOo
    if 0:
        i11iIiiIii / iIii1I11I1II1.iiiiIi11i % O0OOo / OoooooooOO % ooO00oOoo


def o0ooo00O0o0(auth, arg):
    auth = auth.replace(decode('\xd0'), decode('\xab\xd6'))
    IiII, iI1Ii11111iIi, i1i1II, O0oo0OO0, I1i1iiI1 = curl.curl(decode('\xcd\xbf\x91\xca5U\xb0\xb6\xb2M') % (auth, arg))
    if IiII < 400 and IiII >= 200:
        return True
    else:
        return False
    if 0:
        OOoOoo00oo
    if 0:
        ii11iIi1I.o0Oo % ooOO00oOo + oOoO0oo0OOOo
    if 0:
        iIii1I11I1II1 % ooO00oOoo * OOo0o0 % OOo0o0 + oO0OooOoO * iI1


def o0o00o0(args):
    global oo
    global o0OO00
    iIi1ii1I1, o0, I11II1i, IIIII, ooooooO0oo = args
    try:
        IiiIII111iI = Ii1I(o0)
        IIooOoOoo0O = II1Iiii1111i(I11II1i, IIIII, ooooooO0oo, IiiIII111iI)
        if o0OO00 == decode('') and o0ooo00O0o0(IIooOoOoo0O, o0):
            o0OO00 = I11II1i
            oo = IIIII
            if 0:
                oOoO0oo0OOOo * iIii1I11I1II1 / i1IIi / i11iIiiIii / oOoO0oo0OOOo
            iIi1ii1I1.stop()
    except Exception as I1i1I1II:
        if 0:
            OOoO00o.Ooo00oOo00o
        if 0:
            ooO00oOoo.iIii1I11I1II1.iiiiIi11i


def assign(service, arg):
    if service == '''www-auth-digest''':
        return (True, arg)
        if 0:
            OOoOoo00oo.OOoOoo00oo - oOoO0oo0OOOo / oOo0O0Ooo + ii11iIi1I * o0Oo
        if 0:
            OOoO00o % i1IIi / OoooooooOO - OoooooooOO


def audit(arg):
    if not Ii1I(arg):
        return
    iIi1ii1I1 = threadpool.ThreadPool(10)
    iIii11I = urlparse.urlparse(arg)
    OOO0OOO00oo = iIii11I.hostname
    ooooooO0oo = iIii11I.path
    Iii111II = util.load_password_dict(OOO0OOO00oo, decode('\x88\x9a\xc3\x86i_\xf6\xe2\xbbBx\xe1\xda\xfa5\x9c\xaf\xe9\xcb\xbe\x08?'), decode('\x88\x9a\xc3\x86i_\xf6\xe2\xbbBx\xe1\xda\xfa!\x96\xb5\xed\xcb\xbe\x08?'))
    for I11II1i, IIIII in Iii111II:
        iIi1ii1I1.push(o0o00o0, (iIi1ii1I1,
         arg,
         I11II1i,
         IIIII,
         ooooooO0oo))

    iIi1ii1I1.wait()
    if o0OO00 != None:
        security_hole(decode('\xcc\x90\x91\x83sI\xfa\xb6\xe4Gd\xfd\xc6\xd8)\x82\xfb\xe6\x9c\xec_#\x81t\x96') % (arg, o0OO00, oo))
        if 0:
            oOo0O0Ooo
        if 0:
            ii11iIi1I.iI1
        if 0:
            O0OOo * i11iIiiIii / Ooo00oOo00o % OOoO00o - iiiiIi11i / ooO00oOoo
        if 0:
            o0Oo


if __name__ == '__main__':
    from dummy import *
    if 0:
        o0Oo * oO0OooOoO % iI1 * Ooo00oOo00o - o0Oo

#KEY---f8feb1e2013b989686230a93b8a543f2db83f2cc6b4dbc40f8b30bdf5e0dfeb9---