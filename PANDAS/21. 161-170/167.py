'''Exercise 167
The df DataFrame is given below. Find the distribution of the owner_type column and print to the console.'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df['owner_type'].value_counts())