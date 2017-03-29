#Embedded file name: mssql_crack.py
import struct
import sys
import random
import socket
if 0:
    i11iIiiIii
OO0o = 1433
if 0:
    Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o

class ii11i(object):

    def __init__(self):
        self.packetno = 0
        self.length = 0
        self.size = 0
        self.cli_version = 7
        self.cli_pid = 0
        self.conn_id = 0
        self.options_1 = 160
        self.options_2 = 3
        self.sqltype_flag = 0
        self.reserved_flag = 0
        self.time_zone = 0
        self.collation = 0
        self.version = 1895825409
        if 0:
            iIiI * iIiiiI1IiI1I1 * o0OoOoOO00
        self.client = decode('\x9a\x8a-\xff')
        self.username = None
        self.password = None
        self.app = decode('\x9a\x8a-\xff\x90\xf4l\x0f')
        self.server = decode('\x93\xa9\x1c\xc8\xf7')
        self.library = decode("\xb6\x91'\xfb\xc1\x94S-\xa4")
        self.locale = decode('')
        self.database = decode('\xb1\x8b<\xff\xc0\xc5')
        self.MAC = decode('\xc3\xffI\x9d\xb0\xad')
        if 0:
            OOOo0 / Oo - Ooo00oOo00o.I1IiI

    def widechar(self, ch):
        return ch + decode('\xc3')
        if 0:
            OOooOOo / ii11ii1ii

    def widestring(self, s):
        return decode('').join(map(self.widechar, s))
        if 0:
            OoOO + OoOO0ooOOoo0O + o0000oOoOoO0o * o00O0oo

    def encryptpass(self, s):
        O0oOO0o0 = 23130
        i1ii1iIII = decode('')
        for Oo0oO0oo0oO00 in s:
            Oo0oO0oo0oO00 = ord(Oo0oO0oo0oO00) ^ O0oOO0o0
            i1ii1iIII += struct.pack(decode('\x82'), Oo0oO0oo0oO00 >> 4 & 3855 | Oo0oO0oo0oO00 << 4 & 61680)

        return i1ii1iIII
        if 0:
            OOo00O0Oo0oO / o00O0oo

    def to_string(self):
        iIi = 86
        self.cli_pid = random.randint(1, 100000)
        self.length = iIi + 2 * (len(self.client) + len(self.username) + len(self.password) + len(self.app) + len(self.server) + len(self.library) + len(self.database))
        if 0:
            I1IiI / OOOo0 / OoOO0ooOOoo0O * o0OoOoOO00.ooO0OO000o
        Ii1IIii11 = struct.pack(decode('\xf0\xba\x0c\xd8\xf5\xe8g'), self.length, self.version, self.size, self.cli_version, self.cli_pid, self.conn_id)
        Ii1IIii11 += struct.pack(decode('\x8b\xb7\x01\xd5'), self.options_1, self.options_2, self.sqltype_flag, self.reserved_flag)
        Ii1IIii11 += struct.pack(decode('\xf0\xba\x0c'), self.time_zone, self.collation)
        if 0:
            OO0O0O - iIiI.OoOO * o0000oOoOoO0o * ii1I / OO0O0O
        if 0:
            I1IiI + o00O0oo.OOo00O0Oo0oO * o0000oOoOoO0o % ii11ii1ii.iIiI
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.client))
        iIi += len(self.client) * 2
        if 0:
            OoOO0ooOOoo0O * OoOO / o0000oOoOoO0o.ii1I * OoOO0ooOOoo0O
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.username))
        iIi += len(self.username) * 2
        if 0:
            ii1I % i11iIiiIii
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.password))
        iIi += len(self.password) * 2
        if 0:
            OOo00O0Oo0oO * ooO0OO000o
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.app))
        iIi += len(self.app) * 2
        if 0:
            Oo * OO0O0O * OOo00O0Oo0oO
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.server))
        iIi += len(self.server) * 2
        if 0:
            OO0O0O / ii11ii1ii + I1IiI / iIiiiI1IiI1I1 - ooO0OO000o - ii11ii1ii
        if 0:
            ii11ii1ii - OOooOOo % Iii1I1 + iIiI - OoOO0ooOOoo0O / ii11ii1ii
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), 0, 0)
        if 0:
            o0OoOoOO00 + ooO0OO000o
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.library))
        iIi += len(self.library) * 2
        if 0:
            OOooOOo * I1IiI * iIiI
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.locale))
        iIi += len(self.locale) * 2
        if 0:
            ooO0OO000o
        Ii1IIii11 += struct.pack(decode('\xf0\xbe\x08'), iIi, len(self.database))
        iIi += len(self.database) * 2
        if 0:
            OOOo0 - ii1I + o00O0oo + OoOO
        if 0:
            Oo
        Ii1IIii11 += self.MAC
        if 0:
            OoOO % ii1I % iiiii
        if 0:
            OoOO0ooOOoo0O + Iii1I1
        Ii1IIii11 += struct.pack(decode('\xf0\xbe'), iIi)
        if 0:
            OOooOOo / ii1I + i11iIiiIii - OoOO
        Ii1IIii11 += struct.pack(decode('\xf0\xbe'), 0)
        if 0:
            o0OoOoOO00
        Ii1IIii11 += struct.pack(decode('\xf0\xbe'), self.length)
        if 0:
            Iii1I1 - OoOO0ooOOoo0O / OoOO0ooOOoo0O + OOo00O0Oo0oO % OOo00O0Oo0oO - o0000oOoOoO0o
        Ii1IIii11 += struct.pack(decode('\xf0\xbe'), 0)
        if 0:
            OoOO0ooOOoo0O - o0000oOoOoO0o - OOOo0 % ii1I / I1IiI
        if 0:
            ooO0OO000o - ooO0OO000o.iIiI / Oo
        if 0:
            ii11ii1ii % Iii1I1
        Ii1IIii11 += self.widestring(self.client)
        Ii1IIii11 += self.widestring(self.username)
        Ii1IIii11 += self.encryptpass(self.password)
        Ii1IIii11 += self.widestring(self.app)
        Ii1IIii11 += self.widestring(self.server)
        Ii1IIii11 += self.widestring(self.library)
        Ii1IIii11 += self.widestring(self.locale)
        Ii1IIii11 += self.widestring(self.database)
        if 0:
            ii1I + o00O0oo + OOooOOo - o0000oOoOoO0o
        return Ii1IIii11
        if 0:
            iIiiiI1IiI1I1.o0000oOoOoO0o % OOo00O0Oo0oO

    def login(self, servername, port, username, password, timeout = 10):
        self.username = username
        self.password = password
        self.server = servername
        if 0:
            I1IiI - ii1I / i11iIiiIii + OOooOOo + o0OoOoOO00
        Ii1IIii11 = self.to_string()
        iIiII = len(Ii1IIii11) + 8
        iI = 1
        iI11iiiI1II = 0
        O0oooo0Oo00 = 0
        self.packetno += 1
        Ii11iii11I = 16
        oOo00Oo00O = struct.pack(decode('\xf8\xb7\x01\xdc\xf1\xe5jo\xb0\xa5') % len(Ii1IIii11), Ii11iii11I, iI, iIiII, iI11iiiI1II, self.packetno, O0oooo0Oo00, Ii1IIii11)
        iI11i1I1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        iI11i1I1.settimeout(timeout)
        iI11i1I1.connect((servername, port))
        iI11i1I1.send(oOo00Oo00O)
        if 0:
            OOo00O0Oo0oO % OoOO0ooOOoo0O / Oo
        ii11i1iIII = decode('')
        Ii1I = 0
        iI = 0
        Oo0o0 = False
        i1ii1iIII = decode('')
        while True:
            if len(ii11i1iIII) - Ii1I < 4:
                III1ii1iII = iI11i1I1.recv(4)
                if len(III1ii1iII) > 0:
                    ii11i1iIII += III1ii1iII
                    Oo0o0 = True
                else:
                    return (None, decode("\x9b\x9b,\xec\x90\xdf_{\xaa\xbf\xbc\x8d\xae\xad\xe5.\xb8\xcc\xeawkL\x9e4\xad\xcc\x1d\xf1\xe8\xe3|\x12\x92\xdf'\xe9\xda\xd7V1"))
                    if 0:
                        iIiI % ooO0OO000o % ooO0OO000o
            Ii11iii11I, iI, iI1 = struct.unpack_from(decode('\xf8\xb7\x01\xdc'), ii11i1iIII, Ii1I)
            Ii1I += 4
            if 0:
                ii11ii1ii + OOo00O0Oo0oO
            if Ii11iii11I != 4:
                return (None, decode('\x8d\x8b#\xe7\xc4\xc7\x021\xb4\xb9\xa6\x93\xb2\xa3\xe1.\xbf\xd1\xfc~n[\xcel\xa5\xd5\x04\xbc\xc9\xdf'))
                if 0:
                    iiiii.ii1I
            ii1I1i1I = iI1 - (len(ii11i1iIII) - Ii1I + 4)
            if ii1I1i1I > 0:
                III1ii1iII = iI11i1I1.recv(ii1I1i1I)
                if len(III1ii1iII) > 0:
                    ii11i1iIII += III1ii1iII
                else:
                    return (None, decode("\x9b\x9b,\xec\x90\xdf_{\xaa\xbf\xbc\x8d\xae\xad\xe5.\xb8\xcc\xeawkL\x9e4\xad\xcc\x1d\xf1\xe8\xe3|\x12\x92\xdf'\xe9\xda\xd7V1"))
            iI11iiiI1II, OOoo0O0, O0oooo0Oo00, III1ii1iII = struct.unpack_from(decode('\xf8\xbe%\xf1\x84\xddL') % (iI1 - 8), ii11i1iIII, Ii1I)
            i1ii1iIII += III1ii1iII
            Ii1I += 4 + (iI1 - 8)
            if iI == 1:
                break

        iI11i1I1.close()
        if 0:
            I1IiI
        if not Oo0o0:
            return (None, decode('\x95\x86$\xe0\xce\xd4\x02/\xaa\xa1\xad\x93'))
            if 0:
                Ooo00oOo00o
            if 0:
                OoOO.OoOO - Oo / o0OoOoOO00 + OOo00O0Oo0oO * iIiI
        O0ooOooooO, = struct.unpack_from(decode('\x8b'), i1ii1iIII, 0)
        if 0:
            ii11ii1ii / ii11ii1ii
        if 0:
            OoOO * OOooOOo - o0OoOoOO00 * I1IiI - o00O0oo
        if 0:
            iiiii
        if 0:
            ooO0OO000o - OOooOOo.o00O0oo % OOOo0 - Iii1I1
        if 0:
            ooO0OO000o / OOo00O0Oo0oO.OoOO0ooOOoo0O
        if 0:
            OOooOOo * i11iIiiIii / OOOo0 % o00O0oo - Ooo00oOo00o / I1IiI
        if 0:
            iIiI
        if 0:
            iIiI * ooO0OO000o % OoOO0ooOOoo0O * OOOo0 - iIiI
        if 0:
            Oo + OOooOOo * o0OoOoOO00 - iIiiiI1IiI1I1 / I1IiI % OoOO
        if 0:
            o0OoOoOO00 * OO0O0O % I1IiI * ii1I
        if 0:
            Iii1I1 - o00O0oo * OO0O0O + OoOO0ooOOoo0O
        if 0:
            ooO0OO000o - OOo00O0Oo0oO * Ooo00oOo00o / o00O0oo + Oo
        if 0:
            OoOO / o00O0oo + OoOO0ooOOoo0O - ooO0OO000o / OOo00O0Oo0oO - OOOo0
        if 0:
            Ooo00oOo00o + OOOo0 - iiiii / OOooOOo
        if O0ooOooooO == 170:
            return False
        else:
            if O0ooOooooO == 227:
                return True
                if 0:
                    i11iIiiIii % ii11ii1ii
            return (None, decode('\x91\x82$\xe9\xc9\x8dv\x11\x8a\x96\x9a'))
        if 0:
            OOooOOo + OOo00O0Oo0oO % i11iIiiIii + Ooo00oOo00o - o0000oOoOoO0o
        if 0:
            OOOo0 - o0OoOoOO00 % OOooOOo


