n=input()
if n<10:
	a=0
	b=0
	c=0
	d=n
elif n<100:
	a=0
	b=0
	c=n/10
	d=n%10
elif n<1000:
	a=0
	b=n/100
	c=(n/10)%10
	d=n%10
elif n<10000:
	a=n/1000
	b=(n/100)%10
	c=(n/10)%10
	d=n%10
if a==d:
	if b==c:
		print 'YES'
	else:
		print 'NO'		
else:
	print 'NO'
