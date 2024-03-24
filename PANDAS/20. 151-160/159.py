'''Exercise 159
The following df DataFrame is given. Replace the order of the columns in the df object as following:
-   D, A, B, C

and assign to df variable. In respone, print this variable to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df = df[['D', 'A', 'B', 'C']]
print(df)