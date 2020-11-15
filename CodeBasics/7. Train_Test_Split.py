import pandas as pd
df=pd.read_csv('carprices.csv')
print(df)
#
# import matplotlib as plt
# plt.scatter(df['Mileage'],df['Sell Price($)'])

X=df[['Mileage','Age(yrs)']]
y=df['Sell Price($)']
# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
print(len(X_train))

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)
p=reg.predict(X_test)
print(p)
s=reg.score(X_test,y_test)
print(s)