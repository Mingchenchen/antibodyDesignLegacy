#!/usr/bin/python
for count in range(1,43):
	for i in range(1, 8):
		print "/nas1/apps/mslib/current/bin/insertLoopIntoTemplate_dwk --template FRH2-"+str(i)+".pdb --fragment H3_"+str(count)+"-aligned.pdb"
		j = i + (7*(count-1))
		print "mv FRH2-"+str(i)+"_H3_"+str(count)+"-aligned.pdb FRH2H3-"+str(j)+".pdb"

