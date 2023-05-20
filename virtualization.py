import pandas as pd
import numpy as np

date = pd.date_range('today',periods = 6)
n1 = np.random.rand(6,4)
Columns = ['a','b','c','d']

df1 = pd.DataFrame(n1,index=date,columns=(Columns))
 
#print(df1)
#df1.plot()

#date = pd.date_range('today',periods = 6)
#n1 = np.random.ran(6,2)          //rand= postive values
#Columns = ['A','B']

#df1 = pd.DataFrame(n1,index=date,columns=(Columns))
 
#print(df1)
#df1.plot()                  

data = {'animal':['cat','dog','cow','goat','snake','cat','dog','cow','goat','snake'],
        'AGE' :[1,3,10,5,np.nan,3,2,1,4,np.nan],
        'visits': [1,2,3,1,3,1,2,1,2,1]}

df2 = pd.DataFrame(data,index=('a','b','c','d','e','f','g','h','i','j'))

#print(df2)
#df2.plot.barh(stacked = True)        //Horizontal

#df2.plot.hist(stacked = False)       //Histtogram  

#df1.plot.hist(bins=20)
#df1.plot.box()                  //box chart
#df2.plot.area()
#df1.plot.scatter(x='a',y='d')
       
#df2.plot.pie(subplots = True)        //pie chart