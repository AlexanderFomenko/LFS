#!/usr/bin/env python3
import os
from executor import Subhelp

path = '$LFS/sources/'

def unpack(data):

    def get_pack():
        with open('wget-list', 'r') as data:
            res = data.read()
        res = [i.split('/')[-1] for i in res.split('\n') if i != '']
        return res

    for pack in get_pack():
        if pack[-5:] != 'patch':
            print(Subhelp('tar -xvf {0}{1} -C {0}'.format(data, pack)).result())

unpack(path)

