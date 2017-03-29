#Embedded file name: padding_oracle.py
import re
import urlparse
import time

def assign(service, arg):
    if service != '''www''':
        return
    else:
        oo000 = urlparse.urlparse(arg)
        return (True, '''%s://%s/WebResource.axd''' % (oo000.scheme, oo000.netloc))
    if 0:
        Ii.o0o00Oo0O - iI11I1II1I1I


def audit(arg):
    oooo = arg
    iIIii1IIi, o0OO00, oo, i1iII1IiiIiI1, iIiiiI1IiI1I1 = curl.curl(oooo + '''?d=''')
    if iIIii1IIi == 404:
        o0OoOoOO00 = '''%s?d=%d''' % (arg, int(time.time()))
        iIIii1IIi, o0OO00, oo, i1iII1IiiIiI1, iIiiiI1IiI1I1 = curl.curl(o0OoOoOO00)
        if iIIii1IIi == 500:
            security_warning(o0OoOoOO00)
            if 0:
                OOOo0 / Oo - Ooo00oOo00o.I1IiI


if __name__ == '__main__':
    from dummy import *

#KEY---a13b6776facce2ce24b9407fe76b7d9a2ac9f97fd11b4c03da49c5dc1bfdd4ed---