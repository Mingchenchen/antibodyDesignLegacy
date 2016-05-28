#!/usr/bin/python

def distance(pdb, position, chain, position2, chain2) :
	pdbfile = open(pdb, "r")
	lines = pdbfile.readlines()
	for w in lines :
		if w[0:4] == "ATOM" and w.split()[2] == "CA" and w.split()[5] == str(position) and w.split()[4] == chain :
			x = float(w.split()[6])
			y = float(w.split()[7])
			z = float(w.split()[8])

		if w[0:4] == "ATOM" and w.split()[2] == "CA" and w.split()[5] == str(position2) and w.split()[4] == chain2 :
			a = float(w.split()[6])
			b = float(w.split()[7])
			c = float(w.split()[8])

	sq_dist = (x-a)**2 + (y-b)**2 + (z-c)**2
	print sq_dist**0.5		
     
         #---------------------------------------------#

def find_near(pdb, position, position2, chain) : # Lists all residues within 8.5 ang and belonging to diff chain
	pdbfile = open(pdb, "r")                     # For A SINGLE RESIDUE, position2 is wanted position + 1
	lines = pdbfile.readlines()
	items = ["CA", "CB", "N", "C", "O"]
	L = []
	H = []
	P = []
	Q = []
	final_list1 = []
	final_list2 = []
	ab_chains = ["H", "L"]
	for n in range(position, position2):
		for w in lines :
			if w[0:4] == "ATOM" and w.split()[2] in items and w.split()[5] == str(n) and w.split()[4] == chain :
				x = float(w.split()[6])
				y = float(w.split()[7])
				z = float(w.split()[8])
				pdbfile2 = open(pdb, "r")
				for i in pdbfile2 :
					if i[0:4] == "ATOM" and i.split()[2] in items and i.split()[4] in ab_chains : # Remove from 'and i.split()[4] ...' to
						a = float(i.split()[6])                                                 # include nearby residues from same chain
						b = float(i.split()[7])
						c = float(i.split()[8]) 
						sq_dist = (x-a)**2 + (y-b)**2 + (z-c)**2
						if sq_dist < 64.0 : 
							#	print "{0:4.2f}".format(sq_dist**0.5), i.split()[5], i.split()[4] # Uncomment this line to see each distance value
							if i.split()[4] == "L":
								L.append(i.split()[5])
							if i.split()[4] == "H":
								H.append(i.split()[5])
		P.extend(L)
		Q.extend(H)
	final_list1 = sorted(set(P),key=P.index) 
	final_list2 = sorted(set(Q),key=Q.index)

	print "There are ", len(final_list1), "contacting residues in chain L"
	print sorted(final_list1)
	print "There are ", len(final_list2), "contacting residues in chain H"
	print sorted(final_list2)

          #---------------------------------------------#

def is_near_chain(pdb, position, chainA, chainB) : # Tests if residue is contacting one of the two chains
    decision = False                               # Usually used for testing Heavy or Light chain contact
    pdbfile = open(pdb, "r")
    items = ["CA", "CB", "N", "C", "O"]
    for w in pdbfile :
            if w[0:4] == "ATOM" and w.split()[2] in items and w.split()[5] == position and w.split()[4] == chainA :
                x = float(w.split()[6])
                y = float(w.split()[7])
                z = float(w.split()[8])
                pdbfile2 = open(pdb, "r")
                for i in pdbfile2 :
                    if i[0:4] == "ATOM" and i.split()[2] in items :
                        a = float(i.split()[6])
                        b = float(i.split()[7])
                        c = float(i.split()[8])
                        sq_dist = (x-a)**2 + (y-b)**2 + (z-c)**2
                        if sq_dist < 36.0 and i.split()[4] == chainB :
                            decision = True
                            break
    return decision
