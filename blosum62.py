def score(m, n) :
	resint = dict(A=1, R=2, N=3, D=4, C=5, Q=6, E=7, G=8, H=9, I=10, L=11, K=12, M=13, F=14, P=15, S=16, T=17, W=18, Y=19, V=20, X=23)
	file = open("blosum62_mod.txt", "r")
	for lines in file :
		x =  lines.split( )[0]
		if(x == m) :
				return int(lines.split( )[resint[n]])
	file.close()
