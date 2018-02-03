#!/usr/bin/env python
from tkinter import *
import os
import sys
import socket
import time
from tkinter import messagebox
import random
from SimpleDialog import SimpleDialog
import pyperclip

# Instructions: Navigate to dir where file is saved. Enter into terminal: python pw-gen-gui.py
# Visit: http://youtube.com/user/postulatedstate For More!
# webmaster@botanicalguides.com & http://learnhtmlcode2.000webhostapp.com
global numeric, num, alphanumeric, generatred
global string
string=' '
os.system('clear')
print('Random Password Generator By Scott Hermann http://YouTube.com/user/postulatedstate')
print('')


class App:
  def __init__(self, master):


    frame = Frame(master)
    frame.pack()
    frame.configure(background="#000000") # bam
    Label(root, text=" ", bg="#000000", fg="#9440ED", font="none 18").pack()

    self.button = Button(frame, 
                         text="QUIT", bg="#000000", fg="#9440ED", font="none 18",
                         command=quit)
    self.button.pack(side=BOTTOM)
#
    self.button = Button(frame, 
                         text="Generate Random Password!", bg="#000000", fg="#FFFFFF", font="none 18",
                         command=self.gen_pw)
    self.button.pack(side=BOTTOM)
#





  



  

  def get_iton(self):
    time.sleep(.5)
    #messagebox.showinfo("Success!", "watch out now " + list[5] + "" + "yezir" )
    #sample function


  def edit_settings(self):
        
    os.system("x-terminal-emulator -e echo how to open a new terminal window kids")
    
  def ready(self):
	print('add function')

  def gen_pw(self):
	numeric=[]
	for x in range(20):
  	 num=random.randint(1,9)
  	 numeric.append(num)

	generated=[]

	alphanumeric=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "[", "{", "]", "}", ":", ";", " ", "<", ",", ">", ".", "/", "?"]


	for y in range(10):
  	#print(y)
  	   rndalpha=random.randint(1,78)
  	   tmptwo=(alphanumeric[rndalpha])
   	   rndnum=(numeric[y])
   	   generated.append(tmptwo)
   	   generated.append(rndnum)
        global string
	string=' '
	print('')
	print('Generated password:')
	print(generated)
	print('')
	os.system('rm password.gen')
	with open('password.gen', 'a') as fkey:
	   for lines in generated:
	    fkey.write(str(lines))
	    string=string+str(lines)
	print('')
	os.system('cat password.gen')
	print('')
	pyperclip.copy(str(string))
	messagebox.showinfo("Password: ", " " + str(string) + " " + "  copied to clipboard!" )

  def nother_funct(self):

    emptyness=true


  def func_tion(pw):

	#forever =1;
	Label(root, text=pw, bg="#000000", fg="#9440ED", font="none 18").pack()




# **************** Software Default GUI Window Settings ******************


root = Tk()

root.title('Secure Random Password Generator!')
root.configure(background="#000000") # #fffadd worx

root.geometry('480x230')

app = App(root)



Label(root, text="Secure Random Password Generator!", bg="#000000", fg="#FFFF00", font="none 18").pack()
Label(root, text="Coded by: Scott Hermann", bg="#000000", fg="#01DF01", font="none 18").pack()
Label(root, text="YouTube.com/user/postulatedstate", bg="#000000", fg="#2ECCFA", font="none 18").pack()

root.mainloop()
