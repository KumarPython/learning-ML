import pandas as pd
df = pd.read_csv("carprices.csv")
print(df)
#Getting Dummy Variables
dummies = pd.get_dummies(df['Car Model'])
print(dummies)

#Concatenation of  previous DataFrame with the new Dummies Dataframe
merged = pd.concat([df,dummies],axis=1)

#Dropping some useless columns
final=merged.drop(['Car Model','Mercedez Benz C class'],axis=1)
X=final.drop('Sell Price($)',axis=1)
print(X)

y=final['Sell Price($)']
print(y)

#Using the Linear Regression Classifier to Train & Test the Model
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)

#Scoring the Accuracy of the model
score=model.score(X,y)
print(score)

price=model.predict([[45000,4,0,0]])
print(price)