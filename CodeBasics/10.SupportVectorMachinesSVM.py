import pandas as pd
from sklearn.datasets import  load_iris

iris=load_iris()

df=pd.DataFrame(iris.data,columns=iris.feature_names )
df['target']=iris.target

X=df.drop(['target'],axis=1)
y=df.target
print(X)
print(y)

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

# Get SVM followed by Training & Testing
from sklearn.svm import SVC
model=SVC()
model.fit(X_train,y_train)
pre=model.predict(X_test)
print(pre)
sco=model.score(X_test,y_test)
print(sco)