from src.data_exploration.eda_pd_profiling import ProfilingEDA
from src.data_exploration.plot_correlation import CorrPlot
from src.data_exploration.plot_distribution import DistributionPlot
from src.data_exploration.plot_autocorrelation import AutocorrPlot
from src.data_engineering.engineering_management import DataReady4Analysis
from src.data_TA_features.data_with_ta_features import TaFeaturesAddition


class DataExploration:

    def __init__(self, obj: DataReady4Analysis or TaFeaturesAddition):
        if isinstance(obj, DataReady4Analysis):
            self.__data = obj.data_ready4analysis
            self.__config = obj.config
        elif isinstance(obj, TaFeaturesAddition):
            self.__data = obj.data_with_TA_features
            self.__config = obj.config
        else:
            raise ValueError("DataExploration requires DataReady4Analysis or TaFeaturesAddition")

    def pd_profiling_eda(self, report_name: str):
        ProfilingEDA(
            dataframe=self.__data,
            config=self.__config,
            report_name=report_name
        )

    def plot_data_distribution(self):
        DistributionPlot(
            dataframe=self.__data,
            config=self.__config
        )

    def plot_correlation(self,
                         fig_title: str,
                         corr_method="pearson"):
        CorrPlot(
            dataframe=self.__data,
            config=self.__config,
            fig_title=fig_title,
            corr_method=corr_method
        )

    def plot_autocorrelations(self):
        AutocorrPlot(
            dataframe=self.__data,
            config=self.__config
        )
