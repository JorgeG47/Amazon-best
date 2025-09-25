"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 1.0.0
"""

# src/amazon_best/pipelines/data_science/pipeline.py

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import dividir_datos, entrenar_modelo, evaluar_modelo, generar_predicciones

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=dividir_datos,
                inputs=["preprocessed_data", "params:data_science"], # Carga parámetros de data_science.yml
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="dividir_datos_node",
            ),
            node(
                func=entrenar_modelo,
                inputs=["X_train", "y_train"],
                outputs="model",
                name="entrenar_modelo_node",
            ),
            node(
                func=evaluar_modelo,
                inputs=["model", "X_test", "y_test"],
                outputs="metrics",
                name="evaluar_modelo_node",
            ),
            node(
                func=generar_predicciones,
                inputs=["model", "X_test", "y_test"],
                outputs="predictions",
                name="generar_predicciones_node",
            ),
        ]
    )