# Load data into dataframe
import pandas as pd
df=pd.read_csv('salaries.csv')
print(df)


# Define my X and y
X=df.drop('salary_more_then_100k',axis=1)
y=df['salary_more_then_100k']


# ML only works with numbers.So we need to convert columns 1,2,3 into number
# This is done using LabelEncoder
from sklearn.preprocessing import LabelEncoder
myle=LabelEncoder()
df['companyle']=myle.fit_transform(df['company'])
df['joble']=myle.fit_transform(df['job'])
df['degreele']=myle.fit_transform(df['degree'])

print(df)

# Drop unnecessary columns
final=df.drop(['company', 'job', 'degree', 'degreele'], axis=1)
print(final)

# Final X and y
X=final.drop('salary_more_then_100k ', axis=1)
y=final['salary_more_then_100k ']

# Train/Fit model
from sklearn.tree import DecisionTreeClassifier
mytree=DecisionTreeClassifier()
mytree.fit(X.y)