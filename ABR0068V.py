n=input()
mas=[]
mas.append(0)
mas.append(0)
mas.append(0)
mas.append(0)
i=0
while n>0:
	a=n%10
	n=n/10
	mas.insert(i,a)
	i+=1
if mas[0]!=mas[1]:
	if mas[1]!=mas[2]:
		if mas[2]!=mas[3]:
		   if mas[0]!=mas[2]:
	       	      if mas[0]!=mas[3]:
	 	          if mas[1]!=mas[3]:		     
				print 'YES'
			  else:			
				print 'NO'
		      else:
			print 'NO'
		   else:
			print 'NO'
		else:
			print 'NO'
	else:
		print 'NO'
else:
	print 'NO'
