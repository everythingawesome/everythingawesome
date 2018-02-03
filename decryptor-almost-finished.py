#!/usr/bin/env python
# Coded & Designed By Scott Hermann; 
# webmaster@botanicalguides.com; YouTube.com/user/postulaetdstate 
# StonedAimUser @ AIM PHEONIX
import time
from collections import OrderedDict


# encryption[z] == y[z]; if encrtyp[z]==line, then line==y[z]
encrypted=[]

y=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "'", "=", "[", "{", "]", "}", ":", ";", " ", "<", ",", ">", ".", "/", "?", "'\''", "|"]


encrypted=[''] # had \n added, removed it.
# encrypted[0]=a; 1=b; 2=c; 3=d; etc.
count=0;
with open("encryption-key.dat", "r") as e:
   for read in e:
     count+=1 # odd[0] = 1            
     encrypted.append(read)
     # appends e/a # from encryption file to list encrypted.
     count=count+1

print('')
print('ASCII Key Loading:')
print('')
print(encrypted)
print('')
rng=len(encrypted)
print(len(encrypted))
print('')
for r in range(rng):
  encrypted[r] = encrypted[r].replace("\n", "")
print(encrypted)

print('')
print('ASCII Key Loading:')
print('')
print(encrypted)
print('')
# encryption key loaded to list
# determine the length of the encrypted message
templencounter=[]
tempcounter=0;
with open("encrypted.msg", "r") as e:
  for read in e:
     templencounter.append(read)

outputlen=len(templencounter)
print(outputlen)

print('# encryption[z] == y[z]; if encrtyp[z]==line, then line==y[z]')
# ======================================================================
# note: encrypted file must have numbers on separate lins with no spaces
# ======================================================================
nfile=raw_input('Enter path to encrypted file: ')
def slashn():
	print(' ')
	
def a():
	print('a')
	with open('decrypted.msg', "a") as d:
 	 d.write('a')
  	 d.close()
def b():
	print('b')
	with open('decrypted.msg', "a") as d:
 	 d.write('b')
  	 d.close()

def c():
	print('c')
	with open('decrypted.msg', "a") as d:
 	 d.write('c')
  	 d.close()
def d():
	print('d')
	with open('decrypted.msg', "a") as d:
 	 d.write('d')
  	 d.close()
def e():
	print('e')
	with open('decrypted.msg', "a") as d:
 	 d.write('e')
  	 d.close()
def f():
	print('f')
	with open('decrypted.msg', "a") as d:
 	 d.write('f')
  	 d.close()
def g():
	print('g')
	with open('decrypted.msg', "a") as d:
 	 d.write('g')
  	 d.close()
def h():
	print('h')
	with open('decrypted.msg', "a") as d:
	  d.write('h')
	  d.close()
def i():
	print('i')
	with open('decrypted.msg', "a") as d:
 	 d.write('i')
  	 d.close()
def j():
	print('j')
	with open('decrypted.msg', "a") as d:
 	 d.write('j')
  	 d.close()
def k():
	print('k')
	with open('decrypted.msg', "a") as d:
 	 d.write('k')
  	 d.close()
def l():
	print('l')
	with open('decrypted.msg', "a") as d:
 	 d.write('l')
  	 d.close()
def m():
	print('m')
	with open('decrypted.msg', "a") as d:
 	 d.write('m')
  	 d.close()
def n():
	print('n')
	with open('decrypted.msg', "a") as d:
 	 d.write('n')
  	 d.close()
def o():
	print('o')
	with open('decrypted.msg', "a") as d:
 	 d.write('o')
  	 d.close()
def p():
	print('p')
	with open('decrypted.msg', "a") as d:
 	 d.write('p')
  	 d.close()
def q():
	print('q')
	with open('decrypted.msg', "a") as d:
 	 d.write('q')
  	 d.close()
def r():
	print('r')
	with open('decrypted.msg', "a") as d:
 	 d.write('r')
  	 d.close()
