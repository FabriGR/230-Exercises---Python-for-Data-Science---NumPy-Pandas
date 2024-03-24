'''Exercise 157
The following df DataFrame is given. Calculate the number of missing values in this object for each column.

In response, print result to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
print(df.isnull().sum())