#!/usr/bin/python3
# -*- coding: latin-1 -*-
import os, sys


R = 255
G = 0
B = 0

def change_color(r, g, b):
    global R, G, B
    if(r == 255 and g < 255):
        G += 1
    elif(r > 0 and g == 255):
        R -= 1
    elif(r == 0 and g == 255 and b < 255):
        B += 1
    elif(r == 0 and g > 0 and b == 255):
        G -= 1
    elif(r < 255 and g == 0 and b == 255):
        R += 1

with open('duha.ppm', 'w') as soubor:
    soubor.write("P3" + '\n')
    soubor.write("1276 100" + '\n')
    soubor.write("255" + '\n')
    for x in range(100):
        for y in range(1276):
            print(str(R) + '\t' + str(G) + '\t' + str(B))
            soubor.write(str(R) + ' ' + str(G) + ' ' + str(B) + '\n')
            change_color(R, G, B)
        R = 255
        G = 0
        B = 0