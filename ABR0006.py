n=raw_input()
import math
a=float(n.split()[0])
b=float(n.split()[1])

w1=float(math.sqrt(a*a+b*b))
w2=float(a*b/2)

print round(w1,1)
print round(w2,1)

