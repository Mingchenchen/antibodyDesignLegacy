#!/usr/bin/python
f1 = open("temp.txt" , "r")
lines = f1.readlines()

count = 0
for i in lines:
	print i.strip()
	count += 1
	if count == 2000 :
		break
