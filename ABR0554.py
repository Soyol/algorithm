n=input()
a=0
b=0
c=0
i=0
mas1=[]
mas2=[]
mas3=[]
while a <= n:
	if a*a+b*b==c*c:
		if a<=b:
			if b<=c:
			 	if c<=n:
					mas1.insert(i,a)
					mas2.insert(i,b)
					mas3.insert(i,c)
						
					i+=1
	if c<=100:
		c+=1
	elif b<=100:
		c=0
		b+=1
	else:
		b=0
		a+=1


for t in range(0,i):
	print mas1[t],mas2[t],mas3[t]
