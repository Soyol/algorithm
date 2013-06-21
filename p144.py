n=input()
mas=[]

mas.insert(0,0)
mas.insert(1,1)

for i in range(1,n+1):
	mas.insert(i,mas[i-1]+mas[i-2])
	
for i in range(0,n+1):
	print mas[i]
