import math
import itertools

table=[['pedro','pear'],['pedro','peach'],['pedro','plum'],['ramon','graph'],['ramon','pear'],['ferrero','peach']]
T=pd.DataFrame(table)
T.columns=['name','items']

my_list = list(set(T['name']))
for j in my_list:
  cc = list(itertools.combinations(T[T['name']==j]['items'], 2))
  for i in cc:
    table.append([j,i[0]+'&'+i[1]])

table2=[]
for i in ['pedro','ramon','ferrero']:
  for j in range(len(table)):
    if table[j][0]==i:
      table2.append(table[j])

T2=pd.DataFrame(table2)
T2.columns=['name','items']
T2
