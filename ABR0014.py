n=raw_input()
r=float(n.split()[0])
m1=float(n.split()[1])
m2=float(n.split()[2])

g=6.67*0.00000000001
k=(g*m1*m2)/(r*r)
print '%.1f'%k
