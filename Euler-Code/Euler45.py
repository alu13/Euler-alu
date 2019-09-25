#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 00:16:47 2019

@author: albertlu
"""
import math
def is_pentagonal(n):
    k = (math.sqrt(24*n+1)+1)/6
    return k.is_integer()
for i in range(0, 150000):
    hexagon = i*(2*i-1)
    if is_pentagonal(hexagon):
        print(hexagon)
