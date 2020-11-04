# Pipelines are a simple way to keep your data preprocessing and modeling code organized.
# Specifically, a pipeline bundles preprocessing and modeling steps so you can use the whole
# bundle as if it were a single step.

# Step 1: Define Preprocessing Steps - Similar to how a pipeline bundles together
                            # preprocessing and modeling steps, we use the ColumnTransformer
                            # class to bundle together different preprocessing steps.
                            # The code below:imputes missing values in numerical data, and
                            # imputes missing values and applies a one-hot encoding to
                            # categorical data.
                            from sklearn.compose import ColumnTransformer
                            from sklearn.pipeline import Pipeline
                            from sklearn.impute import SimpleImputer
                            from sklearn.preprocessing import OneHotEncoder

                            # Preprocessing for numerical data
                            numerical_transformer = SimpleImputer(strategy='constant')

                            # Preprocessing for categorical data
                            categorical_transformer = Pipeline(steps=[
                                ('imputer', SimpleImputer(strategy='most_frequent')),
                                ('onehot', OneHotEncoder(handle_unknown='ignore'))
                            ])

                            # Bundle preprocessing for numerical and categorical data
                            preprocessor = ColumnTransformer(
                                transformers=[
                                    ('num', numerical_transformer, numerical_cols),
                                    ('cat', categorical_transformer, categorical_cols)
                                ])
# Step 2: Define the Model - Next, we define a random forest model with the familiar
                            # RandomForestRegressor class.
                            from sklearn.ensemble import RandomForestRegressor

                            model = RandomForestRegressor(n_estimators=100, random_state=0)

# Step 3: Create and Evaluate the Pipeline - Finally, we use the Pipeline class to define
                                            # a pipeline that bundles the preprocessing and modeling steps.
                            from sklearn.metrics import mean_absolute_error

                            # Bundle preprocessing and modeling code in a pipeline
                            my_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                                          ('model', model)
                                                         ])

                            # Preprocessing of training data, fit model
                            my_pipeline.fit(X_train, y_train)

                            # Preprocessing of validation data, get predictions
                            preds = my_pipeline.predict(X_valid)

                            # Evaluate the model
                            score = mean_absolute_error(y_valid, preds)
                            print('MAE:', score)