# The most important part of the 3. Pandas library is the DataFrame.
# A DataFrame holds the type of data you might think of as a table.
# This is similar to a sheet in Excel, or a table in a SQL database.
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'

# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)

# print a summary of the data in Melbourne data
melbourne_data.describe()

# To choose variables/columns, we'll need to see a list of all columns in the dataset.
# That is done with the columns property of the DataFrame (the bottom line of code below).
melbourne_data.columns

# We'll use the dot notation to select the column we want to predict,
# which is called the prediction target. By convention, the prediction target is called y.
# So the code we need to save the house prices in the Melbourne data is
y = melbourne_data.Price

# The columns that are inputted into our model (and later used to make predictions)
# are called "features." In our case, those would be the columns used to determine the
# home price. Sometimes, you will use all columns except the target as features.
# Other times you'll be better off with fewer features.
# For now, we'll build a model with only a few features.
# Later on you'll see how to iterate and compare models built with different features.
# We select multiple features by providing a list of column names inside brackets.
# Each item in that list should be a string (with quotes).
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

# You will use the scikit-learn library to create your models.
# When coding, this library is written as sklearn, as you will see in the sample code.
# Scikit-learn is easily the most popular library for modeling the types of data typically
# stored in DataFrames.
# The steps to building and using a model are:
#Define: What type of model will it be? A decision tree? Some other type of model?
        #Some other parameters of the model type are specified too.
# Fit: Capture patterns from provided data. This is the heart of modeling.
# Predict: Just what it sounds like
# Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

# In practice, you'll want to make predictions for new houses coming on the market rather
# than the houses we already have prices for. But we'll make predictions for the first
# few rows of the training data to see how the predict function works.
print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))
