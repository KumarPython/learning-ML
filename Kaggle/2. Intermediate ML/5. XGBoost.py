# Gradient boosting is a method that goes through cycles to iteratively add models
# into an ensemble.
# It begins by initializing the ensemble with a single model, whose predictions can be
# pretty naive. (Even if its predictions are wildly inaccurate, subsequent additions to
# the ensemble will address those errors.)
# Then, we start the cycle:
# First, we use the current ensemble to generate predictions for each observation in the
# dataset. To make a prediction, we add the predictions from all models in the ensemble.
# These predictions are used to calculate a loss function
# (like mean squared error, for instance). Then, we use the loss function to fit a new model that will be added to the ensemble. Specifically, we determine model parameters so that adding this new model to the ensemble will reduce the loss. (Side note: The "gradient" in "gradient boosting" refers to the fact that we'll use gradient descent on the loss function to determine the parameters in this new model.)
# Finally, we add the new model to ensemble, and ...
# ... repeat!
            from xgboost import XGBRegressor

            my_model = XGBRegressor()
            my_model.fit(X_train, y_train)
            We also make predictions and evaluate the model.

            from sklearn.metrics import mean_absolute_error

            predictions = my_model.predict(X_valid)
            print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))

