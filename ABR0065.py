n=input()
b=n
sum=0
while n>0:
	a=n%10
	n=n/10
	sum+=a*a*a
if sum == b*b:
	print 'YES'
else:
	print 'NO'
