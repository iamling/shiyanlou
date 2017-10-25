#!/usr/bin/env python3
class config(object):
	def __init__(self,configfile):
		filename = configfile
		self._config={}
		with open(filename) as file:
			L=file.readlines()
		for i in range(1,len(L)+1):
			self._config[L[i-1].split('=')[0].strip()]=float(L[i-1].split('=')[1].strip())
	def get_config(self,key):
		return self._config[key]

class UserData(object):
	def __init__(self,userdatafile):
		filename=userdatafile
		self.userdata={}
		with open(filename) as file:
			L=file.readlines()
		for i in range(1,len(L)+1):
			self.userdata[int(L[i-1].split(',')[0].strip())]=int(L[i-1].split(',')[1].strip())
	def calculator(self,config):
		self.shebaolist={}
		self.taxlist={}
		self.salarylist={}
		for i in self.userdata.keys():
			self.shebaolist[i]=format(ss(self.userdata[i],config),".2f")
			self.taxlist[i]=format(tax(self.userdata[i]-float(self.shebaolist[i])-3500),".2f")
			self.salarylist[i]=format(self.userdata[i]-float(self.shebaolist[i])-float(self.taxlist[i]),".2f")
	def dumptofile(self,outputfile,userdata,shebaolist,taxlist,salarylist):
		filename=outputfile
		with open(filename,'w') as file:
			file.truncate()
		for i in userdata.keys():
			with open(filename,'a') as file:
				file.write(str(i)+','+str(userdata[i])+','+str(shebaolist[i])+','+str(taxlist[i])+','+str(salarylist[i])+'\n')

def ss(money,L):
	if money<L['JiShuL']:
		money=L['JiShuL']
	elif money>L['JiShuH']:
		money=L['JiShuH']
	t=money*(L['YangLao']+L['YiLiao']+L['ShiYe']+L['GongShang']+L['ShengYu']+L['GongJiJin'])
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

import sys,os
from multiprocessing import Process,Queue
queue = Queue()
args = sys.argv[1:]

def f1():
	index = args.index('-c')
	configfile=args[index+1]
	try:
		L = config(configfile)
	except:
		print('error,no found configfile')
	queue.put(L._config)

def f2():
	config=queue.get()
	index = args.index('-d')
	userdatafile=args[index+1]
	try:
		LL=UserData(userdatafile)
	except:
		print('error,no found userdatafile')
	LL.calculator(config)
	queue.put(LL)
	queue.put(LL.userdata)
	queue.put(LL.shebaolist)
	queue.put(LL.taxlist)
	queue.put(LL.salarylist)

def f3():
	index = args.index('-o')
	outputfile=args[index+1]
	LL=queue.get()
	userdata=queue.get()
	shebaolist=queue.get()
	taxlist=queue.get()
	salarylist=queue.get()
	try:
		LL.dumptofile(outputfile,userdata,shebaolist,taxlist,salarylist)
	except:
		print("no found outputfile,error")

def main():
	p1=Process(target=f1)
	p2=Process(target=f2)
	p3=Process(target=f3)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
	p3.start()

if __name__ == '__main__':
	main()

