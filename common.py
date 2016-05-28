#!/usr/bin/python
f1 = open("sorted_ddg.txt", "r")
lines1 = f1.readlines()
f2 = open("sorted_energy.txt", "r")
lines2 = f2.readlines()

common = set(lines1)&set(lines2)

for i in common:
	print i.strip()
