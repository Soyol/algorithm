n=raw_input()
x=float(n.split()[0])
y=float(n.split()[1])

if x>y:
	z=x-y
else:
	z=y-x+1
print round(z,1)
