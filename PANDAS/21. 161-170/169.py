'''Exercise 169
The df DataFrame is given below. Look at the distribution of the power column. Note that this column also has missing values as a 'null bhp'. Replace these values with np.nan. Use the np.where() function for this.

In response, print the distribution of the power column to the console (only the top five most common values). '''

import numpy as np
import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df['power'] = np.where(df['power'] == 'null bhp', np.nan, df['power'])
print(df['power'].value_counts()[:5])