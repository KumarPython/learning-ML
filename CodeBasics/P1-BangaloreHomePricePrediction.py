import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CodeBasics import Rough


df=pd.read_csv('Bengaluru_House_Data.csv')

# Assuming that some columns are not important and dropping few columns
df=df.drop(['area_type','availability','society','balcony'],axis=1)
df=df.fillna('0 bhk')

# We take the first value of the string for size column
df['bhk']=df['size'].apply(lambda x: int(str(x).split(' ')[0]))

# We convert the range values to their average and convert units
df['total_sqft']=df['total_sqft'].apply(lambda x: Rough.range_to_average(str(x)))

# Creating a new column with each element of other 2 columns
for i in range(0,len(df)):
    pricepersqrft=float(df.price.loc[i])*100000/float(df.total_sqft.loc[i])
df['pricepersqrft']=pd.Dataframe(pricepersqrft)
print(df.head(5))

# Strip the location column of any extra spaces
df.location=df.location.apply(lambda x:x.strip())

# Check how many rows of each unique location
location_stats=df.groupby('location')['location'].agg('count')

# Check how many locations have less than 10 houses
len(location_stats[location_stats<=10])

# Seggregate all such locations as Other Locations
other_location=location_stats[location_stats<=10]

# Give a label of "Others" if it has less than 10 houses
df.location=df.location.apply(lambda x : 'other' if x in other_location else x)

# Selecting errorneous values for totalsqrft/bhk because they are related
# print(df[df.total_sqft/df.bhk<=300].head(5))
# print(df.head(10))