iI1I111Ii111i = None
I11IiI1I11i1i = None

def iI1ii1Ii(arg):
    global iI1I111Ii111i
    global I11IiI1I11i1i
    oooo000, iIIIi1, iiII1i1, o00oOO0o, OOO00O = arg
    for OOoOO0oo0ooO in range(5):
        try:
            debug(decode('\x8c\xd2}\xbf\x9a\xddu{\xb5\xa5\xbe\x9f\xba\xfc\xac3\xee\xc6\xad.q~\x8a"\xec\x85\x18\xec'), OOoOO0oo0ooO, o00oOO0o, OOO00O, iIIIi1, iiII1i1)
            O0o0O00Oo0o0 = ii11i()
            if O0o0O00Oo0o0.login(iIIIi1, iiII1i1, o00oOO0o, OOO00O, 10):
                iI1I111Ii111i = o00oOO0o
                I11IiI1I11i1i = OOO00O or decode('\xf0\x8b<\xff\xc2\xca\x19')
                oooo000.stop()
            break
        except Exception as O00O0oOO00O00:
            if 0:
                o0000oOoOoO0o.Ooo00oOo00o


def assign(service, arg = None):
    if service == '''mssql''':
        return (True, arg)
        if 0:
            OoOO0ooOOoo0O.o00O0oo


