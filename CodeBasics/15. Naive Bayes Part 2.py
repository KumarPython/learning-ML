import pandas as pd
df=pd.read_csv('spam.csv')

df['spam']=df['Category'].apply(lambda x: 1  if x=='spam' else 0)
y=df.spam
X=df.drop('spam',axis=1)
# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Change words into vectors using sklearn's CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
X_train_c=v.transform(X_train.values)
X_test_c=v.transform(X_test.values)

#Using Multinomial Niave-Bayes model to Train & Test my Data
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()

#Fit the model
model.fit(X_train_c,y_train)

#Predict using the trained model
pre=model.predict(X_test_c)

#Scoring the accuracy of the model
sco=model.score(X_test_c,y_test)
print(sco)



