'''Exercise 168
The df DataFrame is given below. Look at the distribution of the engine column. Note that the type of this column is set to object. Remove the last three characters from each element in this column and convert this column to int type.

In response, print the first five rows using the pd.DataFrame.head() and print() function for two columns: 
- name
- engine
'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df.dropna(inplace=True)
df['engine'] = df['engine'].map(lambda x: int(x[:-3]))
print(df[['name', 'engine']].head())