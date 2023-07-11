from kedro.pipeline import Pipeline, node
from .nodes import preprocess_data

def create_pipeline(**kwargs):
    return Pipeline([
        node(preprocess_data, "customers", "preprocessed_customers"),
    ])
