'''Exercise 175
The df DataFrame is given below. Note that the timestamp column is of object type. Change it to datetime type.

Using the pd.DataFrame.info() print some information about this DataFrame to the console.

Tip: Use the pd.to_datetime() function. '''

import pandas as pd

pd.set_option('max_columns', 9)
pd.set_option('display.width', 150)
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.info()