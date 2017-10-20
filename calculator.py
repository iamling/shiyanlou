#!/usr/bin/env python3
def ss(money):
	t=money*(0.08+0.02+0.005+0.06)
	return t

def tax(t):

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
	return m	

import sys
for i in range(1,len(sys.argv)):
	L=sys.argv[i].split(':')
	try:
		s=int(L[0])
		t=int(L[1])
	except:
		print("Parameter Error")
	
	m = ss(t)
	n = tax(t-m-3500)
	y=t-m-n
	y=format(y,".2f")
	v=str(s)
	u=str(y)
	print(v+":"+u)

