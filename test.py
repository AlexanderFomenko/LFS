#!/usr/bin/env python3

from executor import Subhelp
import os
#a = Subhelp('cat /etc/passwd | awk -F \':\' \'{print $1}\' ').result().split('\n')

a = os.system('ls -al /').split('\n')
print(a)
