"""
This is a boilerplate pipeline 'data_engeenering'
generated using Kedro 1.0.0
"""

# src/amazon_best/pipelines/data_engineering/pipeline.py

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import unir_y_crear_caracteristicas

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=unir_y_crear_caracteristicas,
                inputs=[
                    "raw_amazon",
                    "raw_amazon_products",
                    "raw_amazon_categories",
                    "raw_extra_products",
                    "params:data_engineering", # Carga los parámetros de data_engineering.yml
                ],
                outputs="preprocessed_data",
                name="nodo_preprocesamiento_completo",
            ),
        ]
    )