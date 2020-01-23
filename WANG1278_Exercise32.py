#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:07:02 2020

@author: wang1278
"""
# Defining required functions
def do_twice(f,v):
    f(v)
    f(v)
def print_spam():
    print('spam')
def print_twice(v):
    print(v)
    print(v)
# Testing the functions, note that there should be a total of 2x2+4x2=12 "spam" beeing printed.
do_twice(print_twice,'spam')

def do_four(f,v):
    do_twice(f,v)
    do_twice(f,v)

do_four(print_twice,'spam')