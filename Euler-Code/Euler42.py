# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Tlist = [1]
for i in range(0, 100):
    Tlist.append(0.5*i*(i+1))
    
text_file = open("words.txt", "r")
alphabet = ["\"", "A", "B", "C", "D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
lines = text_file.read().split(',')
supertotal = 0
for i in lines:
    total = 0
    for k in range(0, len(i)):
        total += alphabet.index(i[k])
    if total in Tlist:
        supertotal+=1
print(lines)
print(len(lines))
text_file.close()
print(supertotal)