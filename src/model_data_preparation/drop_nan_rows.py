import pandas as pd
from src.model_data_preparation.split_train_test_data import SplitData


class DropRows:

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

    def split_data(self):
        return SplitData(data=self.data,
                         config=self.config)
