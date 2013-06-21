n=raw_input()

x=float(n.split()[0])
y=float(n.split()[1])
z=float(n.split()[2])

if x<y+z:
	if y<x+z:
		if z<x+y:
			print 'YES'
		else:
			print 'NO'
	else:
		print 'NO'
else:
	print 'NO'

