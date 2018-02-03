#!/usr/bin/env python
# By Scott Hermann http://youtube.com/user/postulatedstate http://learnhtmlcode2.000webhostapp.com
encrypted=[]
# y[0]=a; 1=b; 2=c; 3=d; etc.
count=0;
with open("encryption-key.dat", "r") as e:
   for read in e:
     count+=1 # odd[0] = 1            
     encrypted.append(read)
     # appends e/a # from encryption file to list y.
     count=count+1

print('')
print('ASCII Key Loading:')
print('')
print(encrypted)
print('')


print('')
for r in range(80):
  encrypted[r] = encrypted[r].replace("\n", "")
print(encrypted)

print('')
print('ASCII Key Loading:')
print('')
print(encrypted)
print('')
# encryption key loaded to list


var=raw_input('enter msg: ');
for char in var:
 print(char)
 print('')

yy=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "'", "=", "[", "{", "]", "}", ":", ";", " ", "<", ",", ">", ".", "/", "?", "'\''", "|"]

nFile=raw_input("Enter encrypted file path/name: ");

def a():
	print('@ a')
	with open(nFile, 'a') as e:
	 e.write(encrypted[0])
	 e.write('\n')
	 e.close()
def b():
	print('@ b')
	with open(nFile, 'a') as e:
	 e.write(encrypted[1])
	 e.write('\n')
	 e.close()
def c():
	print('@ c')
	with open(nFile, 'a') as e:
	 e.write(encrypted[2])
	 e.write('\n')
	 e.close()
def d():
	print('@ d')
	with open(nFile, 'a') as e:
	 e.write(encrypted[3])
	 e.write('\n')
	 e.close()
def e():
	print('@ e')
	with open(nFile, 'a') as e:
	 e.write(encrypted[4])
	 e.write('\n')
	 e.close()
def f():
	print('@ f')
	with open(nFile, 'a') as e:
	 e.write(encrypted[5])
	 e.write('\n')
	 e.close()
def g():
	print('@ g')
	with open(nFile, 'a') as e:
	 e.write(encrypted[6])
	 e.write('\n')
	 e.close()
def h():
	print('@ h')
	with open(nFile, 'a') as e:
	 e.write(encrypted[7])
	 e.write('\n')
	 e.close()
def i():
	print('@ i')
	with open(nFile, 'a') as e:
	 e.write(encrypted[8])
	 e.write('\n')
	 e.close()
def j():
	print('@ k')
	with open(nFile, 'a') as e:
	 e.write(encrypted[9])
	 e.write('\n')
	 e.close()
def k():
	print('@ k')
	with open(nFile, 'a') as e:
	 e.write(encrypted[10])
	 e.write('\n')
	 e.close()
def l():
	print('@ l')
	with open(nFile, 'a') as e:
	 e.write(encrypted[11])
	 e.write('\n')
	 e.close()
def m():
	print('@ m')
	with open(nFile, 'a') as e:
	 e.write(encrypted[12])
	 e.write('\n')
	 e.close()
def n():
	print('@ n')
	with open(nFile, 'a') as e:
	 e.write(encrypted[13])
	 e.write('\n')
	 e.close()
def o():
	print('@ o')
	with open(nFile, 'a') as e:
	 e.write(encrypted[14])
	 e.write('\n')
	 e.close()
def p():
	print('@ p')
	with open(nFile, 'a') as e:
	 e.write(encrypted[15])
	 e.write('\n')
	 e.close()
def q():
	print('@ q')
	with open(nFile, 'a') as e:
	 e.write(encrypted[16])
	 e.write('\n')
	 e.close()
def r():
	print('@ r')
	with open(nFile, 'a') as e:
	 e.write(encrypted[17])
	 e.write('\n')
	 e.close()
def s():
	print('@ s')
	with open(nFile, 'a') as e:
	 e.write(encrypted[18])
	 e.write('\n')
	 e.close()
def t():
	print('@ t')
	with open(nFile, 'a') as e:
	 e.write(encrypted[19])
	 e.write('\n')
	 e.close()
