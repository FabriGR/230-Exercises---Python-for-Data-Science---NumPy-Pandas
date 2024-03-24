'''Exercise 171
The df DataFrame is given below. Check the distribution of the transmission column and perform the following mapping:

- 'Manual' -> 0
- 'Automatic' -> 1

Print the first five rows of transmission column. '''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df['transmission'] = df['transmission'].map(
    {'Manual': 0, 'Automatic': 1}
)
print(df['transmission'].head())