def s():
	print('s')
	with open('decrypted.msg', "a") as d:
 	 d.write('s')
  	 d.close()
def t():
	print('t')
	with open('decrypted.msg', "a") as d:
 	 d.write('t')
  	 d.close()
def u():
	print('u')
	with open('decrypted.msg', "a") as d:
 	 d.write('u')
  	 d.close()
def v():
	print('v')
	with open('decrypted.msg', "a") as d:
 	 d.write('v')
  	 d.close()
def w():
	print('w')
	with open('decrypted.msg', "a") as d:
 	 d.write('w')
  	 d.close()
def x():
	print('x')
	with open('decrypted.msg', "a") as d:
 	 d.write('x')
  	 d.close()
def y():
	print('y')
	with open('decrypted.msg', "a") as d:
 	 d.write('y')
  	 d.close()
def z():
	print('z')
	with open('decrypted.msg', "a") as d:
 	 d.write('z')
  	 d.close()

def CA():
	print('A')
	with open('decrypted.msg', "a") as d:
 	 d.write('A')
  	 d.close()
def CB():
	print('B')
	with open('decrypted.msg', "a") as d:
 	 d.write('B')
  	 d.close()
def CC():
	print('C')
	with open('decrypted.msg', "a") as d:
 	 d.write('C')
  	 d.close()
def CD():
	print('D')
	with open('decrypted.msg', "a") as d:
 	 d.write('D')
  	 d.close()
def CE():
	print('E')
	with open('decrypted.msg', "a") as d:
 	 d.write('E')
  	 d.close()
def CF():
	print('F')
	with open('decrypted.msg', "a") as d:
 	 d.write('F')
  	 d.close()
def CG():
	print('G')
	with open('decrypted.msg', "a") as d:
 	 d.write('G')
  	 d.close()
def CH():
	print('H')
	with open('decrypted.msg', "a") as d:
 	 d.write('H')
  	 d.close()
def CI():
	print('I')
	with open('decrypted.msg', "a") as d:
 	 d.write('I')
  	 d.close()
def CJ():
	print('J')
	with open('decrypted.msg', "a") as d:
 	 d.write('J')
  	 d.close()
def CK():
	print('K')
	with open('decrypted.msg', "a") as d:
 	 d.write('K')
  	 d.close()
def CL():
	print('L')
	with open('decrypted.msg', "a") as d:
 	 d.write('L')
  	 d.close()
def CM():
	print('M')
	with open('decrypted.msg', "a") as d:
 	 d.write('M')
  	 d.close()
def CN():
	print('N')
	with open('decrypted.msg', "a") as d:
 	 d.write('N')
  	 d.close()
def CO():
	print('O')
	with open('decrypted.msg', "a") as d:
 	 d.write('O')
  	 d.close()
def CP():
	print('P')
	with open('decrypted.msg', "a") as d:
 	 d.write('P')
  	 d.close()
def CQ():
	print('Q')
	with open('decrypted.msg', "a") as d:
 	 d.write('Q')
  	 d.close()
def CR():
	print('R')
	with open('decrypted.msg', "a") as d:
 	 d.write('R')
  	 d.close()
def CS():
	print('S')
	with open('decrypted.msg', "a") as d:
 	 d.write('z')
  	 d.close()
def CT():
	print('T')
	with open('decrypted.msg', "a") as d:
 	 d.write('T')
  	 d.close()
def CU():
	print('U')
	with open('decrypted.msg', "a") as d:
 	 d.write('U')
  	 d.close()
def CV():
	print('V')
	with open('decrypted.msg', "a") as d:
 	 d.write('V')
  	 d.close()
def CW():
	print('W')
	with open('decrypted.msg', "a") as d:
 	 d.write('W')
  	 d.close()
def CX():
	print('X')
	with open('decrypted.msg', "a") as d:
 	 d.write('X')
  	 d.close()
