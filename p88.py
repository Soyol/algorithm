n=input()
mas=[]
i=0
while n>0:
	a=n%10
	n=n/10
	mas[i]=a
	i+=1

b=mas[0]
mas[0]=mas[i-1]
mas[i-1]=mas[0]
c=0

for j in range(len(mas)-1,-1,-1):
	c=c*10+mas[j]	
print c					
