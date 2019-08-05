#!/usr/bin/env python3
import os
from executor import Subhelp

path = '$LFS/sources/'

def envir():
    #res = Subhelp("""sudo -u lfs cat > ~/.bash_profile << "EOF" exec env -i HOME=$HOME TERM=$TERM PS1='\u:\w\$ ' /bin/bash EOF""").result()
    #res2 = Subhelp("""cat > ~/.bashrc << "EOF" set +h umask 022 LFS=/mnt/lfs LC_ALL=POSIX LFS_TGT=$(uname -m)-lfs-linux-gnu PATH=/tools/bin:/bin:/usr/bin export LFS LC_ALL LFS_TGT PATH EOF""").result()
    res3 = Subhelp("source ~/.bash_profile").result()
    count_proc = Subhelp("cat /proc/cpuinfo|grep processor|wc -l").result()
    res4 = Subhelp("export MAKEFLAGS='-j {}'".format(count_proc)).result()
    print('ENVIRONMENT [OK]')

def unpack(data):

    def get_pack():

        with open('wget-list', 'r') as data:
            res = data.read()
        res = [i.split('/')[-1] for i in res.split('\n') if i != '']
        return res

    for pack in get_pack():
        if pack[-5:] != 'patch':
            print(Subhelp('sudo -u lfs tar -xvf {0}{1} -C {0}'.format(data, pack)).result())

#envir()
unpack(path)

