import pandas as pd
from src.config.load_conifg import Config
from src.data_engineering.data_visualisation import DataOverview


class FixedDTypeData:
    fixed_dtype_data: pd.DataFrame
    config: Config

    @staticmethod
    def plot_data_various_resolutions(data, config, title):
        DataOverview(data=data, config=config, title=title)


class NoNanData(FixedDTypeData):
    no_nan_data: pd.DataFrame
    config: Config


class NoDuplicateData(FixedDTypeData):
    no_dupl_data: pd.DataFrame
    config: Config


class DataReady4Analsysi(NoNanData, NoDuplicateData):
    data_ready4analysis: pd.DataFrame
    config: Config
