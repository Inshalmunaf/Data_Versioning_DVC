import pandas as pd
import os

data ={
    "Name" : ["Inshal" , "Zain" ,"Ahmed"],
    "Age" :[22,24,27],
    "Address" : ['abc' , 'xyz' , 'qwr']
}

df = pd.DataFrame(data)

new_person = {"Name" : "Aimen" , "Age" :22,"Address" : "rcb"}
df.loc[len(df.index)] = new_person

new_person = {"Name" : "Alina" , "Age" :23,"Address" : "mkr"}
df.loc[len(df.index)] = new_person

datadir= 'data'
os.makedirs(datadir ,exist_ok=True)

file_path=os.path.join(datadir , "sample.csv")

df.to_csv(file_path , index=False)

print('Csv file saved to ',file_path)