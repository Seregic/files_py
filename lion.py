import pandas as pd
import matplotlib as mp
import docx
import csv
h = ["Слово","Количество","Процент"]
with open('b.csv','a',encoding='UTF-8') as b :
       o = csv.DictWriter(b,fieldnames=h)
       o.writeheader()
b.close()
w = []
ch = []
d = docx.Document('lion.docx')
for i in d.paragraphs :
    l = i.text.split()
    w.extend(l)
r = len(w)
for i in range(0,len(w)) :
    if w[i] in ch:
        continue
    k = 1
    for j in range(i+1,len(w)) :
        if w[i] == w[j] :
            k+=1
    ch.append(w[i])
    p = k/r*100
    with open('b.csv','a',encoding='UTF-8') as b :
       o = csv.DictWriter(b,fieldnames=h)
       o.writerows([{"Слово":w[i],"Количество":k,"Процент": p}])
    b.close()




























