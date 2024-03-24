'''Exercise 170
The df DataFrame is given below. Group this DataFrame by year and count the number of rows for each year.

In response, print result to the console.
'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df.groupby('year').size())