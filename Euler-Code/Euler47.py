#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:11:53 2019

@author: albertlu
"""
def factorize(n):
    k = n
    s = set()
    p = 2
    while k>=p*p:
        if k%p == 0:
            s.add(p)
            k = k/p
        else:
            p = p+1
    s.add(k)
    return s
for i in range(3, 1000000):
    if len(factorize(i)) == 4:
        if len(factorize (i+1)) == 4:
            if len(factorize(i+2)) == 4:
                if len(factorize(i+3)) == 4:
                    print(i)
                    break
                

