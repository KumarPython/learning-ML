import pandas as pd
df = pd.read_csv("carprices.csv")
print(df)

dummies = pd.get_dummies(df['Car Model'])
print(dummies)

merged = pd.concat([df,dummies],axis=1)
print(merged)

final=merged.drop(['Car Model','Mercedez Benz C class'],axis=1)
print(final)

X=final.drop('Sell Price($)',axis=1)
print(X)

y=final['Sell Price($)']
print(y)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
score=model.score(X,y)
print(score)

price=model.predict([[45000,4,0,0]])
print(price)