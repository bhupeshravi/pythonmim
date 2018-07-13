import requests
import pandas as pd
from bs4 import BeautifulSoup
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import json
import urllib.request
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.ensemble import RandomForestClassifier
from xlrd import open_workbook
# import nltk
# from IPython.display import display, HTML
# from sklearn import tree
# from xlrd import open_workbook


dtf = pd.DataFrame()
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
  return 'Hello, Azure!'

@app.route('/equity',methods=['POST'])
def getequity():
    global dtf
    _cmpname = request.form['cmpname']
    a=[]
    b=[]
    c=[]
    d=[]
    cnt=1
    while(cnt<200):
        urlink="https://www.bseindia.com/corporates/ann.aspx?curpg="+str(cnt)+"&annflag=1&dt=&dur=D&dtto=&cat=&scrip=&anntype=C"
        # linkz = '<a href="'+urlink+'" target = "_blank">link</a>'
        page = requests.get(urlink)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(len(soup.findAll("td", class_="TTHeadergrey")) != 0):
            count = 0
            for i in soup.findAll("td", class_="TTHeadergrey"):
                while(count<4):
                    if(count == 0):
                        a.append(i.text)
                    elif(count == 3):
                        count=-1
                    count =count+1
                    break
            for i in soup.findAll("td", class_="TTRow_leftnotices"):
                if(i.text != "" and i.text != " \xa0"):
                    b.append(i.text)
        else:
            break
        cnt = cnt+20
    for i in range(0,len(a)):
        c.append(a[i]+ '        |      ' +b[i])
    dtf = pd.DataFrame({'Company details':c})
    if(_cmpname != ""):
        for i in dtf['Company details']:
            if(_cmpname in i or _cmpname.lower() in i or _cmpname.upper() in i or _cmpname.title() in i):
                d.append(i)
        newdf = pd.DataFrame({'Company details':d})
        dtf = newdf.to_json()
        return json.dumps({"result": dtf})
    else:
        dtf = dtf.to_json()
        return json.dumps({"result": dtf})

@app.route('/metf',methods=['POST'])
def getmetf():
    global dtf
    _cmpname = request.form['cmpname']
    a=[]
    b=[]
    c=[]
    d=[]
    cnt=1
    while(cnt<200):
        urlink="https://www.bseindia.com/corporates/ann.aspx?curpg="+str(cnt)+"&annflag=1&dt=&dur=D&dtto=&cat=&scrip=&anntype=M"
        # linkz = '<a href="'+urlink+'" target = "_blank">link</a>'
        page = requests.get(urlink)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(len(soup.findAll("td", class_="TTHeadergrey")) != 0):
            count = 0
            for i in soup.findAll("td", class_="TTHeadergrey"):
                while(count<4):
                    if(count == 0):
                        a.append(i.text)
                    elif(count == 3):
                        count=-1
                    count =count+1
                    break
            for i in soup.findAll("td", class_="TTRow_leftnotices"):
                if(i.text != "" and i.text != " \xa0"):
                    b.append(i.text)
        else:
            break
        cnt = cnt+20
    for i in range(0,len(a)):
        c.append(a[i]+ '        |      ' +b[i])
    dtf = pd.DataFrame({'Company details':c})
    if(_cmpname != ""):
        for i in dtf['Company details']:
            if(_cmpname in i or _cmpname.lower() in i or _cmpname.upper() in i or _cmpname.title() in i):
                d.append(i)
        newdf = pd.DataFrame({'Company details':d})
        dtf = newdf.to_json()
        return json.dumps({"result": dtf})
    else:
        dtf = dtf.to_json()
        return json.dumps({"result": dtf})

@app.route('/debt',methods=['POST'])
def getdebt():
    global dtf
    _cmpname = request.form['cmpname']
    a=[]
    b=[]
    c=[]
    d=[]
    cnt=1
    while(cnt<200):
        urlink="https://www.bseindia.com/corporates/ann.aspx?curpg="+str(cnt)+"&annflag=1&dt=&dur=D&dtto=&cat=&scrip=&anntype=D"
        # linkz = '<a href="'+urlink+'" target = "_blank">link</a>'
        page = requests.get(urlink)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(len(soup.findAll("td", class_="TTHeadergrey")) != 0):
            count = 0
            for i in soup.findAll("td", class_="TTHeadergrey"):
                while(count<4):
                    if(count == 0):
                        a.append(i.text)
                    elif(count == 3):
                        count=-1
                    count =count+1
                    break
            for i in soup.findAll("td", class_="TTRow_leftnotices"):
                if(i.text != "" and i.text != " \xa0"):
                    b.append(i.text)
        else:
            break
        cnt = cnt+20
    for i in range(0,len(a)):
        c.append(a[i]+ '        |      ' +b[i])
    dtf = pd.DataFrame({'Company details':c})
    if(_cmpname != ""):
        for i in dtf['Company details']:
            if(_cmpname in i or _cmpname.lower() in i or _cmpname.upper() in i or _cmpname.title() in i):
                d.append(i)
        newdf = pd.DataFrame({'Company details':d})
        dtf = newdf.to_json()
        return json.dumps({"result": dtf})
    else:
        dtf = dtf.to_json()
        return json.dumps({"result": dtf})

