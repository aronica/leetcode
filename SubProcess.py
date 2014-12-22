#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import codecs
import subprocess

__author__ = 'fafu'

def main():
    #run command described by args, wait for command to complete, then return the returncode
    a = subprocess.call(["ls","-l"])
    #run command described by args,  If the return
    # code was zero then return, otherwise raise CalledProcessError. The CalledProcessError object will have the return code in the returncode attribute.
    try:
        b = subprocess.check_call(["lss","-l"],shell=True)
    except subprocess.CalledProcessError:
        print "Error"
    finally:
        print "Finally"

    print a


if __name__ == "__main__":
    main()
