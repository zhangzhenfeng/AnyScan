#Embedded file name: vnc_bypass.py
import socket

def assign(service, arg):
    if service != '''vnc''':
        return
    else:
        return (True, arg)
    if 0:
        i11iIiiIii


def audit(arg):
    OO0o, Oo0Ooo = arg
    debug(decode('\x89\xdf\x94}&\xbc\x05\t5\xd9m\xb3\x06\xa8\x1a\x07\xeb'), OO0o, Oo0Ooo)
    try:
        O0O0OO0O0O0 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        O0O0OO0O0O0.settimeout(10)
        O0O0OO0O0O0.connect((OO0o, Oo0Ooo))
        iiiii = O0O0OO0O0O0.recv(12)
        if iiiii[:3] == decode('\x80\xcf\x98'):
            ooo0OO, min = [ int(II1) for II1 in iiiii[3:-1].split(decode('\xfc')) ]
            O0O0OO0O0O0.send(decode('\x80\xcf\x98\x1eK\xac@If\xd3z\x96'))
            O0O0OO0O0O0.recv(2)
            O0O0OO0O0O0.send(decode('\xd3'))
            if O0O0OO0O0O0.recv(4) == decode('\xd2\x89\xda>'):
                security_hole(decode('\xa4\xe7\xb9\x04T\xb3V\x14l\xc6&\xbc\x0b\x8bRM\xfb\xe1V(\xbf\x9e\x90$\xf4:\xe2\x83') % (OO0o,
                 Oo0Ooo,
                 ooo0OO,
                 min))
        O0O0OO0O0O0.close()
    except:
        if 0:
            Oooo % OOO0O / II1Ii / Ooo


if __name__ == '__main__':
    from dummy import *
    audit(assign('''vnc''', (decode('\xe3\xbb\xe2\x10J\xa5JId\xd6v\xb2\x11\xef\x14'), 5901))[1])

#KEY---d289da3e7b9c736756e3429c23db20228f8e3547d3a4b540da1f86aaf22ff02f---