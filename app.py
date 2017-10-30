#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import json,os
from flask import Flask,render_template

app=Flask (__name__)
app.config['TAMPLATES_AUTO_RELOAD']=True

@app.route('/')
def index():
    title=[]
    l=[]
    lst=os.listdir("/home/shiyanlou/files/")
    for c in lst:
        if(os.path.isfile(t="/home/shiyanlou/files/"+str(c)) and c.endswith('.json')):
            l.append(t)
    for i in l:
        f=open(i,encoding='utf-8')
        setting=json.load(f)
        title.append(setting['title'])
        f.close()
        return render_template('index.html',title=title)
