'''Exercise 163
The df DataFrame is given below. From this object, remove the column 'New_Price' and print the first 5 rows to the console.'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.drop('New_Price', axis=1, inplace=True)
print(df.head())