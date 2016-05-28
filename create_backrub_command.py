#!/usr/bin/python

file1 = open("cpep_3ztn_heavy-align.txt", "r")
lines = file1.readlines()

small_res = ["G", "S", "P", "A"]

######## pivot residue identification for H2 ###########

count = 0
seq = ""

for i in lines:
	name = i.split()[2][0:-4]+"_backrub.sh"
	folder = i.split()[2][10:-4]
	file2 = open(name, "w")
	file2.write("#PBS -j oe \n#PBS -o /nas1/home/ssbhatta/cdr_graft/cpep_3ztn_models/fixbb/"+ folder + "/run.log \ncd /nas1/home/ssbhatta/cdr_graft/cpep_3ztn_models/fixbb/" + folder + "\n\n")
	file2.write("/nas1/apps/rosetta/current/source/bin/backrub.linuxgccrelease -s " + i.split()[2] + " -resfile ../resfile_basic.txt ")
	file2.write("-database /nas1/apps/rosetta/current/database -nstruct 500 -out:file:silent silent"+folder+".out -pivot_residues ")
	temp = i[67]+i[68]
	temp2 = i[69]+i[70]
	temp3 = i[66]+i[67]
	for j in range(50, 66):
		file2.write(str(j+int(i.split()[0]))+" ")
	if(temp == "KG"):
		file2.write(str(66 +int(i.split()[0]) )+" ")
	#	file2.write(str(67 +int(i.split()[0]) )+" ")
		count +=1
	if(temp2 == "KG"):
		file2.write(str(66+int(i.split()[0]) )+" ")
		file2.write(str(67+int(i.split()[0]) )+" ")
		file2.write(str(68+int(i.split()[0]) )+" ")
		count +=1
	if(temp3 == "KS"):
	#	file2.write(str(66+int(i.split()[0]) )+" ")
		count +=1

print count

file2.close()
############ Done ###############

####### Appending H3 mutations to resfile ##########

count4 = 0
seq = ""
switch = 0
j = 0

for i in lines:
	if i[100] == "C":
		switch = 1
		j = 101
	if i[97] == "C":
		switch = 1
		j = 98
	if i[98] == "C":
		switch = 1
		j = 99

	name = i.split()[2][0:-4]+"_backrub.sh"
	file2 = open(name, "a")

	for k in range(j, 130):
		if(switch == 1):
			seq = seq + str(k + int(i.split()[0]))+" "
		if(i[k]+i[k+1] == "WG"):
			temp = seq.split()	
			file2.write(" ".join(temp[0:-3]) + " ")
			seq = ""
			count4 += 1
			switch = 0
			break

file1.close()
print count4





####### Appending L1 mutations to resfile ##########

file1 = open("cpep_3ztn_light-align.txt", "r")
lines = file1.readlines()
end_res_L1 = ["WY", "WF"]

count2 = 0
seq = ""

for i in lines:
	name = i.split()[2][0:-4]+"_backrub.sh"
	file2 = open(name, "a")
	for k in range(22,200):
		seq = seq+" "+str(k+ 2 + int(i.split()[0]))
		if(i[k]+i[k+1] in end_res_L1 ):
			#print i[k]+i[k+1]
			count2 += 1
			break
	
	temp = seq.split()
	file2.write(" ".join(temp[0:-6])+" ")
	seq = ""
print count2
file2.close()
############ Done ###############

####### Appending L3 mutations to resfile ##########

start_res_L3 = ["YYC", "YFC"]

count3 = 0
ini_seq = ""
switch = 0
seq = ""

for i in lines:
	name = i.split()[2][0:-4]+"_backrub.sh"
	file2 = open(name, "a")
	for k in range(80, 200):
		ini_seq = i[k]+i[k+1]+i[k+2]
		if(switch == 1): 
			seq = seq + str(k-1 + int(i.split()[0]))+" "
		if(ini_seq in start_res_L3):
			switch = 1
		if(i[k]+i[k+1] == "FG"):
			temp = seq.split()
			file2.write(" ".join(temp[0:-3])+" \n")
			seq = ""
			count3 += 1
			switch = 0
			break
print count3	

