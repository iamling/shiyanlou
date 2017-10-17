#!/usr/bin/env python3
import sys
try:
	t=int(sys.argv[1])
except:
	print("Parameter Error")

t=t-3500
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

m=format(m,".2f")
print(m)
