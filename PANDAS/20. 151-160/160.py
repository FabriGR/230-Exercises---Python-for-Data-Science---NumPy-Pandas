'''Exercise 160
The following df DataFrame is given. Remove the D column from this object and print DataFrame to the console.
'''
import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
df = df.drop('D', axis=1)
print(df)