def audit(arg):
    iIIIi1, iiII1i1 = arg
    try:
        O0o0O00Oo0o0 = ii11i()
        if O0o0O00Oo0o0.login(iIIIi1, iiII1i1, decode('\xba\x8b3\xe9\xda\xdbL/\xb0\xbd\xbe\x8d\xa1\xae\xf5{\xae'), decode('\xba\x8b3\xe9\xda\xdbL/\xb0\xa9\xb4\x97\xa5')) != False:
            return
    except:
        debug(sys.exc_info())
        return

    oooo000 = threadpool.ThreadPool(10)
    i1i = util.load_password_dict(iIIIi1, decode('\xb3\x9b;\xf9\xd8\xc9L/\xfd\xbe\xbe\x97\xad\xa6\xcex\xb4\xdc\xec#m]\xcc'), decode('\xb3\x9b;\xf9\xd8\xc9L/\xfd\xbe\xbe\x97\xad\xa6\xcel\xbe\xc6\xe8#m]\xcc'))
    for iiI111I1iIiI in i1i:
        oooo000.push(iI1ii1Ii, (oooo000,
         iIIIi1,
         iiII1i1,
         iiI111I1iIiI[0],
         iiI111I1iIiI[1]))

    oooo000.wait()
    if iI1I111Ii111i:
        security_hole(decode('\xf7\x91b\xa9\xc0\x8dW5\xae\xad\xa1\xd9\xa9\xb3\xff`\xa4\xd5\xecj?[\xd0l\xf3\xdfU\xe5\xd3') % (iIIIi1,
         iiII1i1,
         iI1I111Ii111i,
         I11IiI1I11i1i))
        if 0:
            iIiiiI1IiI1I1.OOo00O0Oo0oO + Iii1I1 * Oo % iIiiiI1IiI1I1 * iIiiiI1IiI1I1


if __name__ == '__main__':
    from dummy import *
    import threadpool
    audit(assign('''mssql''', (decode('\xe5\xd8c\xa4\x96\x97\x01b\xe2\xf2\xfa\xdb\xf1'), 1433))[1])

#KEY---c3ff499db0ad225bc0cbd0f9cbd7910edaa8861a1f3ebe4cc7b168d1bdad3254---