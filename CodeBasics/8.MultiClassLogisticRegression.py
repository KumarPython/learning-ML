from sklearn.datasets import load_digits


# Creating an object of the class
digits=load_digits()
print(digits.data[0])


# Plotting the greyscale image
import matplotlib.pyplot as plt
plt.gray()
plt.matshow(digits.images[0])

# Train Test Split.By Default the split is random. It gives 4 outputs with 2 inputs.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)


# Importing Logistic Regression module.Fit/Train the model & Predict using the trained model
from sklearn.model_selection import LogisticRegression
reg=LogisticRegression()
reg.fit(X_train,y_train)
print(reg.predict(X_test))
