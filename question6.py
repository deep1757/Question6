t=int(input())
for i in range(t):
	c,d,l=input().split()
	c=int(c)
	d=int(d)
	l=int(l)

	if l%4!=0:
		print("no")
	else:
		y=c+d
		y=y-(l//4)
		if y>=0 and y<=min(c,2*d):
			print("yes")
		else:
			print("no")