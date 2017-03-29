#Embedded file name: mysql_user_enum.py
import socket
import sys
if 0:
    i11iIiiIii

def assign(service, arg = None):
    if service == '''mysql''':
        return (True, arg)
        if 0:
            O0 / iIii1I11I1II1 % OoooooooOO - i1IIi


def o0OO00(arg):
    oo, i1iII1IiiIiI1, iIiiiI1IiI1I1, o0OoOoOO00 = arg
    I11i = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        I11i.settimeout(8)
        I11i.connect((oo, i1iII1IiiIiI1))
        O0O = I11i.recv(1024)
        Oo = decode('\x8c\x97\xdcT.\xbb\x04\x96') + iIiiiI1IiI1I1 + decode('\x8c\xd5\x81\x9eh\xedP\xc3\xd0\xdb')
        I11i.send(chr(len(Oo) - 3) + Oo)
        O0O = I11i.recv(1024)
        I11i.close()
        if O0O.find(decode('\xfa\xf5\xa4\xabJ\xcba\xef\xf8')) != -1 and O0O[7:13] != decode('\xc8\xfb\xb4\xb5@\xd5'):
            o0OoOoOO00.append(iIiiiI1IiI1I1)
    except:
        pass

    I11i.close()
    if 0:
        o0 * i1 * ii1IiI1i % OOooOOo / I11iIi1I / IiiIII111iI


def audit(arg):
    oo, i1iII1IiiIiI1 = arg
    IiII = []
    iI1Ii11111iIi = threadpool.ThreadPool(10)
    i1i1II = util.load_password_dict(oo, decode('\xfc\xf3\xaa\xa5F\xdfj\xe2\xb9\xae>\x1ckH\xf2\xfdV\xc4b$\xfe\xab\xa2'), None)
    for O0oo0OO0 in i1i1II:
        if O0oo0OO0[0] not in IiII:
            IiII.append(O0oo0OO0[0])

    o0OoOoOO00 = []
    for iIiiiI1IiI1I1 in IiII:
        iI1Ii11111iIi.push(o0OO00, (oo,
         i1iII1IiiIiI1,
         iIiiiI1IiI1I1,
         o0OoOoOO00))

    iI1Ii11111iIi.wait()
    if o0OoOoOO00:
        security_note(decode('\xbd').join(o0OoOoOO00))
        if 0:
            oooO0oo0oOOOO - ooO0oo0oO0 - i111I * II1Ii1iI1i


if __name__ == '__main__':
    from dummy import *
    from dummy import _G
    import threadpool
    audit(assign('''mysql''', (decode('\xa6\xbd\xfe\xf8\x08\x8d=\xbc\xb6\xe1`X+'), 3306))[1])

#KEY---8c97d8c12ebb049684db59720d39ad8b38b0081d8cc8d022bd7768ab0bc7c699---