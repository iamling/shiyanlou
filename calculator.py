#!/usr/bin/env python3

class config(object):
	def __init__(self,configfile):
		filename = configfile
		self._config={}
		with open(filename) as file:
			L=file.readlines()
		for i in range(1,len(L)+1):
			self._config[L[i-1].split()[0].strip()]=float(L[i-1].split()[2])
	def get_config(self,key):
		return self._config[key]

class UserData(object):
	def __init__(self,userdatafile):
		filename=userdatafile
		self.userdata={}
		with open(filename) as file:
			L=file.readlines()
		for i in range(1,len(L)+1):
			self.userdata[int(L[i-1].split(',')[0])]=int(L[i-1].split(',')[1])
	def calculator(self):
		self.shebaolist={}
		self.taxlist={}
		self.salarylist={}
		for i in self.userdata.keys():
			self.shebaolist[i]=format(ss(self.userdata[i],L._config),".2f")
			self.taxlist[i]=format(tax(self.userdata[i]-float(self.shebaolist[i])-3500),".2f")
			self.salarylist[i]=format(self.userdata[i]-float(self.shebaolist[i])-float(self.taxlist[i]),".2f")
	def dumptofile(self,outputfile):
		filename=outputfile
		with open(filename,'w') as file:
			file.truncate()
		for i in self.userdata.keys():
			with open(filename,'a') as file:
				file.write(str(i)+','+str(self.userdata[i])+','+str(self.shebaolist[i])+','+str(self.taxlist[i])+','+str(self.salarylist[i])+'\n')

def ss(money,L):
	if money<L['JiShuL']:
		money=L['JiShuL']
	elif money>L['JiShuH']:
		money=L['JiShuH']
	t=money*(L['Yanglao']+L['YiLiao']+L['ShiYe']+L['GongShang']+L['ShengYu']+L['GongJiJin'])
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
try:
	args = sys.argv[1:]
	index = args.index('-c')
	configfile=args[index+1]
	index = args.index('-d')
	userdatafile=args[index+1]
	index = args.index('-o')
	outputfile=args[index+1]
except:
	print("error,don't exit")

L = config (configfile)
LL= UserData(userdatafile)
LL.calculator()
LL.dumptofile(outputfile)
