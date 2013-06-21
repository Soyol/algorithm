n=raw_input()
a=int(n.split()[0])
b=int(n.split()[1])
q=a
while q:
	if q%a==0:
		if q%b==0:
			break	
	q+=1
			
print q
