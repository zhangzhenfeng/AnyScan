#Embedded file name: mysql_crack.py
if 0:
    i11iIiiIii
try:
    import hashlib
    OO0o = lambda *Oo0Ooo, **O0O0OO0O0O0: hashlib.new(decode('XJP\t'), *Oo0Ooo, **O0O0OO0O0O0)
except ImportError:
    import sha
    OO0o = sha.new
    if 0:
        iiI / ii1I

import socket
import struct
import sys
if 0:
    iII111iiiii11 % I1IiiI
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
    if 0:
        iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o

I1IiI = False
if 0:
    OOooOOo / ii11ii1ii
O00ooOO = 1
I1iII1iiII = 2
iI1Ii11111iIi = 4
i1i1II = 8
O0oo0OO0 = 16
I1i1iiI1 = 32
iiIIIII1i1iI = 64
o0oO0 = 128
oo00 = 256
sys_debug_yes_no = 512
debug_key = 1024
Multiprocessing_RLock = 2048
Login_Get = 4096
oOOoo00O0O = 8192
i1111 = 32768
i11 = 65536
I11 = 131072
Oo0o0000o0o0 = O00ooOO | iI1Ii11111iIi | oOOoo00O0O | sys_debug_yes_no | i1111
oOo0oooo00o = 16777215
if 0:
    O0o * i1iIIII * I1

class O0OoOoo00o(Exception):

    def __init__(self, code, msg = None):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr(self.msg)
        if 0:
            i111IiI + iIIIiI11.iII111ii


def i1iIIi1(b):
    if isinstance(b, int):
        return b
    else:
        return struct.unpack(decode('<`'), b)[0]
    if 0:
        IiIi1Iii1I1 - O00O0O0O0


def ooO0O(i):
    return struct.pack(decode('<`'), i)
    if 0:
        iIii1.i111IiI


def iIiI1I11(bs):
    if len(bs) == 0:
        return decode('')
    else:
        oO = bs[0]
        for OO0OOooOoO0Oo in bs[1:]:
            oO += OO0OOooOoO0Oo

        return oO
    if 0:
        i1iIIII


def iiIiIiIi(data):
    if 0:
        iIIIiI11 + iIiiiI1IiI1I1 % i11iIiiIii.iIii1 - IIiIiII11i

    def O00oooo0O(data):
        if i1iIIi1(data) >= 65 and i1iIIi1(data) <= 122:
            return data
        return decode('\x0f')

    print decode('hXpo\xeb\xbdFd^f{\xbb\x03[\x85%') % len(data)
    print decode('\x7fYE_\xc9\xb9FW_FI\x80U\x04\xb2dzL') % sys._getframe(1).f_code.co_name
    print decode('\x7fYE_\xc9\xb9FW_FI\x80e\x04\xb2dzL') % sys._getframe(2).f_code.co_name
    print decode('\x7fYE_\xc9\xb9FW_FI\x80u\x04\xb2dzL') % sys._getframe(3).f_code.co_name
    print decode('\x7fYE_\xc9\xb9FW_FI\x80D\x04\xb2dzL') % sys._getframe(4).f_code.co_name
    if 0:
        iII111iiiii11 % i111IiI - iII111ii.ii1I * i11iIiiIii
    print decode('?') * 88
    II1i1Ii11Ii11 = [ data[iII11i:iII11i + 16] for iII11i in xrange(len(data)) if iII11i % 16 == 0 ]
    for O0O00o0OOO0 in II1i1Ii11Ii11:
        print decode(',').join(map(lambda Ii1iIIIi1ii: decode('=\x0c$S') % i1iIIi1(Ii1iIIIi1ii), O0O00o0OOO0)) + decode(',\x08\x00') * (16 - len(O0O00o0OOO0)) + decode(',') * 2 + decode(',').join(map(lambda Ii1iIIIi1ii: decode('=|') % O00oooo0O(Ii1iIIIi1ii), O0O00o0OOO0))
        if 0:
            i111IiI * i11iIiiIii / O00O0O0O0
        if 0:
            iIIIiI11 + i1iIIII % iIIIiI11 + I1IiiI.I1

    print decode('?') * 88
    print decode('')
    if 0:
        ii11ii1ii + i111IiI + i111IiI / iIiiiI1IiI1I1


