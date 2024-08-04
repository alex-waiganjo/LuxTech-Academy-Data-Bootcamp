import pandas as pd
import numpy as np

# Load the Csv file
df = pd.read_csv('WeatherData.csv')


# Question 1 

# Query Records where Weather was 'Clear'
# weather_is_clear = df[df['Weather'] == 'Clear']
# if weather_is_clear.empty:
#     print("Sorry, No Rows with Weather is 'Clear' were Found!")
# else:
#     print(weather_is_clear)
    


# Question 2

# Print all records with Windspeed of 4
# df.columns = df.columns.str.replace(' ','')
# wind_speed_is_4 = df[df["WindSpeed_km/h"] == 4]
# print(wind_speed_is_4)
# # Count the Total Rows
# count_total_rows = (df["WindSpeed_km/h"] == 4).sum()
# print(f'Total Rows with Speed of 4 are: {count_total_rows}')


# Question 3

# Check if there are any Null Values in the Columns
# check_if_null = df.isnull().sum()
# print(check_if_null)   


# Question 4

# Rename the Weather Column To Weather_condition
rename_column =df.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)


# Question 5

# Find the Mean Visibility 
# get_visibility_mean = df["Visibility_km"].mean()
# print(f'The Mean Value of the Visibility Column is :{get_visibility_mean}')


# Question 6

# Find the number of records where the wind speed is> 24 and visibility == 25
df.columns = df.columns.str.replace(' ','')
# Count the Total Rows
count_total_rows = (df["WindSpeed_km/h"] > 24  df["Visibility_km"] ==25).sum()
print(f'Total Rows with Speed greater than 24 are: {count_total_rows}')