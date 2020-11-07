import pandas as pd
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np

digits=load_digits()
X=digits.data
y=digits.target

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


#Using KFold Cross Validation
# from sklearn.model_selection import KFold
# kf=KFold(n_splits=10)
#
# for train_index,test_index in kf.split(X):
#     X_train,X_test=X[train_index],X[test_index]
#     y_train,y_test=y[train_index],y[test_index]
#
# Using various Classifiers to measure their scores
    # rf=RandomForestClassifier()
    # rf.fit(X_train,y_train)
    # sco1=rf.score(X_test,y_test)
    # print(sco1)
    #
    # lr=LogisticRegression()
    # lr.fit(X_train,y_train)
    # sco2=lr.score(X_test,y_test)
    # print(sco2)
    #
    # svm=SVC()
    # svm.fit(X_train,y_train)
    # sco3=svm.score(X_test,y_test)
    # print(sco3)


 # Using Cross Validation Built-in Function
from sklearn.model_selection import cross_val_score
cross_val_score(LogisticRegression(),X,y)
cross_val_score(RandomForestClassifier(),X,y)
cross_val_score(SVC(),X,y)