def iiI1(password, message):
    if password == None or len(password) == 0:
        return ooO0O(0)
    else:
        if I1IiI:
            print decode('hXti\xcf\x8b"f\x18') + password
        i11Iiii = OO0o(password).digest()
        iI = OO0o(i11Iiii).digest()
        I1i1I1II = OO0o()
        I1i1I1II.update(message)
        I1i1I1II.update(iI)
        i1IiIiiI = I1i1I1II.digest()
        return I1I(i1IiIiiI, i11Iiii)
    if 0:
        OOooOOo - Ooo00oOo00o


def I1I(message1, message2):
    OOO00 = len(message1)
    i1IiIiiI = struct.pack(decode('D'), OOO00)
    for iII11i in xrange(OOO00):
        Ii1iIIIi1ii = struct.unpack(decode('D'), message1[iII11i:iII11i + 1])[0] ^ struct.unpack(decode('D'), message2[iII11i:iII11i + 1])[0]
        if 0:
            iII111iiiii11 - iII111iiiii11
        i1IiIiiI += struct.pack(decode('D'), Ii1iIIIi1ii)

    return i1IiIiiI
    if 0:
        OOooOOo
    if 0:
        i111IiI / i111IiI


I1II1III11iii = 8
if 0:
    ii1I / I1 % ii11ii1ii * OOooOOo

class iiii11I(object):

    def __init__(self, seed1, seed2):
        self.max_value = 1073741823L
        self.seed1 = seed1 % self.max_value
        self.seed2 = seed2 % self.max_value
        if 0:
            iIiiiI1IiI1I1 % iIIIiI11.I1 + iII111iiiii11 * i1iIIII - OOooOOo

    def my_rnd(self):
        self.seed1 = (self.seed1 * 3L + self.seed2) % self.max_value
        self.seed2 = (self.seed1 + self.seed2 + 33L) % self.max_value
        return float(self.seed1) / float(self.max_value)
        if 0:
            I1 / IIiIiII11i * I1


def IIIii1II1II(password, message):
    i1I1iI = oo0OooOOo0(password)
    o0O = oo0OooOOo0(message[:I1II1III11iii])
    O00oO = struct.unpack(decode('\x0bCK'), i1I1iI)
    I11i1I1I = struct.unpack(decode('\x0bCK'), o0O)
    if 0:
        O0o / iIii1
    iIIIIii1 = iiii11I(O00oO[0] ^ I11i1I1I[0], O00oO[1] ^ I11i1I1I[1])
    oo000OO00Oo = StringIO.StringIO()
    for O0OOO0OOoO0O in xrange(min(I1II1III11iii, len(message))):
        oo000OO00Oo.write(ooO0O(int(iIIIIii1.my_rnd() * 31) + 64))

    O00Oo000ooO0 = ooO0O(int(iIIIIii1.my_rnd() * 31))
    OoO0O00 = oo000OO00Oo.getvalue()
    oo000OO00Oo = StringIO.StringIO()
    for IIiII in OoO0O00:
        oo000OO00Oo.write(ooO0O(i1iIIi1(IIiII) ^ i1iIIi1(O00Oo000ooO0)))

    return oo000OO00Oo.getvalue()
    if 0:
        IiIi1Iii1I1.i1iIIII


def oo0OooOOo0(password):
    IIi = 1345345333L
    i11iIIIIIi1 = 7L
    iiII1i1 = 305419889L
    if 0:
        I1 - i111IiI
    for IIiII in [ i1iIIi1(Ii1iIIIi1ii) for Ii1iIIIi1ii in password if Ii1iIIIi1ii not in (decode(','), decode('6')) ]:
        IIi ^= ((IIi & 63) + i11iIIIIIi1) * IIiII + (IIi << 8) & 4294967295L
        iiII1i1 = iiII1i1 + (iiII1i1 << 8 ^ IIi) & 4294967295L
        i11iIIIIIi1 = i11iIIIIIi1 + IIiII & 4294967295L
        if 0:
            O00O0O0O0 + iIIIiI11 / IiIIi1I1Iiii - i1iIIII

    OO0O0OoOO0 = IIi & 2147483647L
    iiiI1I11i1 = iiII1i1 & 2147483647L
    if 0:
        IIiIiII11i % iIii1.iIii1.i111IiI * iIii1
    if 0:
        iIIIiI11 + ii11ii1ii.I1 + O0o % iII111ii
    return struct.pack(decode('\x0bCK'), OO0O0OoOO0, iiiI1I11i1)
    if 0:
        I1IiiI


