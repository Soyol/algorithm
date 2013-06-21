x=input()
i=0
m=[]
while x>0:
	t=x%10
	x=x/10
	m.insert(i,t)
	i+=1
a=m[0]
m[0]=m[len(m)-1]
m[len(m)-1]=a
e=0
for num in range(len(m)-1,-1,-1):
	e=e*10+m[num]
print e
