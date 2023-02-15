import pandas as pd
from src.model_data_preparation.train_test_split import SplitData
from src.model_data_preparation.drop_unsused_features import FeaturesInUse


class FullRows:

    def __init__(self,
                 data: pd.DataFrame,
                 config
                 ):
        self.data = self.__drop_nan_rows(data=data)
        self.config = config

    @staticmethod
    def __drop_nan_rows(data):
        data.dropna(inplace=True)
        return data

    def drop_unused_features(self):
        return FeaturesInUse(data=self.data,
                             config=self.config)
