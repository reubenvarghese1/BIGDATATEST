#!/usr/bin/env python

import sys
import string
import os

curkey = None
amo = 0
count = 0
for line in sys.stdin:

	line = line.strip()

	key, amount = line.split('\t',1)
	try:
		amount = float(amount)
	except ValueError:
		continue

	if curkey == key:
		amo += amount
		count += 1

	else:
		if curkey:
			print ('{0}\t{1:.2f}, {2:.2f}'.format(curkey,round(amo,2),round(amo/count,2)))

		curkey = key	
		amo = amount
		count = 1
if curkey == key:
	print ('{0}\t{1:.2f}, {2:.2f}'.format(curkey,round(amo,2),round(amo/count,2)))
