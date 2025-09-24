from kedro.pipeline import Pipeline, node
from .nodes import generate_report  # Asegúrate de que esta función exista en nodes.py

def create_pipeline():
    return Pipeline([
        node(
            func=generate_report,
            inputs=["metrics", "trained_model"],  # Ajusta según tus datasets
            outputs=None,  # Si solo imprime o guarda internamente
            name="generate_report_node"
        )
    ])