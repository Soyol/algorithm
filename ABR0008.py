n=raw_input()
import math
r=float(n.split()[0])
n=int(n.split()[1])
a=float(2*r*math.sin(3.14/n))
p=float(n*a)
print round(p,1)
