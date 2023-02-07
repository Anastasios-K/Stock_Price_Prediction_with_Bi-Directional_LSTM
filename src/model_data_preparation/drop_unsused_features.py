import pandas as pd
from src.model_data_preparation.split_train_test_data import SplitData


class FeaturesInUse:

    def __init__(self,
                 data: pd.DataFrame,
                 config):
        self.data = data
        self.config = config

    def __drop_unused_columns(self):
        for col in self.data.columns:
            if col not in self.config.featuresinuse:
                self.data.drop(columns=[col], inplace=True)

    def split_data(self):
        return SplitData(data=self.data,
                         config=self.config)
