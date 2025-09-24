from kedro.pipeline import Pipeline
from amazon_best.pipelines.data_engineering import pipeline as de_pipeline
from amazon_best.pipelines.data_science import pipeline as ds_pipeline
from amazon_best.pipelines.reporting import pipeline as rpt_pipeline  # si lo usas

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "data_engineering": de_pipeline.create_pipeline(),
        "data_science": ds_pipeline.create_pipeline(),
        "reporting": rpt_pipeline.create_pipeline(),  # opcional
        "__default__": de_pipeline.create_pipeline() + ds_pipeline.create_pipeline()
    }