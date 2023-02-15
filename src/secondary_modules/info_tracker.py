class InfoTracker:
    """
    Module used throughout the model to track useful information.
    The tracked info is either used later in the pipeline or saved by MLFlow at the last stage of the pipeline.
    """
    def __init__(self,
                 stock_name: str,
                 time_id: property(int)):
        self.stock_name = stock_name
        self.time_id = time_id

