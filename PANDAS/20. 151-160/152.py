"""
Exercise 152
The following DataFrame is given:

|   df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

Extract rows of this DataFrame for which the C column is greater than 0.3 and the D column is less than 0.7. Print result to the console.
"""

import numpy as np
import pandas as pd
 
 
np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
print(df.loc[(df['C'] > 0.3) & (df['D'] < 0.7)])