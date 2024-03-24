'''Exercise 165
The df DataFrame is given below. Remove all rows with missing values in this object (use the inplace=True argument) In response, print info about df to the console. '''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.dropna(inplace=True)
df.info()