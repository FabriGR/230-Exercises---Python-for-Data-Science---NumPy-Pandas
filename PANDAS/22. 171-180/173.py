'''Exercise 173
Using pandas load the london_bike.csv file into the DataFrame and assign to df variable:

https://storage.googleapis.com/esmartdata-courses-files/ds-bootcamp/london_bike.csv

In response print basic information about this DataFrame to the console. '''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'ds-bootcamp/london_bike.csv'
)
df = pd.read_csv(url, index_col=0)
df.info()