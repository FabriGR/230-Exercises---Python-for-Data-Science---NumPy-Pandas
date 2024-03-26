'''
Exercise 178
The df DataFrame is given below. Group this DataFrame by month and calculate the average value for the hum column. Assign the result to humidity_by_month variable and reset the index.

In response, print humidity_by_month DataFrame to the console as shown below. '''

import pandas as pd

pd.set_option('max_columns', 15)
pd.set_option('display.width', 150)
url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)
df = pd.read_csv(url)
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['month'] = df['timestamp'].dt.month
humidity_by_month = df.groupby('month')['hum'].mean().reset_index()
print(humidity_by_month)