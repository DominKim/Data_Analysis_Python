#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:19:03 2020

@author: mac
"""

PI = 3.141592

def number_input():
    output = input("숫자입력")
    return float(output)

def get_cirumference(radius):
    return 2 * PI * radius

def get_circle_area(radius):
    return PI * radius * radius