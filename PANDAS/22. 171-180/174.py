'''Exercise 174
The df DataFrame is given below. Print the first and last five rows of this object and look at the data. '''

import pandas as pd

pd.set_option('max_columns', 9)
pd.set_option('display.width', 150)
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)
df = pd.read_csv(url, index_col=0)
print(df.head())
print(df.tail())