a=raw_input()
k=int(a.split()[0])
l=int(a.split()[1])
if k<l:
	k=l
elif l<k:
	l=k
else:
	k=0
	l=0
print k,l
