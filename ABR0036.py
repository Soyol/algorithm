n=raw_input()
a=float(n.split()[0])
b=float(n.split()[1])
c=float(n.split()[2])

if b>a:
   if c>b:
	print 'YES'
   else:
	print 'NO'
else:
   print 'NO'
