import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from CodeBasics import Rough
from sklearn.preprocessing import OneHotEncoder


df=pd.read_csv('Bengaluru_House_Data.csv')

# Assuming that some columns are not important and dropping few columns.
# Filling the blank cells of other columns
df=df.drop(['society'],axis=1)
df['size']=df['size'].fillna('1 bhk')
df['total_sqft']=df['total_sqft'].fillna(1)
df['balcony']=df['balcony'].fillna(0)
df['bath']=df['bath'].fillna(0)

# We take the first value of the string for size column and make a new column bhk.
# We then convert the bhk column into int.
df['bhk']=df['size'].apply(lambda x: int(str(x).split(' ')[0]))
df['bhk']=df['bhk'].apply(lambda x: int(x))
df['bath']=df['bath'].apply(lambda x: int(x))
df['balcony']=df['balcony'].apply(lambda x: int(x))

# We convert the range values to their average and convert units
df['total_sqft']=df['total_sqft'].apply(lambda x: Rough.range_to_average(str(x)))

# Creating a new column with each element of other 2 columns
df['pricepersqrft']=df.price*100000/df.total_sqft

# Strip the location column of any extra spaces
df.location=df.location.apply(lambda x:str(x).strip())

# Check how many rows of each unique location
location_stats=df.groupby('location')['location'].agg('count')

# Check how many locations have less than 10 houses
len(location_stats[location_stats<=10])

# Seggregate all such locations as Other Locations
other_location=location_stats[location_stats<=10]

# Give a label of "Others" if it has less than 10 houses
df.location=df.location.apply(lambda x : 'other' if x in other_location else x)

# Selecting errorneous values for totalsqrft/bhk because they are related
# df[df.total_sqft/df.bhk<=300]

# Remove rows that are erraneous Sqrft/bhk combination
df=df[~(df.total_sqft/df['bhk']<=300)]

# Basic Stats of the column
df.pricepersqrft.describe()

# Bathrooms must have a parity with bhk
df=df[~(df.bath>=df.bhk+2)]

# Drop some useless features
df=df.drop(['size','pricepersqrft'],axis=1)

# Dealing with Categorical value column
df1=pd.get_dummies(df.location)
df2=pd.get_dummies(df.availability)
df3=pd.get_dummies(df.area_type)
df=pd.concat([df,df1,df2,df3],axis=1)

# To avoid DUMMY TRAP drop one dummy column each
X=df.drop(['availability','location', 'area_type','other','Ready To Move','Super built-up  1rea'], axis=1)
y=df.price

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25)

# Create and fit  the Model
from xgboost import XGBRegressor
model=XGBRegressor(n_estimators=500,early_stopping_rounds=5)

#Fit the model
model.fit(X_train,y_train)

#Predict using the trained model
pre=model.predict(X_test)

#Scoring the accuracy of the model
sco=model.score(X_test,y_test)
print(sco)

# Saving the Trained Model
import pickle
with open('BengaluruHomePricePredictionModel_Pickle','wb') as f:
    pickle.dump(model,f)

# The columns data columns are important. We need to save them also
import json
columns={'data_column': [col.lower() for col in X.columns]}
with open('Columns.JSON','w') as f:
    f.write(json.dumps(columns))