def u():
	print('@ u')
	with open(nFile, 'a') as e:
	 e.write(encrypted[20])
	 e.write('\n')
	 e.close()
def v():
	print('@ v')
	with open(nFile, 'a') as e:
	 e.write(encrypted[21])
	 e.write('\n')
	 e.close()
def w():
	print('@ w')
	with open(nFile, 'a') as e:
	 e.write(encrypted[22])
	 e.write('\n')
	 e.close()
def x():
	print('@ x')
	with open(nFile, 'a') as e:
	 e.write(encrypted[23])
	 e.write('\n')
	 e.close()
# for some reason it messes up at y. a space added or something?
# I get it. because we have a list called y.... dur....
def why():
	print('@ y')
	with open(nFile, 'a') as e:
	 e.write(encrypted[24])
	 e.write('\n')
	 e.close()
def z():
	print('@ z')
	with open(nFile, 'a') as e:
	 e.write(encrypted[25])
	 e.write('\n')
	 e.close()
def CA():
	print('@ A')
	with open(nFile, 'a') as e:
	 e.write(encrypted[26])
	 e.write('\n')
	 e.close()
def CB():
	print('@ B')
	with open(nFile, 'a') as e:
	 e.write(encrypted[27])
	 e.write('\n')
	 e.close()
def CC():
	print('@ C')
	with open(nFile, 'a') as e:
	 e.write(encrypted[28])
	 e.write('\n')
	 e.close()
def CD():
	print('@ D')
	with open(nFile, 'a') as e:
	 e.write(encrypted[29])
	 e.write('\n')
	 e.close()
def CE():
	print('@ E')
	with open(nFile, 'a') as e:
	 e.write(encrypted[30])
	 e.write('\n')
	 e.close()
def CF():
	print('@ F')
	with open(nFile, 'a') as e:
	 e.write(encrypted[31])
	 e.write('\n')
	 e.close()
def CG():
	print('@ G')
	with open(nFile, 'a') as e:
	 e.write(encrypted[32])
	 e.write('\n')
	 e.close()
def CH():
	print('@ H')
	with open(nFile, 'a') as e:
	 e.write(encrypted[33])
	 e.write('\n')
	 e.close()
def CI():
	print('@ I')
	with open(nFile, 'a') as e:
	 e.write(encrypted[34])
	 e.write('\n')
	 e.close()
def CJ():
	print('@ J')
	with open(nFile, 'a') as e:
	 e.write(encrypted[35])
	 e.write('\n')
	 e.close()
def CK():
	print('@ K')
	with open(nFile, 'a') as e:
	 e.write(encrypted[36])
	 e.write('\n')
	 e.close()
def CL():
	print('@ L')
	with open(nFile, 'a') as e:
	 e.write(encrypted[37])
	 e.write('\n')
	 e.close()
def CM():
	print('@ M')
	with open(nFile, 'a') as e:
	 e.write(encrypted[38])
	 e.write('\n')
	 e.close()
def CN():
	print('@ N')
	with open(nFile, 'a') as e:
	 e.write(encrypted[39])
	 e.write('\n')
	 e.close()
def CO():
	print('@ O')
	with open(nFile, 'a') as e:
	 e.write(encrypted[40])
	 e.write('\n')
	 e.close()
def CP():
	print('@ P')
	with open(nFile, 'a') as e:
	 e.write(encrypted[41])
	 e.write('\n')
	 e.close()
def CQ():
	print('@ Q')
	with open(nFile, 'a') as e:
	 e.write(encrypted[42])
	 e.write('\n')
	 e.close()
def CR():
	print('@ R')
	with open(nFile, 'a') as e:
	 e.write(encrypted[43])
	 e.write('\n')
	 e.close()
def CS():
	print('@ S')
	with open(nFile, 'a') as e:
	 e.write(encrypted[44])
	 e.write('\n')
	 e.close()
def CT():
	print('@ T')
	with open(nFile, 'a') as e:
	 e.write(encrypted[45])
	 e.write('\n')
	 e.close()
