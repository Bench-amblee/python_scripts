import numpy as np
import pandas as pd
from pandas import Series, DataFrame
obj = pd.Series([4,7,-5,3])
obj
obj.values
obj.index
obj2 = pd.Series([4,7,-5,3], index = ['d','b','a','c'])
obj2
obj2['d'] = 6
obj2
obj2[obj2 > 0]
obj2 * 2
np.exp(obj2)
'b' in obj2
'e' in obj2
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
obj3
states = ['California', 'Ohio','Oregon','Texas']
obj4 = pd.Series(sdata, index = states)
obj4
pd.isnull(obj4)
obj3 + obj4 
obj4.name = 'population'
obj4.index.name = 'state'
obj4
obj
obj.index = ['Bob','Steve','Jeff','Ryan']
obj
#DataFrame
data = {'state': ['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],
       'year': [2000,2001,2002,2001,2002,2003],
       'pop': [1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)
frame
frame.head()
pd.DataFrame(data,columns=['year','state','pop'])
frame2 = pd.DataFrame(data,columns=['year','state','pop','debt'],
                     index=['one','two','three','four',
                            'five','six'])
frame2
frame2.columns
frame2['state']
frame2.year
frame2.state
frame2.loc['three']
frame2['debt'] = 16.5
frame2
frame2['debt'] = np.arange(6.)
frame2
frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern']
frame2.columns
