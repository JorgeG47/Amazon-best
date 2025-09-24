from kedro.pipeline import Pipeline, node
from .nodes import generate_report  # o la función que uses

def create_pipeline():
    return Pipeline([
        node(
            func=generate_report,
            inputs=["metrics", "trained_model"],  # ajusta según tus datos
            outputs=None,
            name="generate_report_node"
        )
    ])