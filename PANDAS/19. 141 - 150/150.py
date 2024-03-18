"""
Exercise 150
The df DataFrame is given below. Extract the first five rows of this object, convert to HTML and assign it to the df_html variable.

Print the contents of the df_html variable to the console
"""

# 1
import numpy as np
import pandas as pd

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df.head().to_html())

# 2

"""
import numpy as np
import pandas as pd

np.random.seed(42)
s1 = pd.Series(np.random.rand(20))
s2 = pd.Series(np.random.randn(20))

df = pd.concat([s1, s2], axis=1)
df.columns = ['col1', 'col2']
print(df[:5].to_html())
"""