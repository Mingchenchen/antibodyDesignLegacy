#!/usr/bin/python
import blosum62

file = open("testfileforidentity.txt", "r")
lines = file.readlines()
count = 1
score = 0
index = 0

for f in lines :
		if(count == 1) :
			arra1 = list(f)
		if(count == 2) :
			arra2 = list(f)
		count += 1


for n in range(16):

	for x in range(index, len(arra2)-1) :
			score += blosum62.score(arra1[x], arra2[x])
	print "Score : ", score
	print "".join(arra1).rstrip("\n")
	print "".join(arra2)
	score = 0
	index += 1
	arra2.insert(0, " ")