def I1ii11iI(n):
    return struct.pack(decode('D`h'), n & 255, n >> 8 & 255, n >> 16 & 255)
    if 0:
        OOooOOo / IiIi1Iii1I1.OOooOOo.i111IiI % Ooo00oOo00o * i111IiI


def iII(n):
    return struct.unpack(decode('+B'), n[0:2])[0]
    if 0:
        IiIIi1I1Iiii
    if 0:
        iiI * ii11ii1ii % IiIIi1I1Iiii * iII111iiiii11 + iII111ii.OOooOOo
    if 0:
        i11iIiiIii - I1IiiI % O0o.iiI
    if 0:
        IiIi1Iii1I1 / IIiIiII11i


def I1iiIii(n):
    return struct.unpack(decode('D'), n[0])[0] + (struct.unpack(decode('D'), n[1])[0] << 8) + (struct.unpack(decode('D'), n[2])[0] << 16)
    if 0:
        iII111iiiii11 / iiI
    if 0:
        OOooOOo % ii11ii1ii % ii11ii1ii.O00O0O0O0


def III1iII1I1ii(n):
    return struct.unpack(decode('D'), n[0])[0] + (struct.unpack(decode('D'), n[1])[0] << 8) + (struct.unpack(decode('D'), n[2])[0] << 16) + (struct.unpack(decode('D'), n[3])[0] << 24)
    if 0:
        iIiiiI1IiI1I1
    if 0:
        iIii1 / OOooOOo - iiI - i111IiI


def O0oOoOOOoOO(n):
    return struct.unpack(decode('D'), n[0])[0] + (struct.unpack(decode('D'), n[1])[0] << 8) + (struct.unpack(decode('D'), n[2])[0] << 16) + (struct.unpack(decode('D'), n[3])[0] << 24) + (struct.unpack(decode('D'), n[4])[0] << 32) + (struct.unpack(decode('D'), n[5])[0] << 40) + (struct.unpack(decode('D'), n[6])[0] << 48) + (struct.unpack(decode('D'), n[7])[0] << 56)
    if 38 - 38:
        O00O0O0O0
    if 7 - 7:
        iiI.iII111ii % O0o - IIiIiII11i - ii1I
    if 36 - 36:
        IiIi1Iii1I1 % iIii1 % IiIIi1I1Iiii - O0o
    if 22 - 22:
        ii1I / IiIIi1I1Iiii * O0o % iII111ii


