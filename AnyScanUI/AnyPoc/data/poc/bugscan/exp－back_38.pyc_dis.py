#Embedded file name: dns_enum.py
import socket
import Queue
import time

def assign(service, arg = None):
    if service == '''dns''':
        return (True, util.get_domain_root(arg))
        if 0:
            i11iIiiIii


def OO0o(src, dst):
    if src == dst:
        return True
    else:
        if dst.startswith('''www.'''):
            dst = dst[4:]
        return src.endswith('''.''' + dst)
    if 0:
        Iii1I1 + OO0O0O % iiiii % ii1I - ooO0OO000o


def ii11i(host):
    if host.find('''.''') != -1 and OO0o(host, _G['''target''']):
        oOooOoO0Oo0O = '''http://%s/''' % host
        task_push('''www''', oOooOoO0Oo0O, oOooOoO0Oo0O, host)
        if 0:
            IIiI1I11i11


def ooOO00oOo(arg):
    OOOo0, Oooo000o, IiIi11iIIi1Ii = arg
    try:
        Oo0O = socket.gethostbyname(OOOo0)
        if Oo0O and (not IiIi11iIIi1Ii or Oo0O.find(IiIi11iIIi1Ii) == -1):
            if 0:
                iiiiIi11i.o0O / OoOO + I1iII1iiII
            if 0:
                Ii11111i * iiI1i1
            Oooo000o.put((OOOo0, Oo0O))
    except Exception as i1I1ii1II1iII:
        if 0:
            oO0o
        if 0:
            OOO0o0o / o0oO0 + i111I * O0Oo0oO0o.II1iI.i1iIii1Ii1II


def audit(arg):
    if not _G['''subdomain''']:
        return
    i1I1Iiii1111 = threadpool.ThreadPool(300)
    Oooo000o = Queue.Queue()
    i11 = arg
    I11 = util.list_from_file('''database/sub_domain.txt''')
    IiIi11iIIi1Ii = None
    try:
        IiIi11iIIi1Ii = socket.gethostbyname('''faken0ndoma1nfakenond0main.''' + i11)
        IiIi11iIIi1Ii = '''.'''.join(IiIi11iIIi1Ii.split('''.''')[:2]) + '''.'''
    except:
        pass

    for Oo0o0000o0o0 in I11:
        OOOo0 = Oo0o0000o0o0 + '''.''' + i11
        i1I1Iiii1111.push(ooOO00oOo, (OOOo0, Oooo000o, IiIi11iIIi1Ii))

    i1I1Iiii1111.wait()
    oOo0oooo00o = decode('')
    for oO0o0o0ooO0oO in range(Oooo000o.qsize()):
        OOOo0, Oo0O = Oooo000o.get()
        oOo0oooo00o += decode('\xb1kbn\xe8\x8b') % (OOOo0, Oo0O)
        if _G['''subdomain''']:
            ii11i(OOOo0)

    if oOo0oooo00o:
        security_note(str(oOo0oooo00o))


if __name__ == '__main__':
    from dummy import *
    from dummy import _G
    import threadpool
    _G['''target'''] = decode('\xe3cp6\xfb\xf7')
    _G['''subdomain'''] = True
    if 0:
        ooO0OO000o - i11iIiiIii % II1iI

#KEY---8505495a868258d1a09f88cf12b87431531bedca34a3dafc03ab58d741c0bbd7---