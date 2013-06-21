r1=raw_input()
r2=raw_input()
v1=float(r1.split()[0])
t1=float(r1.split()[1])
v2=float(r2.split()[0])
t2=float(r2.split()[1])
a=(v1*t1+v2*t2)/(v1+v2)
b=v1+v2
print '%.1f' % a
print '%.1f' % b
