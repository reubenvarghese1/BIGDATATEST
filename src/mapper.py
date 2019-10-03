#!/usr/bin/env python
 
import sys
import string
import csv
import os

inp=csv.reader(sys.stdin,delimiter=',')

for line in inp:
    
	key = line[2]
	try:
		value = float(line[12])
	except ValueError:
		continue

	print ('{0:s}\t{1:f}'.format(key,value))
