from kedro.pipeline import Pipeline, node
from .nodes import prepare_features, train_model, evaluate_model

def create_pipeline():
    return Pipeline([
        node(prepare_features, inputs="df_merged", outputs=["X_train", "X_test", "y_train", "y_test"], name="prepare_features_node"),
        node(train_model, inputs=["X_train", "y_train"], outputs="trained_model", name="train_model_node"),
        node(evaluate_model, inputs=["trained_model", "X_test", "y_test"], outputs="metrics", name="evaluate_model_node")
    ])
