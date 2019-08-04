#!/usr/bin/env python3
import os
from executor import Subhelp

v_check = './version-check.sh'
mnt = '/mnt/lfs'

def variabl(mnt):
    res = Subhelp('export LFS={}'.format(mnt)).result()
    print('export LFS={}'.format(mnt))
    print('Variables is [OK]')

def v_info(data):
    res = Subhelp(data)
    print(res.result())

def disk_main(data):
    res = Subhelp('fdisk -l {}'.format(data))
    print(res.result())

def mount(disk_name):
    if os.path.exists('/mnt/lfs') is True:
        mount = Subhelp('mount {} $LFS'.format(disk_name)).result()
        print(mount)
    

    else: 
        make = Subhelp('mkdir -pv $LFS'.format(disk_name)).result()
        mount = Subhelp('mount {} $LFS'.format(disk_name)).result()
        print(make, '\n', mount)

def packets():
    res = Subhelp('mkdir -v $LFS/sources').result()
    res2 = Subhelp('mkdir -v $LFS/tools').result()
    res3 = Subhelp('chmod -v a+wt $LFS/sources').result()
    res4 = Subhelp('wget --input-file=wget-list --continue --directory-prefix=$LFS/sources').result()
    print(res, res2, res3)



if __name__ == '__main__':
    disk_name = input('DISK_NAME: ')
    
    variabl(mnt)
    v_info(v_check)
    disk_main(disk_name)
    mount(disk_name)
    packets()
