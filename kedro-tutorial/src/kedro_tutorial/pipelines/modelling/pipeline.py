from kedro.pipeline import Pipeline, node
from .nodes import split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(split_data, ["preprocessed_customers", "params:test_size", "params:random_state"], "split_data"),
            node(train_model, ["split_data", "params:random_state"], "rf_model"),
            node(evaluate_model, ["rf_model", "split_data"], None),
        ]
    )