@app.route('/manda',methods=['POST'])
def getmanda():
    global dtf
    _cmpname = request.form['cmpname']
    a=[]
    b=[]
    c=[]
    d=[]
    cnt=1
    while(cnt<200):
        urlink="https://www.bseindia.com/corporates/ann.aspx?curpg="+str(cnt)+"&annflag=1&dt=&dur=D&dtto=&cat=&scrip=&anntype=C"
        page = requests.get(urlink)
        soup = BeautifulSoup(page.content, 'html.parser')
        if(len(soup.findAll("td", class_="TTHeadergrey")) != 0):
            count = 0
            for i in soup.findAll("td", class_="TTHeadergrey"):
                while(count<4):
                    if(count == 0):
                        a.append(i.text)
                    elif(count == 3):
                        count=-1
                    count =count+1
                    break
            for i in soup.findAll("td", class_="TTRow_leftnotices"):
                if(i.text != "" and i.text != " \xa0"):
                    b.append(i.text)
        else:
            break
        cnt = cnt+20
    for i in range(0,len(a)):
        chk = a[i] + ' | ' + b[i]
        c.append(chk)
    dtfn = pd.DataFrame({'Company details':c})
    for i in dtfn['Company details']:
        if("SAST" in i or "Acquisition" in i):
            d.append(i)
    dtf = pd.DataFrame({'Company details': d})
    if(_cmpname != ""):
        for i in dtf['Company details']:
            if(_cmpname in i or _cmpname.lower() in i or _cmpname.upper() in i or _cmpname.title() in i):
                d.append(i)
        newdf = pd.DataFrame({'Company details':d})
        dtf = newdf.to_json()
        return json.dumps({"result": dtf})
    else:
        dtf = dtf.to_json()
        return json.dumps({"result": dtf})


# @app.route('/search',methods=['POST'])
# def getsearch():
#     global dtf
#     d =[]
#     _cmpname = request.form['cmpname']
#     if(_cmpname != ""):
#         print(_cmpname)
#         # res = json.loads(dtf)
#         dtf = pd.read_json(dtf, typ='series', orient='records')
#         for i in dtf:
#             if(_cmpname in i):
#                 print(i)
#                 d.append(i)
#         newdf = pd.DataFrame({'Company details':d})
#         newdf = newdf.to_json()
#         dtf = newdf
#     return json.dumps({"result":dtf})



@app.route('/reload',methods=['POST'])
def getreload():
#   global dtf
  return json.dumps({"result": dtf})


@app.route('/moneyinmotion',methods=['POST'])
def getmoney():
  _topic = request.form['topic']
  dfrr = pd.read_excel('https://docs.google.com/spreadsheets/d/e/2PACX-1vRsprFuBCzOfQZIZPzdKPKFuSjlfIiBh1KTliDukv_bO60iX-9FvOvLLx2NW7z53nFF7ELHa0OdcZBa/pub?output=xlsx')
  dfrtrain = dfrr
  txt=_topic
  finalwordlist =[]
  finalcountlist =[]
  final = txt
#   final = "Microsoft accquired Github"
  alltext=final.lower()
  letters="abcdefghijklmnopqrstuvwxyz$-. "
  alltext = ''.join([e for e in alltext if e in letters])
  rough=alltext.split()
  dic = defaultdict(int)
  for i in range(0, len(rough)-2):
    dic[str(rough[i]) + ' ' + str(rough[i+1])+' '+str(rough[i+2])] +=1
  div=len(dic)
  for keys,values in dic.items():
    if(values>0):
        finalwordlist.append(keys)
        finalcountlist.append(values/div)
  dic1 = defaultdict(int)
  for i in range(0, len(rough)-1):
    dic1[str(rough[i]) + ' ' + str(rough[i+1])] +=1
  div=len(dic1)
  for keys,values in dic1.items():
    if(values>0):
        finalwordlist.append(keys)
        finalcountlist.append(values/div)
        
#   stop_words = set(stopwords.words('english'))
#   word_tokens = word_tokenize(alltext)
#   words=[]
#   for w in word_tokens:
#     words.append(w)
#     if w not in stop_words:
  dic2 = defaultdict(int)
  for i in range(0, len(alltext)):
    dic2[str(alltext[i])] +=1
  div=len(dic2)
  for keys,values in dic2.items():
    if(values>0):
        finalwordlist.append(keys)
        finalcountlist.append(values/div)
        
  dictionary = dict(zip(finalwordlist, finalcountlist))

  for i in dfrtrain.columns:
    lets=False
    for key,value in  dictionary.items():
        if (i==key):
            dfrtrain[i].ix[80] = value
            lets=True
            break
    if(lets==False):
        dfrtrain[i].ix[80] = 0 
        
  X1 = dfrtrain.iloc[:80, :498]
  Y1 = dfrtrain.iloc[:80, 498:]
  X2 = dfrtrain.iloc[80:, :498]
  forest = RandomForestClassifier(max_depth = 15, min_samples_split=3, n_estimators = 100, random_state = 1)
  my_forest = forest.fit(X1, Y1)
  Yp = my_forest.predict(X2) 
  return json.dumps({"result": str(Yp[0])})


if __name__ == '__main__':
    app.run()
