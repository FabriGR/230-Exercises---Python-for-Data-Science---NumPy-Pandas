'''Exercise 164
The df DataFrame is given below. Find the number of missing values for each column and print result to the console. '''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.drop('New_Price', axis=1, inplace=True)
print(df.isnull().sum())