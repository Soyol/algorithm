t=raw_input()
a=int(t.split()[0])
b=int(t.split()[1])
r=int(t.split()[2])
s=int(t.split()[3])

if a%b == r:
	print 'R'
elif a%b == s:
	print 'S'
else:
	print 'No solution'
