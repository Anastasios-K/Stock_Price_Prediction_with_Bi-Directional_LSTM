import pandas as pd
from src.config.load_conifg import Config
from src.model_data_preparation.train_test_split import SplitData


class FeaturesInUse:

    def __init__(self,
                 data: pd.DataFrame,
                 config: Config):
        self.config = config
        self.data = self.__drop_unused_columns(data=data)

    def __drop_unused_columns(self, data: pd.DataFrame) -> pd.DataFrame:
        [
            data.drop(columns=[col], inplace=True)
            for col
            in data.columns
            if col not in self.config.featuresinuse.features
        ]
        return data

    def split_data(self) -> SplitData:
        return SplitData(data=self.data,
                         config=self.config)