def CU():
	print('@ U')
	with open(nFile, 'a') as e:
	 e.write(encrypted[46])
	 e.write('\n')
	 e.close()
def CV():
	print('@ V')
	with open(nFile, 'a') as e:
	 e.write(encrypted[47])
	 e.write('\n')
	 e.close()
def CW():
	print('@ W')
	with open(nFile, 'a') as e:
	 e.write(encrypted[48])
	 e.write('\n')
	 e.close()
def CX():
	print('@ X')
	with open(nFile, 'a') as e:
	 e.write(encrypted[49])
	 e.write('\n')
	 e.close()
def CY():
	print('@ Y')
	with open(nFile, 'a') as e:
	 e.write(encrypted[50])
	 e.write('\n')
	 e.close()
def CZ():
	print('@ Z')
	with open(nFile, 'a') as e:
	 e.write(encrypted[51])
	 e.write('\n')
	 e.close()

def escla():
	print('@ !')
	with open(nFile, 'a') as e:
	 e.write(encrypted[52])
	 e.write('\n')
	 e.close()
def at():
	print('@ @')
	with open(nFile, 'a') as e:
	 e.write(encrypted[53])
	 e.write('\n')
	 e.close()
def num():
	print('@ #')
	with open(nFile, 'a') as e:
	 e.write(encrypted[54])
	 e.write('\n')
	 e.close()
def dollar():
	print('@ $')
	with open(nFile, 'a') as e:
	 e.write(encrypted[55])
	 e.write('\n')
	 e.close()

def mod():
	print('@ %')
	with open(nFile, 'a') as e:
	 e.write(encrypted[56])
	 e.write('\n')
	 e.close()
def up():
	print('@ ^')
	with open(nFile, 'a') as e:
	 e.write(encrypted[57])
	 e.write('\n')
	 e.close()
def amp():
	print('@ &')
	with open(nFile, 'a') as e:
	 e.write(encrypted[58])
	 e.write('\n')
	 e.close()
def star():
	print('@ *')
	with open(nFile, 'a') as e:
	 e.write(encrypted[59])
	 e.write('\n')
	 e.close()

def rbrac():
	print('@ (')
	with open(nFile, 'a') as e:
	 e.write(encrypted[60])
	 e.write('\n')
	 e.close()
def lbrac():
	print('@ )')
	with open(nFile, 'a') as e:
	 e.write(encrypted[61])
	 e.write('\n')
	 e.close()
def und():
	print('@ _')
	with open(nFile, 'a') as e:
	 e.write(encrypted[62])
	 e.write('\n')
	 e.close()
def tak():
	print('@ -')
	with open(nFile, 'a') as e:
	 e.write(encrypted[63])
	 e.write('\n')
	 e.close()
def plus():
	print('@ +')
	with open(nFile, 'a') as e:
	 e.write(encrypted[64])
	 e.write('\n')
	 e.close()

def takt():
	print('@ left postraphe')
	with open(nFile, 'a') as e:
	 e.write(encrypted[65])
	 e.write('\n')
	 e.close()
def eq():
	print('@ =')
	with open(nFile, 'a') as e:
	 e.write(encrypted[66])
	 e.write('\n')
	 e.close()
def sbr():
	print('@ [')
	with open(nFile, 'a') as e:
	 e.write(encrypted[67])
	 e.write('\n')
	 e.close()

def curl():
	print('@ {')
	with open(nFile, 'a') as e:
	 e.write(encrypted[68])
	 e.write('\n')
	 e.close()
def sbl():
	print('@ ]')
	with open(nFile, 'a') as e:
	 e.write(encrypted[69])
	 e.write('\n')
	 e.close()
def curr():
	print('@ }')
	with open(nFile, 'a') as e:
	 e.write(encrypted[70])
	 e.write('\n')
	 e.close()
def colon():
	print('@ :')
	with open(nFile, 'a') as e:
	 e.write(encrypted[71])
	 e.write('\n')
	 e.close()

