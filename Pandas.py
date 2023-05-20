import pandas as pd
import numpy as np
l1=pd.Series({'a':10,'b':29,'d':23}, index=['a','d','b'],)

#print(l1)

n1 = {'a':10,'b':29,'d':23,'v':33}
d = pd.Series(n1,index=['a','d','b','v'])
#print(d[:2])

#s= pd.Series(5,index=['a','d','b'])
#print(s)
#print(d[-1:])

#print(l1+d,"\n")

#print(d[2] + l1[1])

print(d[['a','b']])