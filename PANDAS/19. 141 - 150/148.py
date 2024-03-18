""""
Exercise 148
The df DataFrame is given below. Extract rows for which the col2 takes values greater than 0.0 and print result to the console.
"""
# 1
import numpy as np
import pandas as pd
 
 
np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
 
df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.query("col2 > 0"))

# 2
"""
import numpy as np
import pandas as pd
 
 
np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
 
df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df[df['col2'] > 0])
"""