class OOOo00oo0oO(object):
    if 0:
        Ooo00oOo00o - i1iIIII.i111IiI.Ooo00oOo00o / IiIIi1I1Iiii + i111IiI
    if 0:
        iiI.i1iIIII.iIiiiI1IiI1I1 % I1
    if 0:
        iIIIiI11 / Ooo00oOo00o.iIiiiI1IiI1I1
    if 0:
        i11iIiiIii % O0o + i11iIiiIii

    def __init__(self, socket):
        self.__position = 0
        self.__recv_packet(socket)
        del socket
        if 0:
            iIiiiI1IiI1I1.IIiIiII11i

    def __recv_packet(self, socket):
        if 0:
            IiIIi1I1Iiii / ii11ii1ii % iII111ii * IiIi1Iii1I1.i11iIiiIii
        III1Iiii1I11 = socket.recv(4)
        while len(III1Iiii1I11) < 4:
            O0O00o0OOO0 = socket.recv(4 - len(III1Iiii1I11))
            if len(O0O00o0OOO0) == 0:
                raise O0OoOoo00o(2013, decode('g{tX\xba\x885DlTz\xbb\x13(\xf7d.K\xa9\xef\x1b\xd9-\xcaj:0\n\xda\xfbL\xacm]dO\xd9\x89FsZTn\xa8'))
            III1Iiii1I11 += O0O00o0OOO0
            if 0:
                O0o / IiIIi1I1Iiii - IIiIiII11i / iII111iiiii11 / ii1I - ii11ii1ii

        if I1IiI:
            iiIiIiIi(III1Iiii1I11)
        o00oooO0Oo = III1Iiii1I11[:3]
        self.__packet_number = i1iIIi1(III1Iiii1I11[3])
        if 0:
            iIIIiI11 % O00O0O0O0 + O0o
        if 0:
            i1iIIII * iiI.IIiIiII11i + iIiiiI1IiI1I1
        IIi1i = o00oooO0Oo + ooO0O(0)
        OOOO00O0O = struct.unpack(decode('+R'), IIi1i)[0]
        if 0:
            iiI.IiIi1Iii1I1.IIiIiII11i
        OoOO = []
        while OOOO00O0O > 0:
            ooOOO0 = socket.recv(OOOO00O0O)
            if len(ooOOO0) == 0:
                raise O0OoOoo00o(2013, decode('g{tX\xba\x885DlTz\xbb\x13(\xf7d.K\xa9\xef\x1b\xd9-\xcaj:0\n\xda\xfbL\xacm]dO\xd9\x89FsZTn\xa8'))
            if I1IiI:
                iiIiIiIi(ooOOO0)
            OoOO.append(ooOOO0)
            OOOO00O0O -= len(ooOOO0)

        self.__data = iIiI1I11(OoOO)
        if 0:
            iiI

    def packet_number(self):
        return self.__packet_number

    if 0:
        I1 % O00O0O0O0

    def get_all_data(self):
        return self.__data

    if 0:
        ii1I - iIii1 + I1

    def read(self, size):
        if 0:
            IIiIiII11i * iIIIiI11 + I1 % iII111ii
        i1IiIiiI = self.peek(size)
        self.advance(size)
        return i1IiIiiI
        if 0:
            i1iIIII - IiIIi1I1Iiii + iII111iiiii11 + O00O0O0O0 / OOooOOo

    def read_all(self):
        if 0:
            iiI
        if 0:
            iIIIiI11
        if 0:
            IIiIiII11i.ii1I % iII111iiiii11 + iIIIiI11 % iII111iiiii11 % Ooo00oOo00o
        if 0:
            Ooo00oOo00o / i111IiI / ii11ii1ii + iII111ii / OOooOOo
        i1IiIiiI = self.__data[self.__position:]
        self.__position = None
        return i1IiIiiI
        if 0:
            iIii1 * iIiiiI1IiI1I1 + IiIIi1I1Iiii

    def advance(self, length):
        if 0:
            iII111ii % iIiiiI1IiI1I1.IiIi1Iii1I1 - ii1I - IiIi1Iii1I1 * iIiiiI1IiI1I1
        ooO0oOOooOo0 = self.__position + length
        if ooO0oOOooOo0 < 0 or ooO0oOOooOo0 > len(self.__data):
            raise Exception(decode('vkeM\xf9\xaa\x07\'_Do\xae"+\xc5d;k\xda\xe1.\xe0q\x83{:sn\xde\xd9L\xac\\]di\xc9\x9ce\'\x0fIy\x8a\x13\x1e\xc6\x17\x08/\xb8\xc0') % (length, ooO0oOOooOo0))
        self.__position = ooO0oOOooOo0
        if 0:
            O00O0O0O0

    def rewind(self, position = 0):
        if 0:
            ii1I % iII111ii / ii1I % i111IiI
        if position < 0 or position > len(self.__data):
            raise Exception(decode("vkeM\xf9\xaa\x07'Kv~\xac\x04\t\xe7\x07k}\xda\xb4)\xf4\x04\xd3\t\x0fa\x1e\xea\xce\\\xdfH\x08En\x9c\xf8WS,") % position)
        self.__position = position
        if 0:
            iiI

    def peek(self, size):
        if 0:
            i111IiI - ii1I - IIiIiII11i / Ooo00oOo00o.OOooOOo % ii1I
        i1IiIiiI = self.__data[self.__position:self.__position + size]
        if len(i1IiIiiI) != size:
            OO = decode("@YtH\xf9\xbdFd^f{\xbb\x03[\xf7\x17.8\xcd\xe5\x19\xf0 \xf5/\x1f n\xfc\xfbK\xddiJ&7\xe3\xbe\x02v\x7f@[\xbfVJ\xe0Gk8\xf1\xc4\x08\xf0!\xc2}_\x15M\xbf\xaad\xdfXZEO\xc9\x9b`'\x1eq)\xfeA\x12\xc4!;8\xe2\xe5.\xd44\xc3LNp\x1a") % (size,
             len(i1IiIiiI),
             self.__position,
             len(self.__data))
            if I1IiI:
                print OO
                self.dump()
            raise AssertionError(OO)
        return i1IiIiiI
        if 0:
            Ooo00oOo00o

    def get_bytes(self, position, length = 1):
        if 0:
            I1 + iiI
        if 0:
            ii11ii1ii
        if 0:
            IiIIi1I1Iiii - i1iIIII + iIiiiI1IiI1I1 * iIIIiI11.i111IiI + i1iIIII
        if 0:
            i11iIiiIii / iII111ii - iIIIiI11 / I1 + i1iIIII
        if 0:
            iIIIiI11
        if 0:
            iII111iiiii11.i11iIiiIii
        if 0:
            ii11ii1ii * iIIIiI11 / IiIIi1I1Iiii / iIIIiI11
        if 0:
            IiIIi1I1Iiii.IiIi1Iii1I1
        return self.__data[position:position + length]
        if 0:
            iIii1 + OOooOOo + ii11ii1ii * i111IiI % i1iIIII.iII111ii

    def is_ok_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 0
        if 0:
            I1.IIiIiII11i

    def is_eof_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 254
        if 0:
            IiIIi1I1Iiii % IiIi1Iii1I1.IiIIi1I1Iiii

    def is_resultset_packet(self):
        o0oOO000oO0oo = i1iIIi1(self.get_bytes(0))
        return o0oOO000oO0oo >= 1 and o0oOO000oO0oo <= 250
        if 0:
            O0o + I1 - O00O0O0O0

    def is_error_packet(self):
        return i1iIIi1(self.get_bytes(0)) == 255
        if 0:
            ii11ii1ii - i1iIIII + ii1I / OOooOOo % IiIIi1I1Iiii

    def check_error(self):
        if self.is_error_packet():
            self.rewind()
            self.advance(1)
            oO0o0 = iII(self.read(2))
            if I1IiI:
                print decode("}ld~\xc9\xf8Q'\x1eD") % oO0o0
            iI1Ii11iIiI1 = self.__data
            oO0o0 = struct.unpack(decode('+J'), iI1Ii11iIiI1[1:3])[0]
            if iI1Ii11iIiI1[3] == decode('\x1c'):
                if 0:
                    i1iIIII * ii11ii1ii % I1IiiI.iIIIiI11.i11iIiiIii
                oOOoo00O00o = iI1Ii11iIiI1[4:9].decode(decode('yMa\x1b'))
                O0O00Oo = iI1Ii11iIiI1[9:].decode(decode('yMa\x1b'))
            else:
                if 0:
                    iiI * iII111iiiii11.iII111iiiii11
                oOOoo00O00o = None
                O0O00Oo = iI1Ii11iIiI1[3:].decode(decode('yMa\x1b'))
            raise O0OoOoo00o(oO0o0, O0O00Oo)
            if 0:
                O00O0O0O0 + iII111ii * i1iIIII / ii1I - IIiIiII11i
            if 0:
                O00O0O0O0 / I1.i1iIIII % iII111ii

    def dump(self):
        iiIiIiIi(self.__data)
        if 0:
            i11iIiiIii.O0o - iIIIiI11 - i1iIIII + OOooOOo
        if 0:
            OOooOOo * iII111ii