def CY():
	print('Y')
	with open('decrypted.msg', "a") as d:
 	 d.write('Y')
  	 d.close()
def CZ():
	print('Z')
	with open('decrypted.msg', "a") as d:
 	 d.write('Z')
  	 d.close()

def symbol_one():
	print('!')
	with open('decrypted.msg', "a") as d:
 	 d.write('!')
  	 d.close()
def symbol_two():
	print('@')
	with open('decrypted.msg', "a") as d:
 	 d.write('@')
  	 d.close()
def symbol_three():
	print('#')
	with open('decrypted.msg', "a") as d:
 	 d.write('#')
  	 d.close()
def symbol_four():
	print('$')
	with open('decrypted.msg', "a") as d:
	 d.write('$')
	 d.close()
def symbol_five():
	print('%')
	with open('decrypted.msg', "a") as d:
	 d.write('%')
	 d.close()
def symbol_six():
	print('^')
	with open('decrypted.msg', "a") as d:
	 d.write('^')
	 d.close()
def symbol_seven():
	print('&')
	with open('decrypted.msg', "a") as d:
	 d.write('&')
	 d.close()
def symbol_eight():
	print('*')
	with open('decrypted.msg', "a") as d:
	 d.write('*')
	 d.close()
def symbol_nine():
	print('(')
	with open('decrypted.msg', "a") as d:
	 d.write('(')
	 d.close()
def symbol_ten():
	print(')')
	with open('decrypted.msg', "a") as d:
	 d.write(')')
	 d.close()
def symbol_eleven():
	print('_')
	with open('decrypted.msg', "a") as d:
	 d.write('_')
	 d.close()
def symbol_twelve():
	print('-')
	with open('decrypted.msg', "a") as d:
	 d.write('-')
	 d.close()
def symbol_thirteen():
	print('+')
	with open('decrypted.msg', "a") as d:
	 d.write('+')
	 d.close()
def symbol_fourteen():
	print("'")
	with open('decrypted.msg', "a") as d:
	 d.write("'")
	 d.close()
def symbol_fif():
	print('=')
	with open('decrypted.msg', "a") as d:
	 d.write('=')
	 d.close()
def symbol_sixt():
	print('[')
	with open('decrypted.msg', "a") as d:
	 d.write('[')
	 d.close()
def symbol_sevente():
	print(']')
	with open('decrypted.msg', "a") as d:
	 d.write(']')
	 d.close()
def symbol_eighteen():
	print('}')
	with open('decrypted.msg', "a") as d:
	 d.write('}*')
	 d.close()
def symbol_ninteen():
	print(':')
	with open('decrypted.msg', "a") as d:
	 d.write(':')
	 d.close()
def symbol_twenty():
	print(';')
	with open('decrypted.msg', "a") as d:
	 d.write(';')
	 d.close()
def symbol_twetwo():
	print(' ')
	with open('decrypted.msg', "a") as d:
	 d.write(' ')
	 d.close()
def symbol_twone():
	print('<')
	with open('decrypted.msg', "a") as d:
	 d.write('<')
	 d.close()

#?!#

def symbol_twthree():
	print(',')
	with open('decrypted.msg', "a") as d:
	 d.write(',')
	 d.close()
def symbol_twfour():
	print('>')
	with open('decrypted.msg', "a") as d:
	 d.write('>')
	 d.close()
def symbol_twfive():
	print('.')
	with open('decrypted.msg', "a") as d:
	 d.write('.')
	 d.close()
def symbol_twsix():
	print('/')
	with open('decrypted.msg', "a") as d:
	 d.write('/')
	 d.close()
# ? should be \ and \ should be ?
def symbol_tweight():
	print('?')
	with open('decrypted.msg', "a") as d:
	 d.write('?')
	 d.close()
def symbol_twseven():
	print('\ ')
	with open('decrypted.msg', "a") as d:
	 d.write('\ ')
	 d.close()
