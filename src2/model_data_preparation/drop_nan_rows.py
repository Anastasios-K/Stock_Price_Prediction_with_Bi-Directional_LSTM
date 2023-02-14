import pandas as pd
from src.config.load_conifg import Config
from src.model_data_preparation.drop_unsused_features import FeaturesInUse


class FullRows:

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):
        self.data = self.__drop_nan_rows(data=data)
        self.config = config

    @staticmethod
    def __drop_nan_rows(data) -> pd.DataFrame:
        data.dropna(inplace=True)
        return data

    def drop_unused_features(self) -> FeaturesInUse:
        return FeaturesInUse(data=self.data,
                             config=self.config)
