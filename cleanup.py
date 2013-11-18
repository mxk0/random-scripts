'''
Takes files of specified type in the current directory, and checks to see if twelve hours 
have passed since the file was created. If so, the file is deleted.

Make sure to set the file_type variable to your targeted extension.
'''

import os
import sys
import time

file_type = "[insert file extension]"

files = filter(lambda x: x.endswith(file_type),os.listdir("."))
if len(files) == 0:
	print("No " + file_type + "s in this dir!")
	sys.exit(1)
for one_file in files:
	if (os.path.getctime(one_file) + 43200) < time.time():
		os.remove(one_file)