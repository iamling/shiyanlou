#!/usr/bin/env python3
import sys
for i in range(1,len(sys.argv)):
	L=sys.argv[i].split(':')
	z=L[0]
	n=L[1]
	try:
		s=int(z)
		t=int(n)
	except:
		print("Parameter Error")

	t=t*(1-0.08-0.02-0.005-0.06)-3500
	if t<=0:
		m=0
	elif t<=1500:
		m=t * 0.03
	elif t<=4500:
		m = t*0.1 - 105
	elif t<=9000:
		m=t*0.2 - 555
	elif t<=35000:
		m = t*0.25 - 1005
	elif t<=55000:
		m = t*0.3 - 2755
	elif t<=80000:
		m=t*0.35 - 5505
	else:
		m=t*0.45 - 13505
	

	y=t-m+3500
	y=format(y,".2f")
	print(s,':',y )

