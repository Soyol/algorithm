n=raw_input()

x=float(n.split()[0])
y=float(n.split()[1])
z=float(n.split()[2])
a=x+y+z
b=x*y*z
if a>b:
	print round(a,1)
else:
	print round(b,1)
