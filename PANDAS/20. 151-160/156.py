'''Exercise 156
The following df DataFrame is given. Note that the index after removing two rows in the df1 is not correct. Reset this index and print df DataFrame to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df1 = df.dropna()
df1 = df1.reset_index(drop=True)
print(df1)