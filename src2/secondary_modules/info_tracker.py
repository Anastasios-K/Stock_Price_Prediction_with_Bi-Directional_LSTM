class InfoTracker:
    """
    Module used throughout the model to track useful information.
    The tracked info is either used later in the pipeline or saved by MLFlow at the last stage of the pipeline.
    """
    def __init__(self,
                 stock_name: str = None,
                 prediction_horizon=None):
        self.stock_name = stock_name
        self.prediction_horizon = prediction_horizon
