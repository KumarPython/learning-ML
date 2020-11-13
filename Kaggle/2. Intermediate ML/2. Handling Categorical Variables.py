# You will get an error if you try to plug these variables into most machine learning
# models in Python without preprocessing them first. In this tutorial, we'll compare
# three approaches that you can use to prepare your categorical data.
# 1) Drop Categorical Variables-The easiest approach to dealing with categorical variables
                                # is to simply remove them from the dataset.
                                # This approach will only work well if the columns did not
                                # contain useful information.
                                drop_X_train = X_train.select_dtypes(exclude=['object'])
                                drop_X_valid = X_valid.select_dtypes(exclude=['object'])

                                print("MAE from Approach 1 (Drop categorical variables):")
                                print(score_dataset(drop_X_train, drop_X_valid, y_train, y_valid))

# 2) Label Encoding- Label encoding assigns each unique value to a different integer
                    from sklearn.preprocessing import LabelEncoder

                    # Make copy to avoid changing original data
                    label_X_train = X_train.copy()
                    label_X_valid = X_valid.copy()

                    # Apply label encoder to each column with categorical data
                    label_encoder = LabelEncoder()
                    for col in object_cols:
                        label_X_train[col] = label_encoder.fit_transform(X_train[col])
                        label_X_valid[col] = label_encoder.transform(X_valid[col])

                    print("MAE from Approach 2 (Label Encoding):")
                    print(score_dataset(label_X_train, label_X_valid, y_train, y_valid))

# 3) One-Hot Encoding - One-hot encoding creates new columns indicating the presence
                        # (or absence) of each possible value in the original data.
                        #We set handle_unknown='ignore' to avoid errors when the
                        # validation data contains classes that aren't represented in
                        # the training data, and
                        # setting sparse=False ensures that the encoded columns are
                        # returned as a numpy array (instead of a sparse matrix).
                        from sklearn.preprocessing import OneHotEncoder

                        # Apply one-hot encoder to each column with categorical data
                        OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
                        OH_cols_train = pd.DataFrame(OH_encoder.fit_transform(X_train[object_cols]))
                        OH_cols_valid = pd.DataFrame(OH_encoder.transform(X_valid[object_cols]))

                        # One-hot encoding removed index; put it back
                        OH_cols_train.index = X_train.index
                        OH_cols_valid.index = X_valid.index

                        # Remove categorical columns (will replace with one-hot encoding)
                        num_X_train = X_train.drop(object_cols, axis=1)
                        num_X_valid = X_valid.drop(object_cols, axis=1)

                        # Add one-hot encoded columns to numerical features
                        OH_X_train = pd.concat([num_X_train, OH_cols_train], axis=1)
                        OH_X_valid = pd.concat([num_X_valid, OH_cols_valid], axis=1)

                        print("MAE from Approach 3 (One-Hot Encoding):")
                        print(score_dataset(OH_X_train, OH_X_valid, y_train, y_valid))


# In contrast to label encoding, one-hot encoding does not assume an ordering of
# the categories. Thus, you can expect this approach to work particularly well if
# there is no clear ordering in the categorical data (e.g., "Red" is neither more
# nor less than "Yellow"). We refer to categorical variables without an intrinsic
# ranking as nominal variables.