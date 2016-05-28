#!/usr/bin/python

f0 = open("list", "r")
line = f0.readlines()
for t in line :
	name = str(t).strip()+"/cpep_3ztn_"+str(t).strip()+"_backrub.sh"
	f1 = open(name, "r")
	lines = f1.readlines()
	count = 0
	temp2 = ""
	for i in lines:
		count += 1
		if count == 5:
			temp = i.split()[12:]
			for k in range(1, 325):
				if str(k) not in temp:
					temp2 = temp2 + str(k) + " "

	outname = "cpep_3ztn_"+str(t).strip()+"_cluster.sh"
	fout =  open(outname, "w")
	fout.write ("cluster.linuxgccrelease -in:file:silent silent"+str(t).strip()+".out -cluster:radius 0.5 -cluster:sort_groups_by_energy -in::file::fullatom -exclude_res " + temp2)
