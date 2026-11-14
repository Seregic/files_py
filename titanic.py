#вводим нужные нам библиотеки
import matplotlib.pyplot as plt
import pandas as pd
#читаем
a = pd.read_parquet('titanic.parquet')
#считаем процент выживших и погибших внутри каждого класса
p = pd.crosstab(a['Pclass'], a['Survived'], normalize='index') * 100
#строим диаграмму
b = p.plot(kind='bar',figsize=(10, 6),color=['red', 'green'],width=0.6,)
#настраиваем заголовки и подписи осей
plt.title('Процент выживших и погибших в зависимости от класса',fontsize=14,pad=15,)
plt.xlabel('Класс', fontsize=12)
plt.ylabel('Процент', fontsize=12)
plt.xticks(rotation=0)
plt.ylim(0, 110)  
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.legend(title='Статус', fontsize=11)
#добавляем точные цифры с процентами над каждым столбцом
for i in b.containers:
  b.bar_label(i, fmt='%.1f%%', padding=4, fontsize=11)
plt.tight_layout()
plt.savefig('sf.png')
plt.show()