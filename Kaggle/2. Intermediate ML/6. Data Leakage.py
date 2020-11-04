# Data leakage (or leakage) happens when your training data contains
# information about the target, but similar data will not be available when the model is
# used for prediction. This leads to high performance on the training set
# (and possibly even the validation data), but the model will perform poorly in production.
# In other words, leakage causes a model to look accurate until you start making decisions
# with the model, and then the model becomes very inaccurate.
# There are two main types of leakage: target leakage and train-test contamination.

# Target leakage
# Target leakage occurs when your predictors include data that will not be available at the
# time you make predictions. It is important to think about target leakage in terms of
# the timing or chronological order that data becomes available, not merely whether a
# feature helps make good predictions.

# Train-Test Contamination
# A different type of leak occurs when you aren't careful to distinguish training data
# from validation data.
# Recall that validation is meant to be a measure of how the model does on data that it
# hasn't considered before. You can corrupt this process in subtle ways if the validation
# data affects the preprocessing behavior. This is sometimes called train-test contamination.
# For example, imagine you run preprocessing (like fitting an imputer for missing values)
# before calling train_test_split(). The end result? Your model may get good validation
# scores, giving you great confidence in it, but perform poorly when you deploy it to
# make decisions.