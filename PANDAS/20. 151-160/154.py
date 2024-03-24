'''Exercise 154
The following DataFrame is given:
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

Set the value in row with index 3 for column B as np.nan (use df.iloc) and also set the value in the row at index 8 for column D as np.nan (use df.loc).
Print DataFrame to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df.iloc[3, 1] = np.nan
df.loc[8, 'D'] = np.nan
print(df)