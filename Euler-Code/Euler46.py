#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:32:33 2019

@author: albertlu
"""
import math
def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
numOfSquares = 300
squares = []
for i in range(1, numOfSquares):
    squares.append(2*i**2)
rangeOfComps = 10000
for i in range(1, rangeOfComps, 2):
    works = True
    for k in range(numOfSquares-1):
        if isPrime(i-squares[k]):
            works = False
    if works and not isPrime(i):
        print(i)