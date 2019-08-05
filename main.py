#!/usr/bin/env python3
import os
from executor import Subhelp

v_check = './version-check.sh'
mnt = '/mnt/lfs'

def variabl(mnt):
    res = Subhelp('su -u root export LFS={}'.format(mnt)).result()
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

def packets(data):

    try:
        with open('wget-list', 'r') as data:
            rw = data.read()
        
        if rw[0] in Subhelp('ls -1 {}/sources'.format(data)).result().split('\n'):   
            print('DOWNLOAD PACKAGES')
            res = Subhelp('mkdir -v $LFS/sources').result()
            res2 = Subhelp('mkdir -v $LFS/tools').result()
            res5 = Subhelp('ln -sv $LFS/tools /').result()
            res3 = Subhelp('chmod -v a+wt $LFS/sources').result()
            res4 = Subhelp('wget --input-file=wget-list --continue --directory-prefix=$LFS/sources').result()
            print('OPERATION COMPLETE')

        else:
            pass

    except:
        print('OPERATION FAILED')

def user():
    
    try:
        if 'lfs' not in Subhelp('cat /etc/passwd | awk -F \':\' \'{print $1}\' ').result().split('\n'):
        
            group = Subhelp('groupadd lfs').result()
            user = Subhelp('useradd -s /bin/bash -g lfs -m -k /dev/null lfs').result()
            passwd = Subhelp('echo -e "Test123\nTest123" | passwd lfs').result()
            tools = Subhelp('chown -v lfs $LFS/tools').result()
            sources = Subhelp('chown -v lfs $LFS/sources').result()
        
        else:

            tools = Subhelp('chown -v lfs $LFS/tools').result()
            sources = Subhelp('chown -v lfs $LFS/sources').result()

        print('USER AND GROUP WAS CREATED!')

    except:
        print('OPERATION IS FAILED')



if __name__ == '__main__':
    disk_name = input('DISK_NAME: ')
    
    variabl(mnt)
    v_info(v_check)
    disk_main(disk_name)
    mount(disk_name)
    packets(mnt)
    user()