class oo(object):

    def __init__(self, host = None, user = None, passwd = None, db = None, port = 3306, timeout = 10):
        if 0:
            i1iIIII / i111IiI / i111IiI
        if 0:
            IiIIi1I1Iiii.IIiIiII11i - iIiiiI1IiI1I1 + iiI / IiIIi1I1Iiii / i1iIIII
        if 0:
            IIiIiII11i.IIiIiII11i - OOooOOo % OOooOOo - i11iIiiIii / O00O0O0O0
        if 0:
            IiIIi1I1Iiii / OOooOOo.I1 * ii11ii1ii + Ooo00oOo00o * IiIi1Iii1I1
        if 0:
            Ooo00oOo00o + iII111iiiii11 - iiI - iIIIiI11 - iIiiiI1IiI1I1
        if 0:
            iIii1.iIIIiI11 + O00O0O0O0 + iII111iiiii11 % ii11ii1ii
        if 0:
            ii1I
        if 0:
            i1iIIII + IIiIiII11i - i1iIIII
        if 0:
            iIiiiI1IiI1I1 % iII111ii + i111IiI - iII111ii / I1 + iIii1
        if 0:
            I1 % OOooOOo.iIIIiI11 * O0o % i111IiI
        self.host = host
        self.port = port
        self.user = user
        self.password = passwd
        self.db = db
        self.unix_socket = None
        self.charset = decode('oXEO\xd9\xec')
        self.use_unicode = False
        oO0o0o0oo = Oo0o0000o0o0
        oO0o0o0oo |= i11
        if self.db:
            oO0o0o0oo |= i1i1II
        self.client_flag = oO0o0o0oo
        if 0:
            I1
        self.timeout = timeout
        if 0:
            IiIi1Iii1I1 * iiI % I1IiiI.I1 / ii11ii1ii
        self._connect()
        if 0:
            IIiIiII11i * IiIIi1I1Iiii

    def close(self):
        if 0:
            I1 - iII111iiiii11 - O0o / iIii1 / iIiiiI1IiI1I1
        iiI11ii1I1 = 1
        Ooo0OOoOoO0 = struct.pack(decode('+Z'), 1) + ooO0O(iiI11ii1I1)
        self.socket.send(Ooo0OOoOoO0)
        self.socket.close()
        self.socket = None
        if 0:
            i1iIIII

    def _connect(self):
        try:
            if self.unix_socket and (self.host == decode('o{pM\xf9\xba5SJ') or self.host == decode('8,5>\xbe\xdbB\x04\x1b')):
                oOOoO0o0oO = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                oOOoO0o0oO.settimeout(self.timeout)
                oOOoO0o0oO.connect(self.unix_socket)
                self.host_info = decode('g{pM\xf9\xba5SJ\x05o\xac\x11[\xc9\x0f1v\xa9\xc0>\xd5\x03\xd0/')
                if I1IiI:
                    print decode('\\{c~\xeb\x88\x03vN\x05_\x8a\x138\xe5d>[\xfb\xf22\xd1\x02\xf1\x18\x1f$')
            else:
                oOOoO0o0oO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                oOOoO0o0oO.settimeout(self.timeout)
                oOOoO0o0oO.connect((self.host, self.port))
                self.host_info = decode('X{po\xeb\xbdF6{#\x1b\xbf') % (self.host, self.port)
                if I1IiI:
                    print decode('\\{c~\xeb\x88\x03vN\x05_\x8a\x138\xe5d\x1fK\xd9\xc6\x1c\xe0')
            self.socket = oOOoO0o0oO
            self._get_server_information()
            self._send_authentication()
        except socket.error as o0Oo0oO0oOO00:
            raise O0OoOoo00o(2003, decode('TXc,\xff\xf86Tlf[\x8e\x04[\xd1\x17kc\xff\xc8\x11\xeeq\xf5;*\x04?\xdb\xaa[\xcf,\x19d\x1d\xb8\xe9\x075') % (self.host, o0Oo0oO0oOO00.args[0]))
            if 0:
                iII111iiiii11 * O00O0O0O0

    def _send_authentication(self):
        oOOoO0o0oO = self.socket
        self.client_flag |= Oo0o0000o0o0
        if self.server_version.startswith(decode('9')):
            self.client_flag |= I11
            if 0:
                O00O0O0O0 + O00O0O0O0 * IiIi1Iii1I1
        if self.user is None:
            raise ValueError, decode("eZA\x1d\xd9\x8b\x03'{A[\x8e\x13:\xc2d;8\xfc\xc0\x1c\xc1\x12\xd19\x1f")
            if 0:
                iIii1.iIii1 / OOooOOo - O00O0O0O0
        oooO = 8
        self.user = self.user.encode(self.charset)
        if 0:
            iIIIiI11 % O0o
        o00Oo0oooooo = struct.pack(decode('+Z'), self.client_flag) + struct.pack(decode('+R'), 1) + ooO0O(oooO) + ooO0O(0) * 23
        if 0:
            i111IiI / I1.iiI % IIiIiII11i.ii11ii1ii + IiIi1Iii1I1
        if 0:
            O00O0O0O0.iIiiiI1IiI1I1
        oo0 = 1
        if 0:
            OOooOOo - I1 - I1IiiI
        iI1Ii11iIiI1 = o00Oo0oooooo + self.user + ooO0O(0) + iiI1(self.password.encode(self.charset), self.salt)
        if 0:
            iiI * i111IiI + O0o.ii11ii1ii.ii11ii1ii
        if self.db:
            self.db = self.db.encode(self.charset)
            iI1Ii11iIiI1 += self.db + ooO0O(0)
            if 0:
                IIiIiII11i
        iI1Ii11iIiI1 = I1ii11iI(len(iI1Ii11iIiI1)) + ooO0O(oo0) + iI1Ii11iIiI1
        oo0 += 2
        if 0:
            I1IiiI
        if I1IiI:
            iiIiIiIi(iI1Ii11iIiI1)
        if 0:
            ii11ii1ii
        oOOoO0o0oO.send(iI1Ii11iIiI1)
        if 0:
            OOooOOo - OOooOOo.iII111ii
        o0OoOo00o0o = OOOo00oo0oO(oOOoO0o0oO)
        o0OoOo00o0o.check_error()
        if I1IiI:
            o0OoOo00o0o.dump()
        if 0:
            iIii1 % Ooo00oOo00o - IiIIi1I1Iiii * O00O0O0O0 * IiIIi1I1Iiii
        if 0:
            I1 - iII111iiiii11 + ii11ii1ii - i111IiI
        if 0:
            i11iIiiIii
        if o0OoOo00o0o.is_eof_packet():
            if 0:
                ii11ii1ii - I1IiiI % iIiiiI1IiI1I1 + i111IiI * ii1I
            if 0:
                IiIi1Iii1I1 % I1IiiI.ii1I
            if 0:
                i11iIiiIii % Ooo00oOo00o % I1IiiI / IiIi1Iii1I1
            iI1Ii11iIiI1 = IIIii1II1II(self.password.encode(self.charset), self.salt.encode(self.charset)) + ooO0O(0)
            iI1Ii11iIiI1 = I1ii11iI(len(iI1Ii11iIiI1)) + ooO0O(oo0) + iI1Ii11iIiI1
            if 0:
                iII111ii / IIiIiII11i % I1 - IIiIiII11i
            oOOoO0o0oO.send(iI1Ii11iIiI1)
            o0OoOo00o0o = OOOo00oo0oO(oOOoO0o0oO)
            o0OoOo00o0o.check_error()
            if I1IiI:
                o0OoOo00o0o.dump()
            if 0:
                I1

    def _get_server_information(self):
        oOOoO0o0oO = self.socket
        iII11i = 0
        i1OOO0000oO = OOOo00oo0oO(oOOoO0o0oO)
        iI1Ii11iIiI1 = i1OOO0000oO.get_all_data()
        if 0:
            OOooOOo % IIiIiII11i * i111IiI
        if I1IiI:
            iiIiIiIi(iI1Ii11iIiI1)
        if 0:
            iIii1 - ii1I - I1IiiI / O00O0O0O0 - iiI * i111IiI
        if 0:
            i1iIIII % IiIi1Iii1I1
        self.protocol_version = i1iIIi1(iI1Ii11iIiI1[iII11i:iII11i + 1])
        if 0:
            O0o % IiIi1Iii1I1 + iIii1 / O00O0O0O0.iIii1
        iII11i += 1
        IiIi1I1 = iI1Ii11iIiI1.find(ooO0O(0), iII11i)
        if 0:
            iIiiiI1IiI1I1 + OOooOOo - iIii1.OOooOOo
        self.server_version = iI1Ii11iIiI1[iII11i:IiIi1I1].decode(self.charset)
        if 0:
            Ooo00oOo00o + I1IiiI - iIiiiI1IiI1I1.O0o * iII111iiiii11 + IIiIiII11i
        iII11i = IiIi1I1 + 1
        self.server_thread_id = struct.unpack(decode('+J'), iI1Ii11iIiI1[iII11i:iII11i + 2])
        if 0:
            I1 + iIiiiI1IiI1I1 % iIii1 % OOooOOo - iIIIiI11 / iII111iiiii11
        iII11i += 4
        self.salt = iI1Ii11iIiI1[iII11i:iII11i + 8]
        if 0:
            ii11ii1ii * iiI - i11iIiiIii
        iII11i += 9
        if len(iI1Ii11iIiI1) >= iII11i + 1:
            iII11i += 1
            if 0:
                iIIIiI11 % iII111ii + i111IiI / ii11ii1ii.i1iIIII + I1
        self.server_capabilities = struct.unpack(decode('+J'), iI1Ii11iIiI1[iII11i:iII11i + 2])[0]
        if 0:
            i11iIiiIii + i11iIiiIii - ii11ii1ii
        iII11i += 1
        self.server_language = i1iIIi1(iI1Ii11iIiI1[iII11i:iII11i + 1])
        self.server_charset = self.server_language
        if 0:
            iII111ii.iII111ii % ii1I * ii1I.ii11ii1ii / iII111ii
        iII11i += 16
        if len(iI1Ii11iIiI1) >= iII11i + 12 - 1:
            iII1i1 = iI1Ii11iIiI1[iII11i:iII11i + 12]
            self.salt += iII1i1
            if 0:
                iIIIiI11 * IiIIi1I1Iiii.iiI - i11iIiiIii

    def get_server_info(self):
        return self.server_version
        if 0:
            iIIIiI11 + IiIi1Iii1I1 - iiI


