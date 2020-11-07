import pandas as pd
from sklearn.datasets import load_digits
digits=load_digits()
df=pd.DataFrame(digits.data)
X=df
y=digits.target

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#Using Random Forest Classifier to Train & Test my Data
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()

#Fit the model
model.fit(X_train,y_train)

#Predict using the trained model
pre=model.predict(X_test)

#Scoring the accuracy of the model
sco=model.score(X_test,y_test)
print(sco)

#Plotting Confusion Matrix.Here we First supply the Truth and then the Predicted
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,pre)
print(cm)
