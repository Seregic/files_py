import matplotlib
import docx
import csv
w = set()
d = docx.Document('lion.docx')
for i in d.paragraphs :
    i.text.split()
    w.add(i)
w = list(w)

for i in range(0,len(w)-1) :
    k = 0
    for j in range(1,len(w)) :
        if i == j :
            k+=1
    p = k/len(w)*100
    with open('b.csv','a',encoding='UTF-8') as b :
       b.write('Слово',w[i],'Количество',k,'Процент',p)
    b.close()


