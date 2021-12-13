import os
import csv
import pandas as pd
out='/Users/11lal/Desktop/foodai/kfood/'

rows=[]
for i in os.listdir(out):

    if len(os.listdir(out+i))>50:
        index=1
    else:
        index=0
        
    rows.append([i, index, len(os.listdir(out+i))])
# field names  
fields = ['class_name', 'use', 'cnt']  
df = pd.DataFrame(rows, columns=fields) 
print('hello: ', rows)
#df.to_csv("file.csv", encoding="utf-8") 
df.to_csv('train_classes.csv',encoding='utf-8-sig')

