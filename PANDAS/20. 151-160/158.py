'''Exercise 158
The following df DataFrame is given. Fill in the missing values with 0 and assign to the variable df. In response, print df to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
df = df.fillna(0)
print(df)