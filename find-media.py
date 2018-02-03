#!/usr/bin/env python
# By Scott Hermann youtube.com/user/postulatedstate webmaster@botanicalguides.com
# http://learnhtmlcode2.000webhostapp.com
import os
import sys
os.system('rm dump.dat')
os.system('lsblk | grep sd | cut -f1-2 -d" " > dump.dat')
with open('dump.dat','r') as f:
  for data in f:
   l=list(data)
   # convert data to list->l
   l[1:3] = ""
   # remove non-ascii chars from list l [1-3]
   print(l[4:8])
   # echo to screen. now remove what we don't need
   dev=l[4:8]
   # now convert to standard string
   device=""
   for char in dev:
    device+=char
   print(device)
   os.system('cd .. && cd .. && cd .. && cd /media && mkdir '+ device)
   # plug strings to terminal commands ( create dir's to mount )
   os.system('mount /dev/'+device+' /media/'+device)
   # mount each device to each dir. 
   # now device = device
# all media devices mounted. all partitions and usb devices.

