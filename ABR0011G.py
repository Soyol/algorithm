n=raw_input()

import math
x=float(n.split()[0])
y=float(n.split()[1])
z=float(n.split()[2])

a=y+x/(y*y+abs(x*x/(y+x*x*x/3)))
b=1+math.tan(z/2)*math.tan(z/2)

print round(a,1)
print round(b,1)