def symbol_twnine():
	print('|')
	with open('decrypted.msg', "a") as d:
	 d.write(''|'')
	 d.close()
print('')

print('Key: ')
print(encrypted)
print('')
decrypt_or = { encrypted[0] : slashn,
	       encrypted[1] : a,
	       encrypted[2] : b,
               encrypted[3] : c,
	       encrypted[4] : d,
	       encrypted[5] : e,
	       encrypted[6] : f,
	       encrypted[7] : g,
	       encrypted[8] : h,
	       encrypted[9] : i,
	       encrypted[10] : j,
	       encrypted[11] : k,
	       encrypted[12] : l,
               encrypted[13] : m,
	       encrypted[14] : n,
	       encrypted[15] : o,
	       encrypted[16] : p,
	       encrypted[17] : q,
	       encrypted[18] : r,
	       encrypted[19] : s,
	       encrypted[20] : t,
	       encrypted[21] : u,
	       encrypted[22] : v,
	       encrypted[23] : w,
	       encrypted[24] : x,
	       encrypted[25] : y,
	       encrypted[26] : z,
	       encrypted[27] : CA,
	       encrypted[28] : CB,
	       encrypted[29] : CC,
	       encrypted[30] : CD,
	       encrypted[31] : CE,
	       encrypted[32] : CF,
	       encrypted[33] : CG,
	       encrypted[34] : CH,
	       encrypted[35] : CI,
	       encrypted[36] : CJ,
	       encrypted[37] : CK,
	       encrypted[38] : CL,
	       encrypted[39] : CM,
	       encrypted[40] : CN,
	       encrypted[41] : CO,
	       encrypted[42] : CP,
	       encrypted[43] : CQ,
	       encrypted[44] : CR,
	       encrypted[45] : CS,
	       encrypted[46] : CT,
	       encrypted[47] : CU,
	       encrypted[48] : CV,
	       encrypted[49] : CW,
	       encrypted[50] : CX,
	       encrypted[51] : CY,
	       encrypted[52] : CZ,
	       encrypted[53] : symbol_one,
	       encrypted[54] : symbol_two,
	       encrypted[55] : symbol_three,
	       encrypted[56] : symbol_four,
	       encrypted[57] : symbol_five,
	       encrypted[58] : symbol_six,
	       encrypted[59] : symbol_seven,
	       encrypted[60] : symbol_eight,
	       encrypted[61] : symbol_nine,
	       encrypted[62] : symbol_ten,
	       encrypted[63] : symbol_eleven,
	       encrypted[64] : symbol_twelve,
	       encrypted[65] : symbol_thirteen,
	       encrypted[66] : symbol_fourteen,
	       encrypted[67] : symbol_fif,
	       encrypted[68] : symbol_sixt,
	       encrypted[69] : symbol_sevente,
	       encrypted[70] : symbol_eighteen,
	       encrypted[71] : symbol_ninteen,
	       encrypted[72] : symbol_twenty,
	       encrypted[73] : symbol_twone,
	       encrypted[74] : symbol_twetwo,
	       encrypted[75] : symbol_twthree,
	       encrypted[76] : symbol_twfour,
	       encrypted[77] : symbol_twfive,
	       encrypted[78] : symbol_twsix,
	       encrypted[79] : symbol_twseven,
	       encrypted[80] : symbol_tweight,
	       encrypted[81] : symbol_twnine
	      }

# msg+=msg. will take message and group it on a single line instead of having it one
# letter on a separate line. remember spaces and special characters. may be a bug with empty lines etc

def go():
 with open(nfile, "r") as e:
   for read in e:
     #original = "EXAMPLE"
     removed = read.replace("\n", "")
     decrypt_or[removed]() # change removed to read to change back
     # executes decryptor dict as function. calls a, b , c etc and echoes results to file.

go()

# # encryption[z] == y[z]; if encrtyp[z]==line, then line==y[z]

#decrypt=raw_input("text to decrypt: ")
#print(dict[decrypt])
# new idea 
