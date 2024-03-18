"""
Exercise 153
The following DataFrame is given:

|   df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

Iterate through the first five rows of this object and print each row to the console as shown below.

Tip: Use the pd.DataFrame.iterrows() function.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))
for index, row in df.head().iterrows():
    print(row)