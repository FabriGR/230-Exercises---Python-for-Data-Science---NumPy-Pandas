'''Exercise 161
Using pandas load the following csv file into the DataFrame and assign to the df variable:
https://storage.googleapis.com/esmartdata-courses-files/dash-course/data.csv

Set the index to the first column and print this DataFrame to the console.'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
print(df)