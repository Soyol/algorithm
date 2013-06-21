n=raw_input()

mas=[]
mas=n.split()

for t in range(len(mas)):
	a=float(mas[t])
	if a>1:
	      if a<3:
		    print round(a,1)
