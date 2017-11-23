import json
import numpy as np
import pandas as pd
import sys
import types

def analysis(file,user_id):
    times = 0
    minutes = 0

    #with open('/home/shiyanlou/Code/shiyanlou/'+file,'r') as file:
        #json_str=file.readlines()
    filename='/home/shiyanlou/Code/shiyanlou/'+file
    diclist=[json.loads(line) for line in open(filename)]
    
    dict={}
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    l5=[]
    for i in diclist:
        for j in i:
            l1.append(j['minutes'])
            l2.append(j['created_at'])
            l3.append(j['user_id'])
            l4.append(j['lab'])
            l5.append(j['course'])

    a1=np.array([l1,l2,l3,l4,l5])
    print(a1)
    print(l4)
    #print(dict['minutes'])

if __name__=='__main__':
    analysis(sys.argv[1],sys.argv[2])
