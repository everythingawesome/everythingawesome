#!/usr/bin/env python
# Coded and designed by Scott Hermann scotthermann850@gmail.com youtube.com/user/postulaetdstate

import random

dict={"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52, "!":53, "@":54, "#":55, "$":56, "%":57, "^":58, "&":59, "*":60, "(":61, ")":62, "_":63, "-":64, "+":65, "'":66, "=":67, "[":68, "{":69, "]":70, "}":71, ":":72, ";":73, " ":74, "<":75, ",":76, ">":77, ".":78, "/":79, "?":80, "'\'":81, "|":82}

dictlen=len(dict)
print(dictlen)
code=[]
for x in range(dictlen):
   num=random.randint(1,1000)
   code.append(num)


newkey=[]
counter=0;
alphacnt=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "'", "=", "[", "{", "]", "}", ":", ";", " ", "<", ",", ">", ".", "/", "?", "'\'", "|"]
alplen=len(alphacnt)
print(alplen)
gth=len(dict)
gth=gth-1
for x in range(0,1,83):
   for y in alphacnt:
      temp=(dict[y]*code[counter])
      newkey.append(temp)
      counter=counter+1
print(newkey)
with open('encryption-key.dat', 'a') as fkey:
   for lines in newkey:
    fkey.write(str(lines)+ '')
    fkey.write('\n')
with open('encryption-key.dat', 'r') as fread:
   for read in fread:
	print(read)

