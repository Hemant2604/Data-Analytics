import pandas as pd
import numpy as np
#data = pd.DataFrame({"Name":["Dhananjay","Hemant","Suraj"],"Age":[19,16,22]},index=(1,2,3))
#print(data)

#print("\n")

#df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
#print(df2)

#print("\n")

#data = [['Dhananjay',10],['Hemant',23]]
#df = pd.DataFrame(data,columns=('Name','Age'))
#print(df )
#print("\n")


#d2 = [{'a':2,'b':5},{'a':2,'b':3,'c':7}]
#print(pd.DataFrame(d2))


d = {'one' : pd.Series([1,2,3], index=['a','b','c']),
     'two' :pd.Series([1,2,3,4], index=['a','b','c','d'])}
df =pd.DataFrame(d)
#print("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
#print (df)
#print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
#print(df)

#del df['four']
#print(df)

#df.pop('one')
#print(df)

print (df.loc['a'])