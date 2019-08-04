#!/usr/bin/env python3
import argparse
from subprocess import PIPE, Popen


class Subhelp:
    
    def __init__(self,command):
        self.command = command
    
    def result(self):
        res = Popen(self.command, stdout = PIPE, stderr = PIPE, shell = True).communicate(timeout = 2000)[0].decode()
        return res
