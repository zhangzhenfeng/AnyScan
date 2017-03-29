#Embedded file name: dnszone_transfer.py
if 0:
    i11iIiiIii
if 0:
    O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if 0:
    II111iiii
import time

def assign(service, arg = None):
    if service == '''dns''':
        return (True, util.get_domain_root(arg))
        if 0:
            I1IiiI * Oo0Ooo / OoO0O00.OoOoOO00.o0oOOo0O0Ooo / I1ii11iIi11i


def I1IiI(src, dst):
    if src == dst:
        return True
    else:
        if dst.startswith(decode('H\xe1E\xd9')):
            dst = dst[4:]
        return src.endswith(decode('\x11') + dst)
    if 0:
        OOooOOo / ii11ii1ii


def O00ooOO(host):
    if host.find(decode('\x11')) != -1 and host != _G[decode('K\xf7@\x90d\xe1')] and I1IiI(host, _G[decode('K\xf7@\x90d\xe1')]):
        I1iII1iiII = decode('W\xe2F\x87;\xba\x12\xdcmT') % host
        task_push('''www''', I1iII1iiII, I1iII1iiII, host)
        if 0:
            Ii11111i * iiI1i1


def audit(arg):
    i1I1ii1II1iII = arg
    oooO0oo0oOOOO = {}
    for O0oO in range(3):
        try:
            o0oO0 = DNS.Resolver(timeout=20)
            oo00, o00 = o0oO0.NameServer(i1I1ii1II1iII)
            for Oo0oO0ooo in o00:
                debug(decode('d\xf2\\\x84\\\xb5G\x96p\x1e)\x9b\x07\xf4\xf9\xf7\x80:'), i1I1ii1II1iII, Oo0oO0ooo)
                o0oOoO00o = o0oO0.Raw(i1I1ii1II1iII, qtype=DNS.T_AXFR, recursion=True, proto=decode('K\xf5B'), nsserver=Oo0oO0ooo)
                for i1 in o0oOoO00o[decode('~\xd8a\xa0D\xc7')]:
                    if i1[decode('k\xcfb\xb2')] in [DNS.T_A, DNS.T_CNAME, DNS.T_NS]:
                        oooO0oo0oOOOO[i1[decode('{\xd9\x7f\xb6H\xdb')]] = i1[decode('m\xd2s\xa3@')]

            if oooO0oo0oOOOO:
                break
            else:
                time.sleep(3)
        except Exception as oOOoo00O0O:
            pass

    if oooO0oo0oOOOO:
        security_info(str(oooO0oo0oOOOO))
        if _G[decode('L\xe3P\x93n\xf8\\\x90p')]:
            for i1111 in oooO0oo0oOOOO:
                O00ooOO(i1111)
                if 0:
                    OOo000.O0I11i1i11i1I


if __name__ == '__main__':
    from dummy import *
    from dummy import _G
    from dummy import DNS
    if 0:
        i11iI / Oo0o0ooO0oOOO + II111iiii - i11iIiiIii % i11iI
    _G[decode('K\xf7@\x90d\xe1')] = decode("]\xfa]\x90/\xf0\\\x89n\x17v\x9aK\xbe\xe7\x99\xc6'")
    _G[decode('L\xe3P\x93n\xf8\\\x90p')] = True
    if 0:
        ii11ii1ii % O0 + I1IiiI - OOo000 / Ii11111i
    audit(assign('''dns''', decode('K\xf7Y\x92d\xbb^\x97'))[1])

#KEY---3f9632f701953df91e7b13b428d18ab7a549520831cc2a46984c83e81b933673---