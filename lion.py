#вводим нужные нам библиотеки
from collections import Counter
import matplotlib.pyplot as mp
import docx
import csv
#задаем массив с заголовками
h = ["Слово","Количество","Процент"]
#задаем массив для записи туда отдельно слов
w = []
d = docx.Document('lion.docx')
#добавляем слова в массив
for i in d.paragraphs :
    l = i.text.lower().split()
    w.extend(l)
#считаем количество каждого слова
cou =  Counter(w)
#получаем списки слов и их количества для диаграммы
ch = list(cou.keys())
co = list(cou.values())
#задаем переменную куда записываем длину для дальнейшего подсчета процентов
r = len(w)
#начинаем счет и запись слов в csv
with open('b.csv','a',encoding='UTF-8') as b :
 o = csv.DictWriter(b,fieldnames=h)
 o.writeheader()
 for i,k in cou.items() :
    p = round(k/r*100,4)
    o.writerow({"Слово":i,"Количество":k,"Процент": p})
b.close()
#составление диаграммы
mp.figure(figsize=(14, 6))
mp.bar(ch[:25], co[:25], color="blue")
mp.title("Процент")
mp.xlabel("Слово")
mp.ylabel("Количество")
mp.xticks(rotation=45)
mp.savefig('words.png')
mp.show()


#задаем массив с заголовками
h = ["Буква","Количество","Процент"]
#задаем массив для записи туда отдельно букв
w = []
d = docx.Document('lion.docx')
#добавляем буквы в массив, переводим их в нижний регистр
for i in d.paragraphs :
    for j in i.runs:
        j.text = j.text.lower()
for i in d.paragraphs :
    for j in i.text :
       if j.isalpha() :
         w.extend(j)
#считаем количество букв
cou =  Counter(w)
#получаем списки букв и их количества для диаграммы
ch = list(cou.keys())
co = list(cou.values())
#задаем переменную куда записываем длину для дальнейшего подсчета процентов
r = len(w)
#начинаем счет и запись букв в csv
with open('b.csv','a',encoding='UTF-8') as b : 
 o = csv.DictWriter(b,fieldnames=h)
 o.writeheader()
 for i,k in cou.items() :
    p = round(k/r*100,4)
    o.writerow({"Буква":i,"Количество":k,"Процент": p})
b.close()
#составление диаграммы
mp.figure(figsize=(20, 6))
mp.bar(ch, co, color="blue")
mp.title("Процент")
mp.xlabel("Буква")
mp.ylabel("Количество")
mp.savefig('letters.png')
mp.show()

























