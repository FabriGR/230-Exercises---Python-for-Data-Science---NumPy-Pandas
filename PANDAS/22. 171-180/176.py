'''Exercise 176
The df DataFrame is given below. Extract time (in hours) from the timestamp column and assign to the new column 'hour'. Print the first five rows of this DataFrame to the console. '''

import pandas as pd

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
print(df.head())