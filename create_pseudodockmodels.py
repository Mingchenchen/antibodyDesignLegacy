#!/usr/bin/python

f1 = open("script.txt", "w")

counter = 1
degree = 0

f1.write("run save_transformed.py\n") 
for i in range(1,11):
	counter += 1
	degree += 3
	f1.write("create dock1, cpep_3eff_start\norient dock1 and chain C and resi 634-660\norigin position=[27.379, 39.368, 14.274]\ncenter origin\nrotate z,90, dock1\nrotate y," + str(degree) + ",dock1 and chain C\nsave_transformed dock1, test" + str(counter) + ".pdb\ndelete dock1\n")

degree = 0

for i in range(1,11):
	counter += 1
	degree -= 3
	f1.write("create dock1, cpep_3eff_start\norient dock1 and chain C and resi 634-660\norigin position=[27.379, 39.368, 14.274]\ncenter origin\nrotate z,90, dock1\nrotate y," + str(degree) + ",dock1 and chain C\nsave_transformed dock1, test" + str(counter) + ".pdb\ndelete dock1\n")

for i in range(1,22):
	f1.write("load test" + str(i) + ".pdb\n")

counter = 0
dist = 0

for i in range(1,22):
	dist = 0
	for k in range(1,21):
		counter += 1
		dist += 0.5
		name = "test" + str(i)
		f1.write("create dock1, " + name  + "\norient dock1 and chain C and resi 634-657\nrotate z,90, dock1 \ntranslate [0,-" + str(dist) + ",0], dock1 and chain C \nsave_transformed dock1, model" + str(counter) + ".pdb\ndelete dock1\n")
