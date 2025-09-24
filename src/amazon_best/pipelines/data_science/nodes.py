def prepare_features(df_merged):
    from sklearn.model_selection import train_test_split

    X = df_merged[['price', 'discounted_price', 'rating', 'rating_count', 'category_x', 'brand']]
    y = df_merged['range_precio']
    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    from sklearn.pipeline import Pipeline
    from sklearn.compose import ColumnTransformer
    from sklearn.preprocessing import StandardScaler, OneHotEncoder
    from sklearn.ensemble import RandomForestClassifier

    num_features = ['price', 'discounted_price', 'rating', 'rating_count']
    cat_features = ['category_x', 'brand']

    preprocessor = ColumnTransformer([
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_features)
    ])

    pipeline = Pipeline([
        ('preprocessing', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    pipeline.fit(X_train, y_train)
    return pipeline


def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import classification_report
    y_pred = model.predict(X_test)
    return classification_report(y_test, y_pred, output_dict=True)