'''Exercise 162
The df DataFrame is given below. Extract list with column names of this DataFrame and print it to the console.'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
print(list(df.columns))