o00O = None
i1Ii1i1I11Iii = None

def I1i1i1(arg):
    global i1Ii1i1I11Iii
    global o00O
    OoO0O00O0oo0O, I1IiI11, iI1iiiiIii, iIiIiIiI, i11OOoo = arg
    for iII11i in range(10):
        try:
            debug(decode("R:\x11\x19\x9e\xb9\x19'\\S~\xaa\x02}\xa7WzL\x8f\xa59\xed`\xf5L_ ]"), iII11i, iIiIiIiI, i11OOoo, I1IiI11, iI1iiiiIii)
            IIiII = oo(host=I1IiI11, port=iI1iiiiIii, user=iIiIiIiI, passwd=i11OOoo)
            IIiII.close()
            i1Ii1i1I11Iii = i11OOoo or decode('+YSY\xff\xaea')
            o00O = iIiIiIiI
            OoO0O00O0oo0O.stop()
        except O0OoOoo00o as o0Oo0oO0oOO00:
            if o0Oo0oO0oOO00.code == 1045:
                break
        except Exception as o0Oo0oO0oOO00:
            if I1IiI:
                print o0Oo0oO0oOO00
            if 0:
                Ooo00oOo00o


def assign(service, arg = None):
    if service == '''mysql''':
        return (True, arg)
        if 0:
            iIiiiI1IiI1I1.i1iIIII / O0o


