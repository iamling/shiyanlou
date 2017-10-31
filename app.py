#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import json,os
from flask import Flask,render_template

app=Flask (__name__)
app.config['TAMPLATES_AUTO_RELOAD']=True

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    title=[]
    l=[]
    lst=os.listdir(r"/home/shiyanlou/files/")
    for c in lst:
        if(os.path.isfile(r"/home/shiyanlou/files/"+str(c)) and c.endswith('.json')):
            l.append(r"/home/shiyanlou/files/"+str(c))
    for i in l:
        f=open(i,encoding='utf-8')
        setting=json.load(f)
        title.append(setting['title'])
        f.close()
    return render_template('index.html',title=title)

@app.route('/files/<filename>')
def file(filename):
    f= open (r"/home/shiyanlou/files/"+filename+".json")
    setting = json.load(f)
    f.close()
    return render_template('base.html',setting=setting)