def semcolon():
	print('@ ;')
	with open(nFile, 'a') as e:
	 e.write(encrypted[72])
	 e.write('\n')
	 e.close()
def space():
	print('@ -space-')
	with open(nFile, 'a') as e:
	 e.write(encrypted[73])
	 e.write('\n')
	 e.close()
def lt():
	print('@ <')
	with open(nFile, 'a') as e:
	 e.write(encrypted[74])
	 e.write('\n')
	 e.close()
def coma():
	print('@ ,')
	with open(nFile, 'a') as e:
	 e.write(encrypted[75])
	 e.write('\n')
	 e.close()

def gt():
	print('@ >')
	with open(nFile, 'a') as e:
	 e.write(encrypted[76])
	 e.write('\n')
	 e.close()
def dot():
	print('@ .')
	with open(nFile, 'a') as e:
	 e.write(encrypted[77])
	 e.write('\n')
	 e.close()
def slf():
	print('@ /')
	with open(nFile, 'a') as e:
	 e.write(encrypted[78])
	 e.write('\n')
	 e.close()
def qm():
	print('@ ?')
	with open(nFile, 'a') as e:
	 e.write(encrypted[79])
	 e.write('\n')
	 e.close()

def osl():
	print('@ \'')
	with open(nFile, 'a') as e:
	 e.write(encrypted[80])
	 e.write('\n')
	 e.close()
def pipe():
	print('@ |')
	with open(nFile, 'a') as e:
	 e.write(encrypted[81])
	 e.write('\n')
	 e.close()


encrypt_or = { yy[0] : a,
	       yy[1] : b,
	       yy[2] : c,
	       yy[3] : d,
	       yy[4] : e,
	       yy[5] : f,
	       yy[6] : g,
	       yy[7] : h,
	       yy[8] : i,
	       yy[9] : j,
	       yy[10] : k,
	       yy[11] : l,
	       yy[12] : m,
	       yy[13] : n,
	       yy[14] : o,
	       yy[15] : p,
	       yy[16] : q,
	       yy[17] : r,
	       yy[18] : s,
	       yy[19] : t,
	       yy[20] : u,
	       yy[21] : v,
	       yy[22] : w,
	       yy[23] : x,
	       yy[24] : why,
	       yy[25] : z,
	       yy[26] : CA,
       	       yy[27] : CB,
	       yy[28] : CC,
	       yy[29] : CD,
	       yy[30] : CE,
	       yy[31] : CF,
	       yy[32] : CG,
	       yy[33] : CH,
	       yy[34] : CI,
	       yy[35] : CJ,
	       yy[36] : CK,
	       yy[37] : CL,
	       yy[38] : CM,
	       yy[39] : CN,
	       yy[40] : CO,
	       yy[41] : CP,
	       yy[42] : CQ,
	       yy[43] : CR,
	       yy[44] : CS,
	       yy[45] : CT,
	       yy[46] : CU,
	       yy[47] : CV,
	       yy[48] : CW,
	       yy[49] : CX,
	       yy[50] : CY,
	       yy[51] : CZ,
	       yy[52] : escla,
	       yy[53] : at,
	       yy[54] : num,
	       yy[55] : dollar,
	       yy[56] : mod,
	       yy[57] : up,
	       yy[58] : amp,
	       yy[59] : star,
	       yy[60] : rbrac,
	       yy[61] : lbrac,
	       yy[62] : und,
	       yy[63] : tak,
	       yy[64] : plus,
	       yy[65] : takt,
	       yy[66] : eq,
	       yy[67] : sbr,
	       yy[68] : curl,
	       yy[69] : sbl,
	       yy[70] : curr,
	       yy[71] : colon,
	       yy[72] : semcolon,
	       yy[73] : space,
	       yy[74] : lt,
	       yy[75] : coma,
	       yy[76] : gt,
	       yy[77] : dot,
	       yy[78] : slf,
	       yy[79] : qm,
	       yy[80] : osl,
	       yy[81] : pipe
	     }

def go():
 for char in var:
  encrypt_or[char]()

go()