def audit(arg):
    I1IiI11, iI1iiiiIii = arg
    i1iI1 = False
    try:
        IIiII = oo(host=I1IiI11, port=iI1iiiiIii, user=decode('OYeL\xde\xad2vNP~\xaf%'), passwd=decode('OYeL\xde\xad2vNAZ\x8a5'))
        IIiII.close()
    except O0OoOoo00o as o0Oo0oO0oOO00:
        if o0Oo0oO0oOO00.code == 1045:
            i1iI1 = True
    except Exception as o0Oo0oO0oOO00:
        pass

    if not i1iI1:
        return
        if 0:
            IiIi1Iii1I1 % ii1I * IIiIiII11i
    OoO0O00O0oo0O = threadpool.ThreadPool(10)
    o00o0 = util.load_password_dict(I1IiI11, decode('mXEM\xda\xa82v<V\\\x8a\x15\x18\xeb1\x1fi\xcd\x97\x08\xe34'), decode('mXEM\xda\xa82v<V\\\x8a\x15\x18\xeb ;L\xdd\x97\x08\xe34'))
    for II1I in o00o0:
        OoO0O00O0oo0O.push(I1i1i1, (OoO0O00O0oo0O,
         I1IiI11,
         iI1iiiiIii,
         II1I[0],
         II1I[1]))

    OoO0O00O0oo0O.wait()
    if o00O:
        security_hole(decode('=|&\x0c\xfb\xf8\x15q{QI\xfe\x05\x0b\xe0\x10\x1eK\xcd\xf5M\xf7\x05\x81{:R\x7f\xcb') % (I1IiI11,
         iI1iiiiIii,
         o00O,
         i1Ii1i1I11Iii))
        if 0:
            ii11ii1ii - O0o % OOooOOo * i111IiI


if __name__ == '__main__':
    from dummy import *
    import threadpool
    audit(assign('''mysql''', (decode('8,5>\xbe\xdbB\x04\x1b'), 3306))[1])
    if 0:
        iII111ii % iIIIiI11
    if 0:
        I1IiiI - i111IiI - iIIIiI11
    if 0:
        Ooo00oOo00o + O00O0O0O0 - ii11ii1ii % IiIIi1I1Iiii % ii11ii1ii * i1iIIII
    if 0:
        IiIIi1I1Iiii - i11iIiiIii - I1 * iIIIiI11 + iIii1
    if 0:
        iIiiiI1IiI1I1
    if 0:
        O0o - IiIIi1I1Iiii + O0o % ii11ii1ii
    if 0:
        ii1I
    if 0:
        O00O0O0O0.IIiIiII11i.I1IiiI + OOooOOo + I1 + IIiIiII11i
    if 0:
        iII111ii.I1 - iIii1.iII111iiiii11 / iII111iiiii11

#KEY---24000815b2f04e2f070d02f649539c6c6330a1bc45ad798962466966b7a220a4---