import pandas as pd
df=pd.read_csv('titanic.csv')

#Dropping Useless columns
df=df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis=1)

y=df.Survived
X=df.drop('Survived',axis=1)

dummies=pd.get_dummies(X.Sex)
X=pd.concat([X,dummies],axis=1)

X=X.drop(['Sex'], axis=1)

#Checking whether any value of the Sex column is missing
X.columns[X.isna().any()]

#Filling up the missing values with the mean
X.Age=X.Age.fillna(X.Age.mean())

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Using Gaussian Niave-Bayes model to Train & Test my Data
from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

#Fit the model
model.fit(X_train,y_train)

#Predict using the trained model
pre=model.predict(X_test)

#Scoring the accuracy of the model
sco=model.score(X_test,y_test)
print(sco)


