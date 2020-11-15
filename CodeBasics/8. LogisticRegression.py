import pandas as pd
df=pd.read_csv('insurance_data.csv')
print(df)
X=df[['age']]
y=df['bought_insurance']

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1)

from sklearn.model_selection import LogisticRegression
reg=LogisticRegression()
reg.fit(X_train,y_train)
p=reg.predict(X_test)
print(p)