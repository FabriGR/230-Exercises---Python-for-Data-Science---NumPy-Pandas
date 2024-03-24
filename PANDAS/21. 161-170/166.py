'''Exercise 166
The df DataFrame is given below. Replace all letters in column names with lowercase, e.g.

Name -> name
Fuel_Type -> fuel_type

Print the first five rows using the pd.DataFrame.head() and print() function. '''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
print(df.head())