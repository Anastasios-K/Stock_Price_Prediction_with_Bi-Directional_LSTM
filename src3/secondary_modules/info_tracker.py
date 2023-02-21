class InfoTracker:
    """
    Module used throughout the model to track useful information.
    The tracked info is either used later in the pipeline or saved by MLFlow at the last stage of the pipeline.
    """
    def __init__(self,
                 stock_name=None,
                 time_id=None,
                 nan_amount=None,
                 duplicates_amount=None):
        self.stock_name = stock_name
        self.time_id = time_id
        self.nan_amount = nan_amount
        self.duplicates_amount = duplicates_amount







