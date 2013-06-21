n=raw_input()
a=float(n.split()[0])
h=float(n.split()[1])
n=int(n.split()[2])
import math
f1=0
sum=0
i=1
p=a
for t in range(0,n):
	p=h*i	
	f1=(p**2+1)*(math.cos(p))**2
	i+=1
	sum+=f1
print sum
