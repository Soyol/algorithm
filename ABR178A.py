n=input()
s=raw_input()
mas=[]
mas=s.split()
count=0
for i in range(n):
	if int(mas[i])%2!=0:
		count+=1
print count
