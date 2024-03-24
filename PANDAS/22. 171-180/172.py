'''Exercise 172
The df DataFrame is given below. Save this object to the cars.csv file (do not save the index).
'''

import pandas as pd

url = (
    'https://storage.googleapis.com/esmartdata-courses-files/'
    'dash-course/data.csv'
)
df = pd.read_csv(url, index_col=0)
df.columns = [col.lower() for col in df.columns]
df.to_csv('cars.csv', index=False)