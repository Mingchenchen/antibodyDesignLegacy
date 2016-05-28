#!/usr/bin/python

pdb = open("pdb_list", "r")
for w in pdb:
	x =  w.strip('\n')
	file = open(x, "r")
	for i in file :
		if i[0:5] == "HELIX" :
			try:
				if int(i.split()[8]) - int(i.split()[5]) > 7 :
					print x, i.split()[4], i.split()[5], i.split()[8]
								
			except Exception:
				pass
