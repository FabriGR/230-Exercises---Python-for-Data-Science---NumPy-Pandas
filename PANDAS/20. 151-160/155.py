'''Exercise 155
The following df DataFrame is given. Remove all rows from this object containing missing values and assign to variable df1.

In response, print this variable to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df1 = df.dropna()
print(df1)