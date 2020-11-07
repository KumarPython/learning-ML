from sklearn.datasets import load_iris
from sklearn.svm import SVC
iris=load_iris()
from sklearn.model_selection import GridSearchCV
clf=GridSearchCV(SVC(gamma='auto'),{
    'C':[1,10,20],
    'kernel':['rbf','linear']
},cv=5,return_train_score=False)


clf.fit(iris.data,iris.target)
