import json
import numpy as np
import pandas as pd
import sys

def analysis(file,user_id):
    times = 0
    minutes = 0

    try:
        filename='/home/shiyanlou/Code/'+file
        diclist=[json.loads(line) for line in open(filename)]
    except:
        return 0
    
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

    df=pd.DataFrame({'minutes':l1,
        'created_at':l2,
        'user_id':l3,
        'lab':l4,
        'course':l5})
    try:
        df1=df['minutes'].groupby(df['user_id'])
        times=df1.count()[int(user_id)]
        minutes = df1.mean()[int(user_id)]*times
    except:
        return 0
    
    return times,minutes

if __name__=='__main__':
    analysis(sys.argv[1],sys.argv[2])
