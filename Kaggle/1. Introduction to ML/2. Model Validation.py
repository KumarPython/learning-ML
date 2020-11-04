# You'll want to evaluate almost every model you ever build.
# In most (though not all) applications, the relevant measure of model quality is
# predictive accuracy. In other words, will the model's predictions be close to what
# actually happens.
# There are many metrics for summarizing model quality, but we'll start with one called
# Mean Absolute Error (also called MAE).
from sklearn.metrics import mean_absolute_error
predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# Since models' practical value come from making predictions on new data, we measure
# performance on data that wasn't used to build the model. The most straightforward way
# to do this is to exclude some data from the model-building process, and then use those
# to test the model's accuracy on data it hasn't seen before. This data is called
# validation data.
# The scikit-learn library has a function train_test_split to break up the data into
# two pieces. We'll use some of that data as training data to fit the model, and we'll
# use the other data as validation data to calculate mean_absolute_error./
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))