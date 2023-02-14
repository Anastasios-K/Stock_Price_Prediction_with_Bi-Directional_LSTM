import pandas as pd
from src.config.load_conifg import Config
from src.model_data_preparation.drop_nan_rows import FullRows
from src.data_engineering.engineering_management import DataReady4Analysis
from src.data_TA_features.data_with_ta_features import TaFeaturesAddition


class LabelsCreator:

    def __init__(self, obj: DataReady4Analysis or TaFeaturesAddition):
        if isinstance(obj, DataReady4Analysis):
            self.__data: pd.DataFrame = obj.data_ready4analysis
            self.__config: Config = obj.config
        elif isinstance(obj, TaFeaturesAddition):
            self.__data: pd.DataFrame = obj.data_with_TA_features
            self.__config: Config = obj.config
        else:
            raise ValueError("DataExploration requires DataReady4Analysis or TaFeaturesAddition")

        diff_col = "Diff"
        data = self.__data
        config = self.__config

        data_with_diff = self.__calc_price_difference(
            data=data,
            config=config,
            diff_col=diff_col
        )
        self.data = self.__create_labels(
            data_with_diff=data_with_diff,
            config=config,
            diff_col=diff_col
        )
        self.config = config

    @staticmethod
    def __calc_price_difference(data: pd.DataFrame,
                                config: Config,
                                diff_col: str) -> pd.DataFrame:
        shifted_col = "Shifted_Close"

        data[shifted_col] = data[config.dfstructure.close].shift(1)
        data[diff_col] = (data[config.dfstructure.close] / data[shifted_col]) - 1
        return data

    @staticmethod
    def __create_labels(data_with_diff: pd.DataFrame,
                        config: Config,
                        diff_col: str) -> pd.DataFrame:
        tollerance = config.labeltolerance.tolerance
        data_with_diff.loc[
            data_with_diff[diff_col] > tollerance,
            config.dfstructure.labels
        ] = 1
        data_with_diff.loc[
            data_with_diff[diff_col] < -tollerance,
            config.dfstructure.labels
        ] = -1
        data_with_diff.loc[
            (data_with_diff[diff_col] < tollerance) &
            (data_with_diff[diff_col] > -tollerance),
            config.dfstructure.labels
        ] = 0
        return data_with_diff

    def drop_nan_rows(self) -> FullRows:
        return FullRows(data=self.data,
                        config=self.config)
