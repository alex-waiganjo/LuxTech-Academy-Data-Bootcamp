import pandas as pd
import numpy as np

# Load the Csv file
df =pd.read_csv('WeatherData.csv')

# List the first 10 Rows
first_10_rows =df.head(10)
print(f'First 10 Rows:{first_10_rows}')

# List the last 10 Rows
last_10_rows = df.tail(10)
print(f'Last 10 Rows:{last_10_rows}')


# Total Rows and Columns
total_rows,total_columns =df.shape
print(f'Total Rows: {total_rows}')
print(f'Total Columns: {total_columns}')
