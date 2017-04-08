#!/usr/bin/env python
import re

def assign(service, arg):
    if service == "dedecms":
        return True, arg

def audit(arg):
    url = arg
    code, head, res, errcode, _ = curl.curl(url + 'data/mysqli_error_trace.inc')
    if code == 200 and 'exit();' in res:
        security_warning('dedecms error info:' + url + 'data/mysqli_error_trace.inc')

        return arg
if __name__== '__main__':
    from dummy import *
