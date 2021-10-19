import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4])
print(s)

s= pd.Series([12,-4,7,9])
print(s)

z = pd.Series([-12,44,5,6], index = ['a','b','c','d'])
print(z)
print(z.values)
print(z.index)
print(s[2])
print(z['b'])
print(z[0:2])
print(z['b'])

s[1] = 55
print(s)

z['b'] = 990
print(z)
arr = np.array([2,4,6,7,8])
s3 = pd.Series(arr)
print(s3)
s4 = pd.Series(z)
print(s4)

arr[2] = -22
print(s3)

print(s[s > 10])
print(s/2)
print(s//2)
#print(np.log(z))

serd = pd.Series([1,0,2,1,2,3], index = ['white', 'white','blue','green','green','yellow'])
print(serd)
print(serd.unique())
print(serd.isin([0,3]))
print(serd[serd.isin([0,3])])
#print(serd.value_counts())

print('----------------------')
s2 = pd.Series([5,-3,np.NaN,14])
print(s2)
print(s2.isnull())
print(s2.notnull())
print(s2[s2.notnull()])
print(s2[s2.isnull()])
print('-----------------------')