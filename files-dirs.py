#!/usr/bin/env python
# youtube.com/user/postulatedstate http://learnhtmlcode2.000webhostapp.com 
# Scott Hermann webmaster@botanicalguides.com
import re
import os 
import time
# nuitka --standalone --recurse-on --python-version=2.7 sample-compile.py
# supply folder name, walk through its directory tree
# echo folders and files within each folder
# search for file extensions or strings

direct=raw_input("Enter directory to begin search: ")
ext=raw_input("Enter file extensions to search for or string: ")

def recursive_walk(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                recursive_walk(subfolder)
        print('\nFolder: ' + folderName + '\n')
	#time.sleep(3)
        for filename in filenames:
            print(filename + '\n')
	    if re.search(ext, filename):#{
		os.system('rm /root/Desktop/py/list.lst')
		os.system('echo ' + filename + ' >> /root/Desktop/py/list.lst')
		print('Search findings below:')
		os.system('cat /root/Desktop/py/list.lst')
recursive_walk(direct)


