import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
def change(l):
    for i in (0,len(l)-1):
        l[i]=int(l[i])
    return l

if __name__=='__main__':
    filename='/home/shiyanlou/Code/user_study.json'
    diclist=[json.loads(line) for line in open(filename)]
    l1=[]
    l2=[]
    dict={}
    for i in diclist:
        for j in i:
            l1.append(j['minutes'])
            l2.append(j['user_id'])
    change(l1)
    change(l2)
    df=pd.DataFrame({'user_id':l2,'minutes':l1})
    dict=df['minutes'].groupby(df['user_id']).sum()
    ax=dict.plot(title='StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    plt.show()

