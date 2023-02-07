from src.data_engineering.handle_nan_values import DataWithoutNans
from src.data_engineering.handle_duplicates import DataWithoutDuplicates
from src.data_engineering.plot_diff_data_resolutions import DataResolutionPlot
from src.abstract.DataReady4AnalysisAbstract import DataReady4AnalysisAbstract
from src.data_finance_technical_analysis.moving_avg_convergence_divergence import MACD
from src.data_finance_technical_analysis.money_flow_index import MFI


class DataReady4Analysis(DataReady4AnalysisAbstract):
    """ Gathering of all data engineering methods."""

    _status = None

    def __init__(self, data, config):
        self.data = data
        self.config = config

    @staticmethod
    def __check_status(expected: str):
        if DataReady4Analysis._status is None:
            DataReady4Analysis._status = expected
        else:
            DataReady4Analysis._status = (
                    DataReady4Analysis._status +
                    expected
            )

    def handle_nan_values(self):
        self.__check_status(
            expected=self.config.dataengin.no_nans
        )
        obj = DataWithoutNans(
            data=self.data,
            config=self.config
        )
        self.data = obj.cooked_data

    def handle_duplicates(self):
        self.__check_status(
            expected=self.config.dataengin.no_dupl
        )
        obj = DataWithoutDuplicates(
            data=self.data,
            config=self.config
        )
        self.data = obj.cooked_data

    def plot_diff_df_resolutions(self, fig_title):
        obj = DataResolutionPlot(
            data=self.data,
            config=self.config,
            fig_title=fig_title
        )
        self.data = obj.cooked_data

    def add_mfi(self):
        mfi = MFI(
            dataframe=self.data,
            config=self.config
        ).mfi
        self.data["MFI"] = mfi

    def add_macd(self):
        macd = MACD(
            dataframe=self.data,
            config=self.config,
        ).macd
        self.data["MACD"] = macd
