import json
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
    print(type(diclist))

if __name__=='__main__':
    analysis(sys.argv[1],sys.argv[2])
