"""
Exercise 149
The df DataFrame is given below. Extract first five rows of the df and convert into the dictionary as shown below.

In response, print this dictionary to the console.
"""

# 1
import numpy as np
import pandas as pd
 
 
np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
 
df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.head().to_dict())

# 2
"""
import numpy as np
import pandas as pd
 
 
np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))
 
df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df[:5].to_dict())
"""