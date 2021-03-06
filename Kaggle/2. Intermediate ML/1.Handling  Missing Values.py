# In this tutorial, you will learn three approaches to dealing with missing values.
# Then you'll compare the effectiveness of these approaches on a real-world dataset.
# 1) A Simple Option: Drop Columns with Missing Values
                        # Get names of columns with missing values
                        cols_with_missing = [col for col in X_train.columns
                                             if X_train[col].isnull().any()]

                        # Drop columns in training and validation data
                        reduced_X_train = X_train.drop(cols_with_missing, axis=1)
                        reduced_X_valid = X_valid.drop(cols_with_missing, axis=1)

                        print("MAE from Approach 1 (Drop columns with missing values):")
                        print(score_dataset(reduced_X_train, reduced_X_valid, y_train, y_valid))


# 2) A Better Option: Imputation
                    # Imputation fills in the missing values with some number.
                    # For instance, we can fill in the mean value along each column.

                    from sklearn.impute import SimpleImputer
                    # Imputation
                    my_imputer = SimpleImputer()
                    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
                    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))

                    # Imputation removed column names; put them back
                    imputed_X_train.columns = X_train.columns
                    imputed_X_valid.columns = X_valid.columns

                    print("MAE from Approach 2 (Imputation):")
                    print(score_dataset(imputed_X_train, imputed_X_valid, y_train, y_valid))

# 3) An Extension To Imputation
                    # In this approach, we impute the missing values, as before.
                    # And, additionally, for each column with missing entries in the
                    # original dataset, we add a new column that shows the location of the
                    # imputed entries.

                    # Make copy to avoid changing original data (when imputing)
                    X_train_plus = X_train.copy()
                    X_valid_plus = X_valid.copy()

                    # Make new columns indicating what will be imputed
                    for col in cols_with_missing:
                        X_train_plus[col + '_was_missing'] = X_train_plus[col].isnull()
                        X_valid_plus[col + '_was_missing'] = X_valid_plus[col].isnull()

                    # Imputation
                    my_imputer = SimpleImputer()
                    imputed_X_train_plus = pd.DataFrame(my_imputer.fit_transform(X_train_plus))
                    imputed_X_valid_plus = pd.DataFrame(my_imputer.transform(X_valid_plus))

                    # Imputation removed column names; put them back
                    imputed_X_train_plus.columns = X_train_plus.columns
                    imputed_X_valid_plus.columns = X_valid_plus.columns

                    print("MAE from Approach 3 (An Extension to Imputation):")
                    print(score_dataset(imputed_X_train_plus, imputed_X_valid_plus, y_train, y_valid))
