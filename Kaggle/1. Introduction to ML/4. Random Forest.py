# The random forest uses many trees, and it makes a prediction by averaging the
# predictions of each component tree. It generally has much better predictive accuracy than
# a single decision tree and it works well with default parameters.
# If you keep modeling, you can learn more models with even better performance,
# but many of those are sensitive to getting the right parameters.
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))