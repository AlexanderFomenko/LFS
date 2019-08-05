#!/usr/bin/env python3
from executor import Subhelp

def meka():

    def binutils():
        
        configure = Subhelp('sudo -u lfs mkdir /mnt/lfs/sources/binutils-2.32/build && sudo -u lfs pushd /mnt/lfs/sources/binutils-2.32/build/ && sudo -u lfs ../configure --prefix=/tools            \
             --with-sysroot=/mnt/lfs    \
             --with-lib-path=/tools/lib \
             --target=x86_64-lfs-linux-gnu         \
             --disable-nls              \
             --disable-werror').result()
        print('CONFIGURE COMPLETE!', configure)
        #make = Subhelp('sudo -u lfs pushd $LFS/sources/binutils-2.32/build && sudo -u lfs make').result()       
        print('MAKE COMPLETE!')
        #make_64 = Subhelp('sudo -u lfs case $(uname -m) in \
        #     x86_64) mkdir -v /tools/lib && ln -sv lib /tools/lib64 ;; \
        #     esac').result()
        print('x86_64 LINK COMPLETE!')

        #make_install = Subhelp('sudo -u lfs pushd $LFS/sources/binutils-2.32/build && sudo -u lfs make install').result()       
        print('BINUTILS INSTALL COMPLETE!')

    binutils()
meka()
