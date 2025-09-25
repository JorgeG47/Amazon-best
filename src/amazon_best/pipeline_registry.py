# src/amazon_best/pipeline_registry.py

from kedro.pipeline import Pipeline
from typing import Dict

from amazon_best.pipelines import data_engineering as de
from amazon_best.pipelines import data_science as ds
from amazon_best.pipelines import reporting as rp

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_engineering_pipeline = de.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    reporting_pipeline = rp.create_pipeline()

    return {
        "de": data_engineering_pipeline,
        "ds": data_science_pipeline,
        "rp": reporting_pipeline,
        "__default__": data_engineering_pipeline + data_science_pipeline + reporting_pipeline,
    }