#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:24:47 2020

@author: wang1278
"""

def draw_row2x2():
    print('+ - - - - + - - - - +')
def draw_col2x2():
    print('|         |         |')
# I noticed that I need to repeat the draw_col2x2() 4 times in between each draw_row2x2() so I took the do_four() function from 3.2
def do_four(f):
    f()
    f()
    f()
    f()
def draw_2x2():
    draw_row2x2()
    do_four(draw_col2x2)
    draw_row2x2()
    do_four(draw_col2x2)
    draw_row2x2()

draw_2x2()

def draw_row4x4():
    print('+ - - - - + - - - - + - - - - + - - - - +')
def draw_col4x4():
    print('|         |         |         |         |')
# I noticed that I need to repeat the whole thing by 4 times so I tossed them into one function for use in the do_four()
def draw_layer4x4():
    draw_row4x4()
    do_four(draw_col4x4)
def draw_4x4():
    do_four(draw_layer4x4)
    draw_row4x4()
draw_4x4()