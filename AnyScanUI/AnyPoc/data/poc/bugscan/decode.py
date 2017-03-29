#coding=utf8
# 2016.03.02 18:03:55 WITA
#Embedded file name: libs/decode.py

import binascii,re
import fcntl

#binascii.b2a_hex(data)
class Decoder:
    def __init__(self, key):
        self.key = key

    def decode(self, text):


        import math

        keys = self.key
        a = 0
        b = 0
        key = 0
        for i in keys:
            key = (key ^ ord(i) * ord(i)) & 255

        for i in range(8):
            if key >> i & 1 == 1:
                a += 1
            else:
                b += 1

        if a > b:
            a ^= b
            b ^= a
            a ^= b
        l = len(text)
        ret = str()
        for i in range(l):
            key = ord(keys[i % 32])
            t = chr(-1 + int(round(math.exp(
                math.log(1 + ((key ^ ord(text[i])) >> b & 255) + (((key ^ ord(text[i])) & (1 << b) - 1) << 8 - b))))))
            ret = ret + chr(((ord(t) & (1 << a) - 1) << 8 - a) + ((ord(t) & (1 << a) - 1 << 8 - a) >> 8 - a) + (
            ord(t) & 255 - ((1 << a) - 1) - ((1 << a) - 1 << 8 - a)))


        # texts = text.encode('string_escape')
        if ret.encode('string_escape').find('jboss.invoca')>-1:
            strx = "texts=" + binascii.b2a_hex(text.encode('string_escape')) + "------" + ret.encode('string_escape') + "----------"+ binascii.b2a_hex(keys)+"--AA--\n"
        else:
            strx = "texts=" + binascii.b2a_hex(text.encode('string_escape')) + "------" + ret + "----------"+ binascii.b2a_hex(keys)+"--AA--\n"

        fl = open("/opt/bugscan/libs/key.txt",'a')
        fcntl.flock(fl, fcntl.LOCK_EX)

        if restr(binascii.b2a_hex(text)) == True or binascii.b2a_hex(text)=='':
            # print u"存在相同，不添加"
            fcntl.flock(fl,fcntl.LOCK_UN)
            fl.close()
        else:
            # print u"不存在，需要添加"
            fl.write(strx)
            fcntl.flock(fl,fcntl.LOCK_UN)
            fl.close()

        return ret

def restr(rexx=''):
    ddd=open("/opt/bugscan/libs/key.txt")

    try:
        re_str=re.search('texts(.*?)%s------'%rexx,ddd.read())
        ddd.close()
        aaaa = re_str.group(1)
        return True
    except:
        ddd.close()
        return False





if __name__ == "__main__":
    asss = Decoder(binascii.a2b_hex("a88b7e002686d3fbc2a187e628d32ec7ddea1fbf47ce00ef6523ce90dba04327")).decode("")
    print asss